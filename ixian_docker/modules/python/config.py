import os

from ixian.check.checker import hash_object
from ixian.config import Config, CONFIG
from ixian.modules.filesystem.file_hash import FileHash
from ixian.utils.decorators import classproperty


class PythonConfig(Config):
    @classproperty
    def MODULE_DIR(cls):
        """Directory where ixian_docker.python is installed"""
        from ixian_docker.modules import python

        return os.path.dirname(os.path.realpath(python.__file__))

    # Runtime
    VERSION = "3.8.0"
    VIRTUAL_ENV = ".venv"
    VIRTUAL_ENV_DIR = "{DOCKER.APP_DIR}/.venv"
    VIRTUAL_ENV_RUN = "{PYTHON.BIN}"
    ROOT_MODULE = "{PROJECT_NAME}"
    ROOT_MODULE_PATH = "{DOCKER.APP_DIR}/src/{PYTHON.ROOT_MODULE}"
    HOST_ROOT_MODULE_PATH = "{PWD}/{PYTHON.ROOT_MODULE}"
    BIN = "python3"
    ETC = "{DOCKER.APP_ETC}/python"

    DOCKERFILE = "Dockerfile.python"
    IMAGE_FILES = ["{PYTHON.ETC}/"]
    REQUIREMENTS_FILES = ["{PYTHON.ETC}/requirements.txt"]

    REPOSITORY = "{DOCKER.REPOSITORY}"
    IMAGE_TAG = "python-{TASKS.BUILD_PYTHON_IMAGE.HASH}"
    IMAGE = "{PYTHON.REPOSITORY}:{PYTHON.IMAGE_TAG}"

    APT_PACKAGES = [
        'make',
        'build-essential',
        'libssl-dev',
        'zlib1g-dev',
        'libbz2-dev',
        'libreadline-dev',
        'libsqlite3-dev',
        'wget',
        'curl',
        'llvm',
        'libncurses5-dev',
        'libncursesw5-dev',
        'xz-utils',
        'tk-dev',
        'libffi-dev',
        'liblzma-dev',
    ]