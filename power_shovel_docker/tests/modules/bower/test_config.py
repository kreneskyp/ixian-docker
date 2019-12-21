import pytest

from power_shovel.config import CONFIG


EXPECTED_FIELDS = [
    "ARGS",
    "BIN",
    "COMPONENTS_DIR",
    "CONFIG_FILE",
    "CONFIG_FILE_PATH",
    "DOCKERFILE",
    "IMAGE",
    "IMAGE_HASH",
    "IMAGE_TAG",
    "MODULE_DIR",
    "REPOSITORY",
]


class TestBowerConfig:

    @pytest.mark.parametrize("field", EXPECTED_FIELDS)
    def test_read(self, field, mock_bower_environment, snapshot):
        """
        Test reading default config values and testing property getter functions.
        """
        snapshot.assert_match(getattr(CONFIG.BOWER, field))
