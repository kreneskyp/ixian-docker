import pytest
from docker import errors as docker_errors

from power_shovel.conftest import *
from power_shovel.conftest import mock_environment as base_mock_power_shovel_environment
from power_shovel_docker.modules.docker.utils.images import (
    build_image,
    delete_image,
    image_exists,
)
from power_shovel_docker.tests.mocks.client import *


TEST_IMAGE_NAME = "power_shovel_docker.test"
TEST_IMAGE_TWO_NAME = "power_shovel_docker.test.two"


# =================================================================================================
# Mock images and Docker api
# =================================================================================================


def build_test_image(
    dockerfile="Dockerfile.one",
    tag=TEST_IMAGE_NAME,
    context="/opt/power_shovel_docker/power_shovel_docker/tests/",
    **kwargs,
):
    return build_image(tag=tag, context=context, dockerfile=dockerfile, **kwargs)


def build_test_image_two(
    dockerfile="Dockerfile.two",
    tag=TEST_IMAGE_TWO_NAME,
    context="/opt/power_shovel_docker/power_shovel_docker/tests/",
    **kwargs,
):
    return build_image(tag=tag, context=context, dockerfile=dockerfile, **kwargs)


@pytest.fixture
def mock_get_image(mock_docker_environment):
    """
    Mock image TEST_IMAGE_NAME
    """
    not_found = set()

    def get_image_mock(image):
        if image in not_found:
            raise docker_errors.NotFound(image)
        image_mock = mock.Mock()
        image_mock.id = f"MOCK_ID__{image}"
        return image_mock

    get_image_mock.not_found = not_found

    mock_docker_environment.images.get.side_effect = get_image_mock
    yield mock_docker_environment


@pytest.fixture
def mock_image_exists():
    patcher = mock.patch("power_shovel_docker.modules.docker.utils.images.image_exists")
    mocked = patcher.start()
    mocked.return_value = False
    yield mocked
    mocked.stop()


@pytest.fixture
def mock_image_exists_in_registry():
    patcher = mock.patch(
        "power_shovel_docker.modules.docker.utils.images.image_exists_in_registry"
    )
    mocked = patcher.start()
    mocked.return_value = False
    yield mocked
    mocked.stop()


@pytest.fixture
def mock_pull_image():
    patcher = mock.patch("power_shovel_docker.modules.docker.utils.images.pull_image")
    mocked = patcher.start()
    mocked.return_value = False
    yield mocked
    mocked.stop()


@pytest.fixture
def test_image():
    """
    Sets up a real docker image by building it.
    """
    yield build_test_image()
    delete_image(TEST_IMAGE_NAME, force=True)


@pytest.fixture
def test_image_two():
    """
    Sets up a real docker image by building it.
    """
    yield build_test_image_two()
    delete_image(TEST_IMAGE_TWO_NAME, force=True)


# =================================================================================================
# Mock module environments
# =================================================================================================


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
