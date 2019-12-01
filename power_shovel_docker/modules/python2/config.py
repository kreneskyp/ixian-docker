import os

from power_shovel.config import Config
from power_shovel.utils.decorators import classproperty


class PythonConfig(Config):
    @classproperty
    def MODULE_DIR(cls):
        """Directory where shovel.python is installed"""
        from power_shovel_docker.modules import python2

        return os.path.dirname(os.path.realpath(python2.__file__))

    # Runtime
    VIRTUAL_ENV = ".venv"
    VIRTUAL_ENV_DIR = "{DOCKER.APP_DIR}/.venv"
    VIRTUAL_ENV_RUN = "{PYTHON.BIN}"
    ROOT_MODULE = "{PROJECT_NAME}"
    ROOT_MODULE_PATH = "{DOCKER.APP_DIR}/{PYTHON.ROOT_MODULE}"
    HOST_ROOT_MODULE_PATH = "{PWD}/{PYTHON.ROOT_MODULE}"
    BIN = "python"

    PIPFILE = "Pipfile"

    # Docker
    VIRTUAL_ENV_VOLUME = "{PROJECT_NAME}.venv"
