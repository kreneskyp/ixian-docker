import base64

import boto3
import docker

from power_shovel import logger
from power_shovel.utils.decorators import cached_property


# Global cache of registries that are created.
DOCKER_REGISTRIES = {}


def docker_client():
    return docker.from_env()


class Docker:

    @classmethod
    def for_registry(cls, registry):
        try:
            return DOCKER_REGISTRIES[registry]
        except KeyError:
            pass
        #instance = cls()
        # TODO: need to decide out how to map registries
        instance = ECRDockerClient()
        DOCKER_REGISTRIES[registry] = instance
        return instance

    @cached_property
    def client(self):
        return docker_client()

    def login(self):
        raise NotImplementedError


class ECRDockerClient(Docker):

    @cached_property
    def ecr_client(self):
        # TODO: where are initialized from?
        return boto3.client('ecr', region_name='eu-west-2')

    def login(self):
        # fetch credentials from ECR
        logger.debug("Authenticating with ECR: {}".format('eu-west-2'))
        token = self.ecr_client.get_authorization_token()
        username, password = base64.b64decode(token['authorizationData'][0]['authorizationToken']).decode().split(':')
        registry = token['authorizationData'][0]['proxyEndpoint']

        # authenticate
        self.client.login(username, password, "", registry=registry)
        print(self.client, id(self.client))
        #import ipdb
        #ipdb.sset_trace()

        logger.debug("Authenticated.")


def authenticate_client(client):
    """
    Helper to create an authenticated docker client.

    TODO: this is just a temp solution. Need something more extensible that can handle different authentication methods
    """

    # ECR requires that creds be fetched from the API
    ecr_client = boto3.client('ecr', region_name='eu-west-2')
    token = ecr_client.get_authorization_token()
    username, password = base64.b64decode(token['authorizationData'][0]['authorizationToken']).decode().split(':')
    registry = token['authorizationData'][0]['proxyEndpoint']

    client.login(username, password, "", registry=registry)
    return docker_client