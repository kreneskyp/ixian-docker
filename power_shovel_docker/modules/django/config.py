import os

from power_shovel.config import Config
from power_shovel.utils.decorators import classproperty


class DjangoConfig(Config):
    @classproperty
    def MODULE_DIR(cls):
        """Directory where shovel.python is installed"""
        from power_shovel_docker.modules import django

        return os.path.dirname(os.path.realpath(django.__file__))

    # Directory containing django settings
    SETTINGS_DIR = "{PYTHON.ROOT_MODULE}/settings"

    # Module containing settings
    SETTINGS_MODULE = "{PYTHON.ROOT_MODULE}.settings"

    # default settings
    SETTINGS_FILE = "{DJANGO.SETTINGS_MODULE}.base"

    # settings file for tests
    SETTINGS_TEST = "{DJANGO.SETTINGS_MODULE}.test"

    # Path to UWSGI configuration file on host.
    UWSGI_INI = "uwsgi.ini"

    # Host for Compose. 0.0.0.0 should be used for docker default network
    # config.
    HOST = "0.0.0.0"

    # Port to expose for both Compose and Docker run.
    PORT = "8000"


DJANGO_CONFIG = DjangoConfig()
