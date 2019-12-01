from unittest import mock

import botocore
import pytest
import docker

from power_shovel_docker.modules.docker.utils.client import (
    DockerClient,
    docker_client,
    UnknownRegistry,
)


def test_get_client():
    """Sanity check"""
    assert isinstance(docker_client(), docker.DockerClient)


class TestDockerClient:
    def test_for_registry(self, mock_docker_environment):
        mock_client = mock_docker_environment
        client = DockerClient.for_registry("MOCK_DEFAULT_REGISTRY")
        assert isinstance(client, DockerClient)
        assert client.client is mock_client

        # sanity test mocks
        print(client, client.client, mock_client)
        client.client.api.push.assert_not_called()
        client.client.api.pull.assert_not_called()
        client.client.login.assert_not_called()

    def test_unknown_registry(self, mock_docker_environment):
        """Test requesting a registry that isn't configured"""
        with pytest.raises(UnknownRegistry):
            DockerClient.for_registry("REGISTRY_DOES_NOT_EXIST")

    def test_client_options(self, mock_docker_environment):
        mock_client = mock_docker_environment
        client = DockerClient.for_registry("MOCK_DEFAULT_REGISTRY")
        assert isinstance(client, DockerClient)
        assert client.client is mock_client


class TestECRDockerClient:
    def test_for_registry(self, mock_docker_environment, mock_ecr):
        mock_client = mock_docker_environment
        client = DockerClient.for_registry("MOCK_ECR_REGISTRY")
        assert isinstance(client, DockerClient)
        assert client.client is mock_client

        # sanity test mocks
        client.client.api.push.assert_not_called()
        client.client.api.pull.assert_not_called()
        client.client.login.assert_not_called()

        # get ecr_client
        assert isinstance(client.ecr_client, mock.Mock)

    def test_login(self, mock_docker_environment, mock_ecr):
        client = DockerClient.for_registry("MOCK_ECR_REGISTRY")
        client.login()
        client.client.login.assert_called_with(
            "AWS",
            "FAKE_AUTH_TOKEN",
            "",
            registry="https://FAKE_REGISTRY.dkr.ecr.us-west-2.amazonaws.com",
        )
