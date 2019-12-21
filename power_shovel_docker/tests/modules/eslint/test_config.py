import pytest

from power_shovel.config import CONFIG


EXPECTED_FIELDS = [
    "BIN",
]


class TestESLintConfig:

    @pytest.mark.parametrize("field", EXPECTED_FIELDS)
    def test_read(self, field, mock_eslint_environment, snapshot):
        """
        Test reading default config values and testing property getter functions.
        """
        snapshot.assert_match(getattr(CONFIG.ESLINT, field))
