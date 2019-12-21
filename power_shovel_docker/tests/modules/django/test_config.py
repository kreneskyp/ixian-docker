import pytest

from power_shovel.config import CONFIG


EXPECTED_FIELDS = [
    "HOST",
    "MODULE_DIR",
    "PORT",
    "SETTINGS_DIR",
    "SETTINGS_MODULE",
    "SETTINGS_FILE",
    "SETTINGS_TEST",
    "UWSGI_INI",
]


class TestDjangoConfig:

    @pytest.mark.parametrize("field", EXPECTED_FIELDS)
    def test_read(self, field, mock_django_environment, snapshot):
        """
        Test reading default config values and testing property getter functions.
        """
        snapshot.assert_match({
            "field": getattr(CONFIG.DJANGO, field)
        })
