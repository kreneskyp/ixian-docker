from power_shovel.config import Config


class DjangoConfig(Config):
    DJANGO_SETTINGS_DIR = '{PYTHON.ROOT_MODULE}/settings'
    DJANGO_SETTINGS_TEST = '{PYTHON.ROOT_MODULE}/settings/test.py'


DJANGO_CONFIG = DjangoConfig()
