import os

from ixian.check.checker import hash_object
from ixian.config import Config, CONFIG
from ixian.modules.filesystem.file_hash import FileHash
from ixian.utils.decorators import classproperty


class BowerConfig(Config):
    @classproperty
    def MODULE_DIR(cls):
        """Directory where ixian_docker.webpack is installed"""
        from ixian_docker.modules import bower

        return os.path.dirname(os.path.realpath(bower.__file__))

    # Directory path and volume for bower_components (installed files)
    COMPONENTS_DIR = "{DOCKER.APP_DIR}/bower_components"
    COMPONENTS_VOLUME = "{PROJECT_NAME}.bower_components"

    # Config file and path
    CONFIG_FILE = "bower.json"
    CONFIG_FILE_PATH = "{DOCKER.PROJECT_DIR}/{BOWER.CONFIG_FILE}"

    # Path to bower executable
    BIN = "{NPM.NODE_MODULES_DIR}/.bin/bower"

    # Default args included in every call to bower
    ARGS = ["--config.interactive=false", "--allow-root"]

    DOCKERFILE = "Dockerfile.bower"
    IMAGE_FILES = ["{PWD}/root/srv/etc/bower/"]

    REPOSITORY = "{DOCKER.REPOSITORY}"
    IMAGE_TAG = "bower-{TASKS.BUILD_BOWER_IMAGE.HASH}"
    IMAGE = "{BOWER.REPOSITORY}:{BOWER.IMAGE_TAG}"
