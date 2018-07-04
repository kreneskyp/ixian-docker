import os

from power_shovel.config import Config
from power_shovel.utils.decorators import classproperty


class BowerConfig(Config):

    @classproperty
    def MODULE_DIR(cls):
        """Directory where shovel.webpack is installed"""
        from power_shovel_docker.modules import bower
        return os.path.dirname(os.path.realpath(bower.__file__))

    # Directory path and volume for bower_components (installed files)
    COMPONENTS_DIR = '{DOCKER.APP_DIR}/bower_components'
    COMPONENTS_VOLUME = '{PROJECT_NAME}.bower_components'

    # Config file and path
    CONFIG_FILE = 'bower.json'
    CONFIG_FILE_PATH = '{DOCKER.PROJECT_DIR}/{BOWER.CONFIG_FILE}'

    # Path to bower executable
    BIN = '{NPM.NODE_MODULES_DIR}/.bin/bower'

    # Default args included in every call to bower
    ARGS = [
        '--config.interactive=false',
        '--allow-root'
    ]

    # Path to Dockerfile template snippet.
    DOCKERFILE_TEMPLATE = '{BOWER.MODULE_DIR}/Dockerfile.template'
