import os

from power_shovel.config import Config
from power_shovel.utils.decorators import classproperty


class PythonConfig(Config):
    @classproperty
    def MODULE(cls):
        """Directory where shovel.python is installed"""
        from power_shovel.modules import python
        return os.path.dirname(os.path.realpath(python.__file__))

    # Runtime
    VIRTUAL_ENV_DIR = 'venv'
    VIRTUAL_ENV_RUN = '{PYTHON.BIN}'
    VIRTUAL_ENV_PATH = '{BUILDER}/{PYTHON.VIRTUAL_ENV_DIR}'
    ROOT_MODULE = '{PROJECT_NAME}'
    ROOT_MODULE_PATH = '{DOCKER.APP_DIR}/{PYTHON.ROOT_MODULE}'
    HOST_ROOT_MODULE_PATH = '{PWD}/{PYTHON.ROOT_MODULE}'
    BIN = 'python3'

    # Docker / Builder
    BUILDER_TAG = 'builder.python'
    BUILDER_CONTEXT = '{PYTHON.MODULE}'
    BUILDER_DOCKERFILE = '{PYTHON.BUILDER_CONTEXT}/Dockerfile'
    IMAGE_TAG = '{PROJECT_NAME}.python'

    # TODO i think pipenv handles this automagically now
    WHEELHOUSE_DIR = 'wheelhouse'
