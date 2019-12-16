from unittest import mock

import pytest
from docker.errors import NotFound as DockerNotFound

from power_shovel_docker.conftest import TEST_IMAGE_NAME
from power_shovel_docker.modules.docker.utils.images import (
    image_exists,
    delete_images,
    push_image,
    pull_image,
    image_exists_in_registry,
)
from power_shovel_docker.tests import event_streams


@pytest.mark.skip
class TestImageExists:
    """
    Tests for image existing locally
    """

    def test_image_does_not_exist(self, mock_docker_environment):
        # delete images to ensure no leakage from other tests
        delete_images()
        assert not image_exists(TEST_IMAGE_NAME)

    def test_image_exists(self, test_image):
        assert image_exists(TEST_IMAGE_NAME)

    def test_delete_images(self, test_image):
        assert image_exists(TEST_IMAGE_NAME)
        delete_images()
        assert not image_exists(TEST_IMAGE_NAME)


class TestImageExistsInRegistry:
    """
    Tests for image existing on remote registry
    """

    def test_image_exists(self, mock_docker_environment):
        assert image_exists_in_registry(TEST_IMAGE_NAME) is True

    def test_image_does_not_exist(self, mock_docker_environment):
        mock_docker_environment.images.get_registry_data.side_effect = DockerNotFound(
            "mocked"
        )
        assert image_exists_in_registry(TEST_IMAGE_NAME) is False


class TestPush:
    """
    Tests for pushing image to registry
    """

    def test_push(self, mock_docker_environment, snapshot, capsys):
        """
        Test a successful push
        """
        push_image(TEST_IMAGE_NAME)
        out, err = capsys.readouterr()
        snapshot.assert_match(out)

    def test_push_already_pushed(self, mock_docker_environment, snapshot, capsys):
        """
        Test a successful push where all layers already exist on the registry
        """
        mock_docker_environment.api.push = mock.Mock(
            return_value=event_streams.PUSH_ALREADY_PRESENT
        )
        push_image(TEST_IMAGE_NAME)
        out, err = capsys.readouterr()
        snapshot.assert_match(out)

    def test_push_tag(self, mock_docker_environment, snapshot, capsys):
        """
        Test pushing with an explicit tag
        """
        mock_docker_environment.api.push = mock.Mock(
            return_value=event_streams.PUSH_SUCCESSFUL_CUSTOM_TAG
        )
        push_image(TEST_IMAGE_NAME, "custom_tag")
        out, err = capsys.readouterr()
        snapshot.assert_match(out)

    def test_push_error(self, mock_docker_environment, snapshot, capsys):
        """
        Test a push with an error
        """
        mock_docker_environment.api.push = mock.Mock(
            return_value=event_streams.ECR_PUSH_AUTH_FAILURE
        )
        push_image(TEST_IMAGE_NAME, "custom_tag")
        out, err = capsys.readouterr()
        snapshot.assert_match(out)

    def test_push_silent(self, mock_docker_environment, snapshot, capsys):
        """
        Test a successful push with silent=True
        """
        push_image(TEST_IMAGE_NAME, silent=True)
        out, err = capsys.readouterr()
        snapshot.assert_match(out)

    def test_push_error_and_silent(self, mock_docker_environment, snapshot, capsys):
        """
        Test a push with an error while silent=True
        """
        mock_docker_environment.api.push = mock.Mock(
            return_value=event_streams.ECR_PUSH_AUTH_FAILURE
        )
        push_image(TEST_IMAGE_NAME, "custom_tag", silent=True)
        out, err = capsys.readouterr()
        snapshot.assert_match(out)


class TestPull:
    """
    Tests for pulling image from registry
    """

    def test_pull(self, mock_docker_environment, snapshot, capsys):
        """
        Test a successful push
        """
        mock_client = mock_docker_environment
        pull_image(TEST_IMAGE_NAME)
        mock_client.api.pull.assert_called_with(
            TEST_IMAGE_NAME, "latest", stream=True, decode=True
        )
        out, err = capsys.readouterr()
        snapshot.assert_match(out)

    def test_pull_silent(self, mock_docker_environment, snapshot, capsys):
        """
        Test a successful push with silent=True
        """
        mock_client = mock_docker_environment
        pull_image(TEST_IMAGE_NAME, silent=True)
        mock_client.api.pull.assert_called_with(
            TEST_IMAGE_NAME, "latest", stream=False, decode=False
        )
        out, err = capsys.readouterr()
        snapshot.assert_match(out)

    def test_pull_tag(self, mock_docker_environment, snapshot, capsys):
        """
        Test pushing with an explicit tag
        """
        mock_client = mock_docker_environment
        pull_image(TEST_IMAGE_NAME, "custom_tag")
        mock_client.api.pull.assert_called_with(
            TEST_IMAGE_NAME, "custom_tag", stream=True, decode=True
        )
        out, err = capsys.readouterr()
        snapshot.assert_match(out)

    def test_pull_error(self):
        """
        Test a push with an error
        """
        raise NotImplementedError

    def test_pull_error_and_silent(self, mock_docker_environment, snapshot, capsys):
        """
        Test a push with an error while silent=True
        """
        raise NotImplementedError
