import os

from power_shovel.config import Config
from power_shovel.utils.decorators import classproperty


class BowerConfig(Config):

    @classproperty
    def MODULE(cls):
        """Directory where shovel.webpack is installed"""
        from power_shovel_docker.modules import bower
        return os.path.dirname(os.path.realpath(bower.__file__))

    BUILDER_TAG = 'builder.bower'
    IMAGE_TAG = '{PROJECT_NAME}.bower'
    COMPONENTS_DIR = '{DOCKER.APP_DIR}/bower_components'
    BUILDER_CONTEXT = '{BOWER.MODULE}'
    BUILDER_DOCKERFILE = '{BOWER.BUILDER_CONTEXT}/Dockerfile'
    CONFIG_FILE = 'bower.json'
    CONFIG_FILE_PATH = '{DOCKER.PROJECT_DIR}/{BOWER.CONFIG_FILE}'
