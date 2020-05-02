from ixian.config import Config


class PytestConfig(Config):
    SRC = "{PYTHON.ROOT_MODULE_PATH}"
    CACHE_DIR = "{DOCKER.APP_DIR}/.pytest_cache"
    INI_FILE = "{DOCKER.APP_ETC}/runtime/pytest.ini"
    ARGS = [
        "-c {PYTEST.INI_FILE}",
        "-o cache_dir={PYTEST.CACHE_DIR}",
    ]
    SPLIT = 3


PYTEST_CONFIG = PytestConfig()
