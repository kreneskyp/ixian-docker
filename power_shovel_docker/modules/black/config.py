from power_shovel.config import Config


class BlackConfig(Config):
    CONFIG = "{DOCKER.APP_DIR}/etc/runtime/pyproject.toml"
    SRC = "{PYTHON.ROOT_MODULE_PATH}"
    ARGS = [
        "--config {BLACK.CONFIG}",
        "{BLACK.SRC}"
    ]

BLACK_CONFIG = BlackConfig()
