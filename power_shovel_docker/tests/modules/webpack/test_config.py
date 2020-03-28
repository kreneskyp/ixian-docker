import pytest

from power_shovel.config import CONFIG


EXPECTED_FIELDS = [
    "ARGS",
    "COMPILED_STATIC_DIR",
    "CONFIG_FILE",
    "CONFIG_FILE_PATH",
    "DOCKERFILE",
    "IMAGE",
    "IMAGE_TAG",
    "MODULE_DIR",
    "REPOSITORY",
    "SOURCE_DIRS",
]


class TestConfig:
    @pytest.mark.parametrize("field", EXPECTED_FIELDS)
    def test_read(self, field, mock_webpack_environment, snapshot):
        """
        Test reading default config values and testing property getter functions.
        """
        snapshot.assert_match(getattr(CONFIG.WEBPACK, field))

    def test_task_hash(self, mock_environment, snapshot):
        snapshot.assert_match(CONFIG.TASKS.BUILD_WEBPACK_IMAGE)