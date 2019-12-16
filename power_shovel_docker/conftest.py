import pytest
from power_shovel.conftest import *
from power_shovel_docker.modules.docker.utils.images import build_image
from power_shovel_docker.tests.mocks.client import *


TEST_IMAGE_NAME = "power_shovel_docker.scratch"


@pytest.fixture
def test_image(mock_docker_environment):
    build_image(
        TEST_IMAGE_NAME,
        file="/opt/power_shovel_docker/power_shovel_docker/tests/Dockerfile.scratch",
    )
    yield
