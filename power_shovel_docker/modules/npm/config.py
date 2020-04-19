import os

from power_shovel.check.checker import hash_object
from power_shovel.config import Config, CONFIG
from power_shovel.modules.filesystem.file_hash import FileHash
from power_shovel.utils.decorators import classproperty


class NPMConfig(Config):
    @classproperty
    def MODULE_DIR(cls):
        """Directory where shovel.npm is installed"""
        from power_shovel_docker.modules import npm

        return os.path.dirname(os.path.realpath(npm.__file__))

    # file name for NPM config
    PACKAGE_JSON = "package.json"

    # Directory in container where node_modules is located.
    NODE_MODULES_DIR = "{DOCKER.APP_DIR}/node_modules"

    DOCKERFILE = "Dockerfile.npm"
    IMAGE_FILES = ["{PWD}/root/srv/etc/npm/"]

    REPOSITORY = "{DOCKER.REPOSITORY}"
    IMAGE_TAG = "npm-{TASKS.BUILD_NPM_IMAGE.HASH}"
    IMAGE = "{NPM.REPOSITORY}:{NPM.IMAGE_TAG}"

    VOLUME = "{NPM.IMAGE_TAG}"
