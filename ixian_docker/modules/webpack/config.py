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

from ixian.check.checker import hash_object
from ixian.config import Config, CONFIG
from ixian.modules.filesystem.file_hash import FileHash
from ixian.utils.decorators import classproperty


class WebpackConfig(Config):
    @property
    def MODULE_DIR(cls) -> str:
        """Directory where ixian_docker.webpack is installed"""
        from ixian_docker.modules import webpack

        return os.path.dirname(os.path.realpath(webpack.__file__))

    #: Directory in container where compiled files are written.
    COMPILED_STATIC_DIR = "{DOCKER.APP_DIR}/compiled_static"

    # Volumes used in development
    #: Docker volume for compiled static for use with ``compose``.
    COMPILED_STATIC_VOLUME = "{PROJECT_NAME}.compiled_static"
    #: Docker volume for webpack cache for use with ``compose``.
    CACHE_LOADER_VOLUME = "{PROJECT_NAME}.cache_loader"

    # Webpack config file and path within the container.
    #: Webpack config file
    CONFIG_FILE = "webpack.config.js"
    #: Webpack configuration directory
    CONFIG_DIR = "{DOCKER.APP_DIR}/etc/webpack"
    #: Path to webpack config file
    CONFIG_FILE_PATH = "{WEBPACK.CONFIG_DIR}/{WEBPACK.CONFIG_FILE}"

    #: Directories with sources to compile.
    SOURCE_DIRS = ["src/static"]

    #: Global arguments added to all calls to `webpack`
    ARGS = [
        "--colors",
        "--config {WEBPACK.CONFIG_FILE_PATH}",
        "--output-path {WEBPACK.COMPILED_STATIC_DIR}",
    ]

    #: Dockerfile template for building the webpack image's dockerfile
    DOCKERFILE = "{WEBPACK.MODULE_DIR}/Dockerfile.jinja"
    #: The path to the dockerfile rendered from ``WEBPACK.DOCKERFILE``
    RENDERED_DOCKERFILE = "{BUILDER}/Dockerfile.webpack"
    #: Files that are required to build this image.
    #:
    #: These files will be included in the task and image hashes, and are used to detect the need
    #: for building. This is generally the inputs to the image, and includes configuration and
    #: source files.
    IMAGE_FILES = ["{PWD}/root/srv/etc/webpack/"]
    #: Arguments passed to ``build_image``
    BUILD_ARGS = {
        "ETC": "{WEBPACK.ETC}",
        "HOST_ETC": "{WEBPACK.HOST_ETC}",
        "SRC": "{WEBPACK.SOURCE_DIRS}",
    }

    #: Repository where docker image will be stored.
    REPOSITORY = "{DOCKER.REPOSITORY}"
    #: Tag identifying the image that will be built.
    IMAGE_TAG = "webpack-{TASKS.BUILD_WEBPACK_IMAGE.HASH}"
    #: Full name of image to build. Includes repository and tag.
    IMAGE = "{WEBPACK.REPOSITORY}:{WEBPACK.IMAGE_TAG}"

    #: Path to webpack executable
    BIN = "{NPM.BIN}/webpack"

    #: Path to webpack config directory
    ETC = "{DOCKER.APP_DIR}/etc/webpack"

    #: path to webpack config directory on the host computer.
    HOST_ETC = "root{WEBPACK.ETC}"

    @property
    def RUN_CMD(self) -> str:
        """
        Shell command to run webpack
        """
        args = " \ \n  ".join(CONFIG.WEBPACK.ARGS)
        return f"{CONFIG.WEBPACK.BIN} \ \n  {args}"


WEBPACK_CONFIG = WebpackConfig()
