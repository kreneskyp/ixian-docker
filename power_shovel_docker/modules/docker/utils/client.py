import base64

import boto3
import docker

from power_shovel import logger
from power_shovel.config import CONFIG
from power_shovel.utils.decorators import cached_property


# Global cache of registries that are created.
DOCKER_REGISTRIES = {}


def docker_client():
    return docker.from_env()


class UnknownRegistry(Exception):
    """Exception raised when registry is not configured"""
    pass


class Docker:

    def __init__(self, **options):
        self.options = options

    @classmethod
    def for_registry(cls, registry):
        try:
            return DOCKER_REGISTRIES[registry]
        except KeyError:
            pass

        # Instantiate client for registry
        try:
            config = CONFIG.DOCKER.REGISTRIES[registry]
        except KeyError:
            logger.warn(f"Registry missing from DOCKER.REGISTRIES: {registry}")
            raise UnknownRegistry(registry)

        Client = config["client"]
        instance = Client(**config.get("options", {}))
        DOCKER_REGISTRIES[registry] = instance

        return instance

    @cached_property
    def client(self):
        return docker_client()

    def login(self):
        raise NotImplementedError


class ECRDockerClient(DockerClient):
    @cached_property
    def ecr_client(self):
        kwargs = dict(region_name="us-west-2", **self.options)
        return boto3.client("ecr", **kwargs)

    def login(self):
        # fetch credentials from ECR
        logger.debug(
            "Authenticating with ECR: {}".format(
                self.options.get("region_name", "us-west-2")
            )
        )
        token = self.ecr_client.get_authorization_token()
        username, password = (
            base64.b64decode(token["authorizationData"][0]["authorizationToken"])
            .decode()
            .split(":")
        )
        registry = token["authorizationData"][0]["proxyEndpoint"]

        # authenticate
        self.client.login(username, password, "", registry=registry)
