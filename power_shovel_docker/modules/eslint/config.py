from power_shovel.config import Config


class ESLintConfig(Config):
    BIN = '{DOCKER.APP_DIR}/node_modules/.bin/eslint'


ESLINT_CONFIG = ESLintConfig()
