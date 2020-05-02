from ixian.config import Config


class JestConfig(Config):
    CONFIG_FILE = "jest.config.json"
    CONFIG_FILE_PATH = "{DOCKER.APP_ETC}/runtime/{JEST.CONFIG_FILE}"
    BIN = "{NPM.NODE_MODULES_DIR}/.bin/jest"


JEST_CONFIG = JestConfig()
