import os

from power_shovel.config import Config
from power_shovel.utils.decorators import classproperty


class WebpackConfig(Config):

    @classproperty
    def MODULE_DIR(cls):
        """Directory where shovel.webpack is installed"""
        from power_shovel_docker.modules import webpack
        return os.path.dirname(os.path.realpath(webpack.__file__))

    COMPILED_STATIC_DIR = '{DOCKER.APP_DIR}/compiled_static'
    CONFIG_FILE = 'webpack.config.js'
    CONFIG_FILE_PATH = '{DOCKER.PROJECT_DIR}/{WEBPACK.CONFIG_FILE}'

    DOCKER_CONTEXT = '{WEBPACK.MODULE_DIR}/context'
    COMPILED_STATIC_VOLUME = '{PROJECT_NAME}.compiled_static'

WEBPACK_CONFIG = WebpackConfig()
