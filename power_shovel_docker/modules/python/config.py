import os

from power_shovel.check.checker import hash_object
from power_shovel.config import Config, CONFIG
from power_shovel.modules.filesystem.file_hash import FileHash
from power_shovel.utils.decorators import classproperty


class PythonConfig(Config):
    @classproperty
    def MODULE_DIR(cls):
        """Directory where shovel.python is installed"""
        from power_shovel_docker.modules import python

        return os.path.dirname(os.path.realpath(python.__file__))

    # Runtime
    VIRTUAL_ENV = ".venv"
    VIRTUAL_ENV_DIR = "{DOCKER.APP_DIR}/.venv"
    VIRTUAL_ENV_RUN = "{PYTHON.BIN}"
    ROOT_MODULE = "{PROJECT_NAME}"
    ROOT_MODULE_PATH = "{DOCKER.PROJECT_DIR}/{PYTHON.ROOT_MODULE}"
    HOST_ROOT_MODULE_PATH = "{PWD}/{PYTHON.ROOT_MODULE}"
    BIN = "python3"

    DOCKERFILE = "Dockerfile.python"
    IMAGE_FILES = [
        "{PWD}/root/srv/etc/python/"
    ]

    REPOSITORY = "{DOCKER.REPOSITORY}"
    IMAGE_TAG = "python-{TASKS.BUILD_PYTHON_IMAGE.HASH}"
    IMAGE = "{PYTHON.REPOSITORY}:{PYTHON.IMAGE_TAG}"
