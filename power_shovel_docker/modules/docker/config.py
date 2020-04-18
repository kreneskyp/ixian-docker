import os

from power_shovel.check.checker import hash_object
from power_shovel.config import Config, CONFIG
from power_shovel.module import MODULES
from power_shovel.modules.filesystem.file_hash import FileHash
from power_shovel.utils.decorators import classproperty


class DockerConfig(Config):
    """Configuration for Docker module."""

    @classproperty
    def ROOT_MODULE_DIR(cls):
        """Directory where power_shovel.docker is installed"""
        import power_shovel_docker

        return os.path.dirname(os.path.realpath(power_shovel_docker.__file__))

    @classproperty
    def MODULE_DIR(cls):
        """Directory where modules.docker is installed"""
        from power_shovel_docker.modules import docker

        return os.path.dirname(os.path.realpath(docker.__file__))

    IMAGE_TAG = "runtime-{TASKS.BUILD_IMAGE.HASH}"
    BASE_IMAGE_TAG = "base-{TASKS.BUILD_BASE_IMAGE.HASH}"

    # TODO: is this still needed since we're moving away from volumes
    @classproperty
    def VOLUMES(self):
        """Volumes included in every environment.

        This property contains a list of docker volume mapping (host:client).
        Volumes are mounted by compose in all environments.

        This property aggregates volumes from all configured modules.
        """
        volumes = []
        for module_configs in MODULES.values():
            volumes.extend(module_configs.get("volumes", []))
        return volumes

    @classproperty
    def DEV_VOLUMES(self):
        """Volumes included in local development environment.

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

    @classproperty
    def ENV(self):
        """ENV settings included in all environments.

        This property returns a dict of ENV variables passed to compose.

        This property aggregates `env` from all configured modules.
        """
        env = {}
        for module_configs in MODULES.values():
            env.update(module_configs.get("dev_environment", {}))
        return env

    @classproperty
    def DEV_ENV(self):
        """ENV settings included in local development environment.

        This property returns a dict of ENV settings that are passed to compose
        when ENV == DEV.

        This property aggregates dev_environment from all configured modules.
        """
        env = {}
        for module_configs in MODULES.values():
            env.update(module_configs.get("dev_env", {}))
        return env

    # App file structure:
    #  - HOME_DIR: home directory for root user
    #  - ENV_DIR: root directory for apps
    #  - APP_DIR: root directory for the app
    #  - APP_BIN: run scripts and other utilities for managing app.
    #  - PROJECT_DIR: root dir for project.
    HOME_DIR = "/root"
    ENV_DIR = "/srv"
    APP_DIR = "{DOCKER.ENV_DIR}/{PROJECT_NAME}"
    APP_BIN = "{DOCKER.APP_DIR}/bin"
    APP_ETC = "{DOCKER.APP_DIR}/etc"
    PROJECT_DIR = "{DOCKER.APP_DIR}/project"

    # Registry settings
    REGISTRY = "docker.io"
    REGISTRY_PATH = "library"

    # Image tags
    REPOSITORY = "{DOCKER.REGISTRY}/{DOCKER.REGISTRY_PATH}/{PROJECT_NAME}"
    IMAGE = "{DOCKER.REPOSITORY}:{DOCKER.IMAGE_TAG}"
    IMAGE_FULL = "{DOCKER.REPOSITORY}:{DOCKER.IMAGE_TAG}"
    BASE_IMAGE = "{DOCKER.REPOSITORY}:{DOCKER.BASE_IMAGE_TAG}"

    # Default app in docker-compose file
    DEFAULT_APP = "app"

    # Name of Dockerfile to build with build_app
    DOCKERFILE = "Dockerfile"
    DOCKERFILE_BASE = "Dockerfile.base"

    # Files needed for build
    IMAGE_FILES = []
    BASE_IMAGE_FILES = [
        '{PWD}/root/{PROJECT_NAME}/bin/'
        '{PWD}/root/{PROJECT_NAME}/etc/base'
    ]

    # Module files added to docker build context.
    MODULE_CONTEXT = "{BUILDER_DIR}/module_context"

    COMPOSE_IMAGE = "{PYTHON.IMAGE}"
    COMPOSE_IMAGE_TASK = "build_python_image"

    # Default flags passed to Compose
    COMPOSE_FLAGS = ["--rm", "-u root"]

    @classproperty
    def COMPOSE_ENV(self):
        """Environment variables set when running compose."""
        return {
            "DOCKER_IMAGE": CONFIG.DOCKER.COMPOSE_IMAGE,
            "DOCKER_NPM_IMAGE": CONFIG.NPM.IMAGE,
            "DOCKER_NPM_VOLUME": CONFIG.NPM.VOLUME
        }
