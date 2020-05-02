from ixian.config import Config


class PrettierConfig(Config):
    SRC = "/srv/wet_arms/src/static"
    BIN = "{NPM.NODE_MODULES_DIR}/.bin/prettier"


PRETTIER_CONFIG = PrettierConfig()
