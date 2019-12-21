import pytest

from power_shovel.config import CONFIG



EXPECTED_FIELDS = [
    "APP_BIN",
    "APP_DIR",
    "APP_IMAGE",
    "APP_IMAGE_FULL",
    "BASE_IMAGE",
    "BASE_IMAGE_FILES",
    "BASE_IMAGE_HASH",
    "BASE_IMAGE_TAG",
    "COMPOSE_FLAGS",
    "DEFAULT_APP",
    "DEV_VOLUMES",
    "DEV_ENV",
    "DOCKERFILE",
    "DOCKERFILE_BASE",
    "DOCKERFILE_TEMPLATE",
    "ENV",
    "ENV_DIR",
    "HOME_DIR",
    "IMAGE_HASH",
    "IMAGE_TAG",
    "MODULE_CONTEXT",
    "MODULE_DIR",
    "PROJECT_DIR",
    "REGISTRY",
    "REGISTRY_PATH",
    "REPOSITORY",
    "ROOT_MODULE_DIR",
    "VOLUMES",
]


class TestDockerConfig:

    @pytest.mark.parametrize("field", EXPECTED_FIELDS)
    def test_read(self, field, mock_environment, snapshot):
        """
        Test reading default config values and testing property getter functions.
        """
        snapshot.assert_match(getattr(CONFIG.DOCKER, field))
