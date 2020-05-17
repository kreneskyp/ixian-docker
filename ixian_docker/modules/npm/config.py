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
from typing import List

from ixian.check.checker import hash_object
from ixian.config import Config, CONFIG
from ixian.modules.filesystem.file_hash import FileHash
from ixian.utils.decorators import classproperty


class NPMConfig(Config):
    @property
    def MODULE_DIR(cls) -> str:
        """Directory where ``ixian_docker.modules.npm`` is installed"""
        from ixian_docker.modules import npm

        return os.path.dirname(os.path.realpath(npm.__file__))

    #: file name for NPM config
    PACKAGE_JSON: str = "package.json"

    #: Path to node_modules within image.
    NODE_MODULES_DIR: str = "{DOCKER.APP_DIR}/node_modules"

    #: Path to binaries installed by npm and npm packages
    BIN: str = "{NPM.NODE_MODULES_DIR}/.bin"

    #: Dockerfile for building NPM intermediate image
    DOCKERFILE: str = "{NPM.MODULE_DIR}/Dockerfile"

    #: Files that are required to build this image.
    #:
    #: These files will be included in the task and image hashes, and are used to detect the need
    #: for building.
    IMAGE_FILES: List[str] = ["{PWD}/root/srv/etc/npm/"]

    #: Repository to store docker image in
    REPOSITORY: str = "{DOCKER.REPOSITORY}"

    #: Tag for npm intermediate image.
    IMAGE_TAG: str = "npm-{TASKS.BUILD_NPM_IMAGE.HASH}"

    #: Full path to npm intermediate image including repository and tag.
    IMAGE: str = "{NPM.REPOSITORY}:{NPM.IMAGE_TAG}"

    #: Identifier for NPM Volume used by ``compose``
    VOLUME: str = "{NPM.IMAGE_TAG}"
