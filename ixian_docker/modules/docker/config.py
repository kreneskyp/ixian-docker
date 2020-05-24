# Copyright [2018-2020] Peter Krenesky
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from typing import List, Dict

from ixian.config import Config, CONFIG
from ixian.module import MODULES


class DockerConfig(Config):
    """Configuration for Docker module.

    This config class contains the building blocks for building docker images and running
    containers. This class is normally accessible from :code:`CONFIG.DOCKER`
    """

    @property
    def ROOT_MODULE_DIR(cls) -> str:
        """
        Directory where ixian.docker is installed. Use this to reference files within the python
        package when installed within your environment.
        """
        import ixian_docker

        return os.path.dirname(os.path.realpath(ixian_docker.__file__))

    @property
    def MODULE_DIR(cls) -> str:
        """
        Directory where modules.docker is installed. Use this to reference files within the docker
        module when isntalled within your environment. (e.g. to reference templates)
        """
        from ixian_docker.modules import docker

        return os.path.dirname(os.path.realpath(docker.__file__))

    #: The docker image will be tagged with this tag when built.
    #:
    #: By default, this tag uses the hash from :code:`build_image`. The hash should represent the
    #: current state and identify the image that would be built.
    IMAGE_TAG = "runtime-{TASKS.BUILD_IMAGE.HASH}"

    #: The base docker image will be tagged with this tag when built.
    #:
    #: By default, this tag uses the hash from :code:`build_base_image`. The hash should represent
    #: the current state and identify the image that would be built.
    BASE_IMAGE_TAG = "base-{TASKS.BUILD_BASE_IMAGE.HASH}"

    @property
    def VOLUMES(self) -> List[str]:
        """
        Volumes included in every environment.

        This property contains a list of docker volume mapping (host:client).
        Volumes are mounted by compose in all environments.

        This property aggregates :code:`volumes` from all modules that configure it.
        """
        volumes = []
        for module_configs in MODULES.values():
            volumes.extend(module_configs.get("volumes", []))
        return volumes

    @property
    def DEV_VOLUMES(self) -> List[str]:
        """
        Volumes included in local development environment.

        This property contains a list of docker volume mapping (host:client).
        Dev volumes are mounted by compose when doing local development. They
        are used to map in local files so that changes reflect in running
        containers immediately.

        This property aggregates dev_volumes from all configured modules.
        """
        volumes = []
        for module_configs in MODULES.values():
            volumes.extend(module_configs.get("dev_volumes", []))
        return volumes

    @property
    def ENV(self):
        """
        ENV settings included in all environments.

        This property returns a dict of ENV variables passed to compose.

        This property aggregates :code:`env` from modules that define it.
        """
        env = {}
        for module_configs in MODULES.values():
            env.update(module_configs.get("dev_environment", {}))
        return env

    @property
    def DEV_ENV(self):
        """
        ENV settings included in local development environment.

        This property returns a dict of ENV settings that are passed to compose
        when :code:`ENV == DEV`.

        This property aggregates dev_environment from all configured modules.
        This property aggregates :code:`dev_environment` from modules that define it.
        :code:`dev_environment` must be a dict.
        """
        env = {}
        for module_configs in MODULES.values():
            env.update(module_configs.get("dev_env", {}))
        return env

    # App file structure:
    #: home directory for root user
    HOME_DIR: str = "/root"

    #: root directory for apps
    ENV_DIR: str = "/opt"

    #: root directory for this app
    APP_DIR: str = "{DOCKER.ENV_DIR}/{PROJECT_NAME}"

    #: working directory for running app
    WORK_DIR: str = "{DOCKER.APP_DIR}"

    #: run scripts and other utilities for managing app.
    APP_BIN: str = "{DOCKER.APP_DIR}/bin"

    #: configuration files for app
    APP_ETC: str = "{DOCKER.APP_DIR}/etc"

    # Registry settings
    #: Registry to push/pull from
    REGISTRY: str = "docker.io"
    #: Path to images within registry.
    REGISTRY_PATH: str = "library"

    # Image tags
    #: Full URL for docker repository that store images from the build.
    REPOSITORY: str = "{DOCKER.REGISTRY}/{DOCKER.REGISTRY_PATH}/{PROJECT_NAME}"
    #: Full url and tag for docker image
    IMAGE: str = "{DOCKER.REPOSITORY}:{DOCKER.IMAGE_TAG}"
    #: Full url and tag for base docker image
    BASE_IMAGE: str = "{DOCKER.REPOSITORY}:{DOCKER.BASE_IMAGE_TAG}"

    #: Default docker-compose app to start if :code:`compose` caller does not specify one. Value
    #: must exist in the docker-compose file.
    DEFAULT_APP: str = "app"

    #: Path to Dockerfile to build with build_app
    DOCKERFILE: str = "Dockerfile"
    #: Path to Dockerfile used to build base image
    DOCKERFILE_BASE: str = "Dockerfile.base"

    #: Files needed to build the image. These images will be included in the image hash and will
    #: trigger rebuilds when changed.
    IMAGE_FILES = []
    #: Files needed to build the base image. These images will be included in the image hash and
    #: will trigger rebuilds when changed.
    BASE_IMAGE_FILES = [
        "{PWD}/root/{PROJECT_NAME}/bin/",
        "{PWD}/root/{PROJECT_NAME}/etc/base",
    ]

    # TODO: is module_context still used?
    #: Module files added to docker build context.
    MODULE_CONTEXT: str = "{BUILDER_DIR}/module_context"

    #: Image to use when running :code:`compose`
    #:
    #: This may be an image other than the runtime image. Often you'll want to skip the final build
    #: step and work with an intermediate image.
    COMPOSE_IMAGE: str = "{PYTHON.IMAGE}"

    #: Task that build the image needed for running compose
    COMPOSE_IMAGE_TASK: str = "build_python_image"

    #: Default flags passed to Compose. These flags will be passed by default to all calls to
    #: :code:`compose`. These default args are merged with args passed to the `compose` api by
    #: tasks or by the user.
    COMPOSE_FLAGS: List[str] = ["--rm", "-u root"]

    @property
    def COMPOSE_ENV(self) -> Dict[str, str]:
        """
        Environment variables passed to all calls :code:`compose`.
        """
        return {
            "DOCKER_IMAGE": CONFIG.DOCKER.COMPOSE_IMAGE,
            "DOCKER_NPM_IMAGE": CONFIG.NPM.IMAGE,
            "DOCKER_NPM_VOLUME": CONFIG.NPM.VOLUME,
        }
