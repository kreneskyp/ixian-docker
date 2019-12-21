import pytest
from power_shovel.conftest import *
from power_shovel.conftest import mock_environment as base_mock_power_shovel_environment
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


@pytest.fixture
def mock_environment(base_mock_power_shovel_environment):
    load_module("power_shovel_docker.modules.docker")
    yield base_mock_power_shovel_environment


@pytest.fixture
def mock_npm_environment(mock_environment):
    load_module("power_shovel_docker.modules.npm")
    yield mock_environment


@pytest.fixture
def mock_bower_environment(mock_npm_environment):
    load_module("power_shovel_docker.modules.bower")
    yield mock_npm_environment


@pytest.fixture
def mock_jest_environment(mock_npm_environment):
    load_module("power_shovel_docker.modules.jest")
    yield mock_npm_environment


@pytest.fixture
def mock_eslint_environment(mock_npm_environment):
    load_module("power_shovel_docker.modules.eslint")
    yield mock_npm_environment


@pytest.fixture
def mock_webpack_environment(mock_npm_environment):
    load_module("power_shovel_docker.modules.webpack")
    yield mock_npm_environment


@pytest.fixture
def mock_python_environment(mock_environment):
    load_module("power_shovel_docker.modules.python")
    yield mock_environment


@pytest.fixture
def mock_django_environment(mock_python_environment):
    load_module("power_shovel_docker.modules.django")
    yield mock_python_environment