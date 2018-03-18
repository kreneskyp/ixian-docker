import os

from power_shovel.config import Config
from power_shovel.utils.decorators import classproperty


class NPMConfig(Config):

    @classproperty
    def MODULE_DIR(cls):
        """Directory where shovel.npm is installed"""
        from power_shovel_docker.modules import npm
        return os.path.dirname(os.path.realpath(npm.__file__))

    NODE_MODULES_DIR = '{DOCKER.APP_DIR}/node_modules'
    PACKAGE_JSON = 'package.json'
    BUILDER_TAG = 'builder.npm'
    IMAGE_TAG = '{PROJECT_NAME}.npm'
    BUILDER_CONTEXT = '{NPM.MODULE_DIR}'
    BUILDER_DOCKERFILE = '{NPM.BUILDER_CONTEXT}/Dockerfile'
