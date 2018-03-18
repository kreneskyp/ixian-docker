import os

from power_shovel.config import Config
from power_shovel.utils.decorators import classproperty


class WebpackConfig(Config):

    @classproperty
    def MODULE(cls):
        """Directory where shovel.webpack is installed"""
        from power_shovel_docker.modules import webpack
        return os.path.dirname(os.path.realpath(webpack.__file__))

    BUILDER_TAG = 'builder.webpack'
    IMAGE_TAG = '{PROJECT_NAME}.webpack'
    COMPILED_STATIC_DIR = '{DOCKER.APP_DIR}/compiled_static'
    BUILDER_CONTEXT = '{WEBPACK.MODULE}'
    BUILDER_DOCKERFILE = '{WEBPACK.BUILDER_CONTEXT}/Dockerfile'
    CONFIG_FILE = 'webpack.config.js'
    CONFIG_FILE_PATH = '{DOCKER.PROJECT_DIR}/{WEBPACK.CONFIG_FILE}'

WEBPACK_CONFIG = WebpackConfig()
