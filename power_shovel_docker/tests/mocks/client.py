import base64
import datetime
import json

import docker
import pytest
from unittest import mock

from dateutil.tz import tzlocal

from power_shovel.config import CONFIG
from power_shovel.module import load_module
from power_shovel_docker.modules.docker.utils.client import (
    DOCKER_REGISTRIES,
    DockerClient,
    ECRDockerClient,
)
from power_shovel_docker.modules.docker.utils.images import build_image
from power_shovel_docker.tests import event_streams


MOCK_REGISTRY_CONFIGS = {
    "docker.io": {
        "client": DockerClient,
        "options": {"username": "tester", "password": "secret"},
    },
    "MOCK_DEFAULT_REGISTRY": {
        "client": DockerClient,
        "options": {"username": "tester", "password": "secret"},
    },
    "MOCK_DEFAULT_REGISTRY_WITH_OPTIONS": {
        "client": DockerClient,
        "options": {"foo": "bar"},
    },
    "MOCK_ECR_REGISTRY": {"client": ECRDockerClient,},
}


@pytest.fixture
def mock_docker_environment(mock_environment):
    """
    Mock the docker environment for tests:
    - docker client partially mocked:
        - local methods not mocked
        - server interactions mocked:
            - pull
            - push
    - containers, images, volumes dropped when fixture exits
    :return:
    """
    load_module("power_shovel_docker.modules.docker")

    CONFIG.DOCKER.REGISTRIES = MOCK_REGISTRY_CONFIGS

    # mock docker remote methods
    mock_client = mock.MagicMock()
    mock_client.api.pull.return_value = (
        event for event in event_streams.PULL_SUCCESSFUL
    )
    mock_client.api.push.return_value = (
        event for event in event_streams.PUSH_SUCCESSFUL
    )
    mock_client.login = mock.Mock()
    patcher = mock.patch("power_shovel_docker.modules.docker.utils.client.docker")
    mock_docker = patcher.start()
    mock_docker.from_env.return_value = mock_client
    yield mock_client
    patcher.stop()

    # Clean docker registry - This assumes tests are running in a container and that it's safe to
    # remove docker objects after the test is complete.
    # clean_volumes
    # clean_containers
    # clean_images
    for client in DOCKER_REGISTRIES.values():
        try:
            del client.__dict__["client"]
        except KeyError:
            pass
        try:
            del client.__dict__["ecr_client"]
        except KeyError:
            pass

    DOCKER_REGISTRIES.clear()
    CONFIG.DOCKER.REGISTRIES = {}


# Mock base64 encoded token
MOCK_ECR_AUTHENTICATION_TOKEN = {
    "authorizationData": [
        {
            "authorizationToken": base64.b64encode(b"AWS:FAKE_AUTH_TOKEN"),
            "expiresAt": datetime.datetime(
                2019, 12, 1, 3, 32, 33, 000000, tzinfo=tzlocal()
            ),
            "proxyEndpoint": "https://FAKE_REGISTRY.dkr.ecr.us-west-2.amazonaws.com",
        }
    ],
    "ResponseMetadata": {
        "RequestId": "604fff98-520e-4b1e-99a4-c3c6dff7dffb",
        "HTTPStatusCode": 200,
        "HTTPHeaders": {
            "x-amzn-requestid": "604fff98-520e-4b1e-99a4-c3c6dff7dffb",
            "content-type": "application/x-amz-json-1.1",
            "content-length": "2709",
        },
        "RetryAttempts": 0,
    },
}


@pytest.fixture
def mock_ecr():
    patcher = mock.patch("power_shovel_docker.modules.docker.utils.client.boto3")
    mock_boto = patcher.start()
    mock_boto.client().get_authorization_token.return_value = (
        MOCK_ECR_AUTHENTICATION_TOKEN
    )
    yield mock_boto
    patcher.stop()
