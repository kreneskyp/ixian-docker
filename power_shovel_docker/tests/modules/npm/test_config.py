import pytest

from power_shovel.config import CONFIG


EXPECTED_FIELDS = [
    "DOCKERFILE",
    "DOCKERFILE_TEMPLATE",
    "IMAGE",
    "IMAGE_TAG",
    "MODULE_DIR",
    "NODE_MODULES_DIR",
    "PACKAGE_JSON",
    "REPOSITORY",
]


class TestNPMConfig:
    @pytest.mark.parametrize("field", EXPECTED_FIELDS)
    def test_read(self, field, mock_bower_environment, snapshot):
        """
        Test reading default config values and testing property getter functions.
        """
        snapshot.assert_match(getattr(CONFIG.NPM, field))

    def test_task_hash(self, mock_environment, snapshot):
        snapshot.assert_match(CONFIG.TASKS.BUILD_NPM_IMAGE)