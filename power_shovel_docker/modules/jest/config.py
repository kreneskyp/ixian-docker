from power_shovel.config import Config


class JestConfig(Config):
    CONFIG_FILE = "jest.config.json"
    CONFIG_FILE_PATH = "{DOCKER.PROJECT_DIR}/{JEST.CONFIG_FILE}"
    BIN = "{NPM.NODE_MODULES_DIR}/.bin/jest"


JEST_CONFIG = JestConfig()
