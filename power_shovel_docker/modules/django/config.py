import os

from power_shovel.config import Config
from power_shovel.utils.decorators import classproperty


class DjangoConfig(Config):
    @classproperty
    def MODULE_DIR(cls):
        """Directory where shovel.python is installed"""
        from power_shovel_docker.modules import django
        return os.path.dirname(os.path.realpath(django.__file__))

    DJANGO_SETTINGS_DIR = '{PYTHON.ROOT_MODULE}/settings'
    DJANGO_SETTINGS_TEST = '{PYTHON.ROOT_MODULE}/settings/test.py'


DJANGO_CONFIG = DjangoConfig()
