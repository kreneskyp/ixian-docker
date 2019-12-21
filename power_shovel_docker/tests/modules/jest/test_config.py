import pytest

from power_shovel.config import CONFIG


EXPECTED_FIELDS = [
    "BIN",
    "CONFIG_FILE",
    "CONFIG_FILE_PATH",
]


class TestJestConfig:

    @pytest.mark.parametrize("field", EXPECTED_FIELDS)
    def test_read(self, field, mock_jest_environment, snapshot):
        """
        Test reading default config values and testing property getter functions.
        """
        snapshot.assert_match({getattr(CONFIG.JEST, field)})
