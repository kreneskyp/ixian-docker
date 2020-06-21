# Copyright [2018-2020] Peter Krenesky
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import logging
import os

import pytest
from docker import errors as docker_errors

from ixian_docker.modules.docker.utils.images import (
    delete_image,
    image_exists,
)
from ixian_docker.tests.mocks.client import *
from ixian.tests.conftest import mock_environment as base_mock_ixian_environment
from ixian.tests.conftest import mock_cli, mock_init


TEST_IMAGE_NAME = "ixian_docker.tests"
TEST_IMAGE_TWO_NAME = "ixian_docker.tests.two"


def get_tests_dir():
    """
    Get the absolute path to the tests directory
    """
    from ixian_docker import tests

    return os.path.dirname(os.path.realpath(tests.__file__))


# =================================================================================================
# Mock images and Docker api
# =================================================================================================


def build_test_image(
    dockerfile="Dockerfile.one", tag=TEST_IMAGE_NAME, context=None, **kwargs,
):
    if context is None:
        context = get_tests_dir()

    return build_image(tag=tag, context=context, dockerfile=dockerfile, **kwargs)


def build_test_image_two(
    dockerfile="Dockerfile.two", tag=TEST_IMAGE_TWO_NAME, context=None, **kwargs,
):
    if context is None:
        context = get_tests_dir()

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
    patcher = mock.patch("ixian_docker.modules.docker.utils.images.image_exists")
    mocked = patcher.start()
    mocked.return_value = False
    yield mocked
    patcher.stop()


@pytest.fixture
def mock_image_exists_in_registry():
    patcher = mock.patch("ixian_docker.modules.docker.utils.images.image_exists_in_registry")
    mocked = patcher.start()
    mocked.return_value = False
    yield mocked
    patcher.stop()


@pytest.fixture
def mock_pull_image():
    patcher = mock.patch("ixian_docker.modules.docker.utils.images.pull_image")
    mocked = patcher.start()
    mocked.return_value = False
    yield mocked
    patcher.stop()


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


@pytest.fixture
def mock_build_image_if_needed(
    mock_image_exists, mock_image_exists_in_registry, mock_pull_image, capsys, snapshot, caplog
):
    """
    Mock ``build_image_if_needed`` with various options
    """
    caplog.set_level(logging.DEBUG, logger="ixian_docker.modules.docker")

    def setup(scenario="image_does_not_exist"):
        mock_image_exists.return_value = False
        mock_image_exists_in_registry.return_value = False
        mock_pull_image.side_effect = None

        if scenario == "image_exists_local":
            mock_image_exists.return_value = True
            mock_image_exists_in_registry.return_value = False
        if scenario == "image_exists":
            mock_image_exists.return_value = True
            mock_image_exists_in_registry.return_value = True
        elif scenario == "image_does_not_exist":
            pass
        elif scenario == "pull_image":
            mock_image_exists_in_registry.return_value = True
        elif scenario == "pull_image_not_found":
            mock_image_exists_in_registry.return_value = True
            mock_pull_image.side_effect = docker_errors.NotFound("testing")
        elif scenario == "pull_unknown_registry":
            raise NotImplementedError

    def assert_build(image: str, builds: bool = True, scenario: str = "image_does_not_exist"):
        from ixian.runner import run

        setup(scenario)
        image_will_be_built = scenario in {
            "image_does_not_exist",
            "pull_image_not_found",
        }

        assert not image_exists(image)
        try:
            run()
        except:
            raise
        else:
            if image_will_be_built and builds:
                assert image_exists(image)
            else:
                assert not image_exists(image)
        finally:
            if image_will_be_built:
                delete_image(image)
        assert not image_exists(image)

        out, err = capsys.readouterr()

        # process log messages
        log = [entry.msg for entry in caplog.records]
        log = []
        for entry in caplog.records:
            if entry.msg.startswith(" ---> Running in"):
                log.append(" ---> Running in [CONTAINER]")
            elif entry.msg.startswith(" --->"):
                log.append(" ---> [IMAGE]")
            elif entry.msg.startswith("Successfully built "):
                log.append("Successfully built [IMAGE]")
            else:
                log.append(entry.msg)

        snapshot.assert_match(log, "log")
        snapshot.assert_match(f"\n{out}", "sys.out")
        snapshot.assert_match(f"\n{err}", "sys.err")
        snapshot.assert_match(mock_image_exists.call_args_list, "mock_image_exists")
        snapshot.assert_match(
            mock_image_exists_in_registry.call_args_list, "mock_image_exists_in_registry"
        )
        snapshot.assert_match(mock_pull_image.call_args_list, "mock_pull_image")

    yield {
        "setup": setup,
        "assert_build": assert_build,
        "mock_image_exists": mock_image_exists,
        "mock_image_exists_in_registry": mock_image_exists_in_registry,
        "mock_pull_image": mock_pull_image,
    }


@pytest.fixture(
    params=[
        "image_exists",
        "image_exists_local",
        "image_does_not_exist",
        "pull_image",
        "pull_image_not_found",
    ]
)
def build_image_if_needed_scenarios(request, mock_build_image_if_needed):
    """
    Enumerates usecases for ``build_image_if_needed``
    """

    def assert_build(image):
        return mock_build_image_if_needed["assert_build"](image, scenario=request.param)

    yield {**mock_build_image_if_needed, "assert_build": assert_build}


# =================================================================================================
# Mock module environments
# =================================================================================================


@pytest.fixture
def mock_environment(base_mock_ixian_environment):
    load_module("ixian_docker.modules.docker")
    yield base_mock_ixian_environment


@pytest.fixture
def mock_npm_environment(mock_environment):
    load_module("ixian_docker.modules.npm")
    yield mock_environment


@pytest.fixture
def mock_jest_environment(mock_npm_environment):
    load_module("ixian_docker.modules.jest")
    yield mock_npm_environment


@pytest.fixture
def mock_eslint_environment(mock_npm_environment):
    load_module("ixian_docker.modules.eslint")
    yield mock_npm_environment


@pytest.fixture
def mock_webpack_environment(mock_npm_environment):
    load_module("ixian_docker.modules.webpack")
    yield mock_npm_environment


@pytest.fixture
def mock_python_environment(mock_environment):
    load_module("ixian_docker.modules.python")
    yield mock_environment


@pytest.fixture
def mock_django_environment(mock_python_environment):
    load_module("ixian_docker.modules.django")
    yield mock_python_environment
