import os

from power_shovel.check.checker import hash_object
from power_shovel.config import Config, CONFIG
from power_shovel.modules.filesystem.file_hash import FileHash
from power_shovel.utils.decorators import classproperty


class WebpackConfig(Config):
    @classproperty
    def MODULE_DIR(cls):
        """Directory where shovel.webpack is installed"""
        from power_shovel_docker.modules import webpack

        return os.path.dirname(os.path.realpath(webpack.__file__))

    # Directory in container where compiled files are written.
    COMPILED_STATIC_DIR = "{DOCKER.APP_DIR}/compiled_static"

    # Webpack config file and path within the container.
    CONFIG_FILE = "webpack.config.js"
    CONFIG_FILE_PATH = "{DOCKER.PROJECT_DIR}/{WEBPACK.CONFIG_FILE}"

    # Directories with sources to compile.
    SOURCE_DIRS = ["static"]

    # Base arguments added to all calls to `webpack`
    ARGS = [
        "--progress",
        "--colors",
        "--config {WEBPACK.CONFIG_FILE_PATH}",
        "--output-path {WEBPACK.COMPILED_STATIC_DIR}",
    ]

    DOCKERFILE = "Dockerfile.webpack"

    @classproperty
    def IMAGE_HASH(cls):
        return hash_object(
            [
                CONFIG.NPM.IMAGE_HASH,
                FileHash("{WEBPACK.DOCKERFILE}", "{WEBPACK.CONFIG_FILE}").state(),
            ]
        )

    REPOSITORY = "{DOCKER.REPOSITORY}"
    IMAGE_TAG = "webpack-{WEBPACK.IMAGE_HASH}"
    IMAGE = "{WEBPACK.REPOSITORY}:{WEBPACK.IMAGE_TAG}"


WEBPACK_CONFIG = WebpackConfig()
