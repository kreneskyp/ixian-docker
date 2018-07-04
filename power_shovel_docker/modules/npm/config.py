import os

from power_shovel.config import Config
from power_shovel.utils.decorators import classproperty


class NPMConfig(Config):

    @classproperty
    def MODULE_DIR(cls):
        """Directory where shovel.npm is installed"""
        from power_shovel_docker.modules import npm
        return os.path.dirname(os.path.realpath(npm.__file__))

    # file name for NPM config
    PACKAGE_JSON = 'package.json'

    # Directory in container where node_modules is located.
    NODE_MODULES_DIR = '{DOCKER.APP_DIR}/node_modules'

    # Tag for docker volume containing node_modules.
    NODE_MODULES_VOLUME = '{PROJECT_NAME}.node_modules'

    # Dockerfile template for NPM support. This snippet is rendered with the
    # base dockerfile template to create a single combined docker image.
    DOCKERFILE_TEMPLATE = '{NPM.MODULE_DIR}/Dockerfile.template'
