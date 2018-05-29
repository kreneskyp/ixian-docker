import os
from power_shovel.config import Config
from power_shovel.module import MODULES
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

    # TODO: is this still needed since we're moving away from volumes
    @classproperty
    def VOLUMES(self):
        """Volumes included in every environment.

        This property contains a list of docker volume mapping (host:client).
        Volumes are mounted by compose in all environments.

        This property aggregates volumes from all configured modules.
        """
        volumes = []
        for module_configs in MODULES:
            volumes.extend(module_configs.get('volumes', []))
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
        for module_configs in MODULES:
            volumes.extend(module_configs.get('dev_volumes', []))
        return volumes

    @classproperty
    def ENV(self):
        """ENV settings included in all environments.

        This property returns a dict of ENV variables passed to compose.

        This property aggregates `env` from all configured modules.
        """
        env = {}
        for module_configs in MODULES:
            env.update(module_configs.get('dev_environment', {}))
        return env

    @classproperty
    def DEV_ENV(self):
        """ENV settings included in local development environment.

        This property returns a dict of ENV settings that are passed to compose
        when ENV == DEV.

        This property aggregates dev_environment from all configured modules.
        """
        env = {}
        for module_configs in MODULES:
            env.update(module_configs.get('dev_env', {}))
        return env

    # App file structure:
    #  - HOME_DIR: home directory for root user
    #  - ENV_DIR: root directory for apps
    #  - APP_DIR: root directory for the app
    #  - APP_BIN: run scripts and other utilities for managing app.
    #  - PROJECT_DIR: root dir for project.
    HOME_DIR = '/root'
    ENV_DIR = '/srv'
    APP_DIR = '{DOCKER.ENV_DIR}/{PROJECT_NAME}'
    APP_BIN = '{DOCKER.APP_DIR}/bin'
    PROJECT_DIR = '{DOCKER.APP_DIR}/project'

    # Name of Dockerfile to build with build_app
    DOCKER_FILE = 'Dockerfile'

    # Template is used for compiling the Dockerfile.
    DOCKERFILE_TEMPLATE = '{DOCKER.MODULE_DIR}/Dockerfile.template'

    # Modules contributed files to add to docker build context.
    MODULE_CONTEXT = '{BUILDER_DIR}/module_context'
