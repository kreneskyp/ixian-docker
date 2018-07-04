import os

from power_shovel.config import Config
from power_shovel.utils.decorators import classproperty


class WebpackConfig(Config):

    @classproperty
    def MODULE_DIR(cls):
        """Directory where shovel.webpack is installed"""
        from power_shovel_docker.modules import webpack
        return os.path.dirname(os.path.realpath(webpack.__file__))

    # Directory in container where compiled files are written.
    COMPILED_STATIC_DIR = '{DOCKER.APP_DIR}/compiled_static'

    # Tag for docker volume containing compiled output.
    COMPILED_STATIC_VOLUME = '{PROJECT_NAME}.compiled_static'

    # Webpack config file and path within the container.
    CONFIG_FILE = 'webpack.config.js'
    CONFIG_FILE_PATH = '{DOCKER.PROJECT_DIR}/{WEBPACK.CONFIG_FILE}'

    # Directories with sources to compile.
    SOURCE_DIRS = [
        'static'
    ]

    # Context to add to Docker build.
    DOCKER_CONTEXT = '{WEBPACK.MODULE_DIR}/context'

    # Base arguments added to all calls to `webpack`
    ARGS = [
        '--progress',
        '--colors',
        '--config {WEBPACK.CONFIG_FILE_PATH}',
        '--output-path {WEBPACK.COMPILED_STATIC_DIR}'
    ]


WEBPACK_CONFIG = WebpackConfig()
