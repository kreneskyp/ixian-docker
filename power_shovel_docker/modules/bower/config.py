import os

from power_shovel.config import Config
from power_shovel.utils.decorators import classproperty


class BowerConfig(Config):

    @classproperty
    def MODULE_DIR(cls):
        """Directory where shovel.webpack is installed"""
        from power_shovel_docker.modules import bower
        return os.path.dirname(os.path.realpath(bower.__file__))

    COMPONENTS_VOLUME = '{PROJECT_NAME}.bower_components'
    COMPONENTS_DIR = '{DOCKER.APP_DIR}/bower_components'
    CONFIG_FILE = 'bower.json'
    CONFIG_FILE_PATH = '{DOCKER.PROJECT_DIR}/{BOWER.CONFIG_FILE}'
    BIN = '{NPM.NODE_MODULES_DIR}/.bin/bower'
    DOCKER_CONTEXT = '{BOWER.MODULE_DIR}/context'
