import shutil
from urllib.parse import urlparse

import os
from docker.errors import NotFound as DockerNotFound
from docker.errors import ImageNotFound as ImageNotFound

from power_shovel import logger
from power_shovel.module import MODULES
from power_shovel.utils.filesystem import pwd
from power_shovel.utils.process import execute
from power_shovel.config import CONFIG
from power_shovel_docker.modules.docker.utils.client import (
    DockerClient,
    UnknownRegistry,
    docker_client,
)
from power_shovel_docker.modules.docker.utils.print import print_docker_transfer_events


def image_exists(name):
    """
    Check if image exists locally.
    :param name: name of image.
    :return: True/False
    """
    client = docker_client()
    try:
        client.images.get(name)
    except DockerNotFound:
        return False
    else:
        return True


def image_exists_in_registry(repository, tag=None):
    """
    Check if image exists in the registry.
    :param name: name of image.
    :return: True/False
    """
    # Disable check till ECR Client works
    registry = parse_registry(repository)
    client = DockerClient.for_registry(registry)
    client.login()
    image = f"{repository}:{tag or 'latest'}"
    logger.debug(f"Checking registry for {image}")
    try:
        client.client.images.get_registry_data(image)
    except DockerNotFound:
        return False
    return True


def delete_image(name, force=False):
    client = docker_client()
    try:
        image = client.images.get(name)
    except ImageNotFound:
        return False
    client.images.remove(image.id, force=force)
    return True


def build_image(dockerfile, tag, context=None, **kwargs):
    """Build a docker image.

    Builds a docker image. This is a shim around Docker-py that adds some
    power-shovel utilities to it.

    :param tag: Tag for image.
    :param file: Dockerfile.
    :param context: build context, default is the working directory.
    :param args: args to pass as build-args to build
    """
    if not context:
        context = pwd()

    client = docker_client()
    return client.images.build(
        path=context,
        dockerfile=dockerfile,
        tag=tag,
        **kwargs
    )


def build_image_if_needed(
    repository,
    tag=None,
    dockerfile="Dockerfile",
    context=None,
    pull=True,
    recheck=None,
    force=False,
    **kwargs
):
    # if local: skip
    # if remote: pull & skip
    # else: build
    image_and_tag = "{}:{}".format(repository, tag or "latest")

    logger.debug(f"Attempting to build {image_and_tag}")

    if not force:
        if image_exists(image_and_tag):
            logger.debug("Image exists, skipping build.")
            return
        else:
            logger.debug("Image does not exist.".format(tag))

        try:
            if pull and image_exists_in_registry(repository, tag):
                logger.debug("Image exists on registry. Pulling image.")
                try:
                    pull_image(repository, tag)
                except DockerNotFound:
                    logger.debug("Image could not be pulled: NotFound")
                    pass
                else:
                    logger.debug("Image pulled.")
                    # Re-check, if task now passes then build can be skipped
                    if not recheck or recheck():
                        logger.debug("Check passed, skipping build.")
                        # TODO: get image and return
                        return
            elif pull:
                logger.debug("Image does not exist on registry.")
        except UnknownRegistry as exception:
            logger.warn(
                f"Registry '{str(exception)}' is not configured, couldn't check for remote image."
            )

    return build_image(dockerfile, image_and_tag, context=context, **kwargs)


def parse_registry(repository):
    """
    Parse hostname from repository (image name)
    :param repository: image name, which may or may not include hostname
    :return: hostname of registry
    """
    parsed_url = urlparse("http://{}".format(repository))
    if parsed_url.netloc == repository:
        # if only a hostname is parsed assume no host was given. This will break if a repository
        # is just a hostname without a path. I think most repositories include paths to support
        # multiple images, so this is ok for now.
        host = "docker.io"
    else:
        host = parsed_url.netloc
    return host


def pull_image(repository, tag=None, silent=False):
    """
    Pull an image from a repository.

    :param repository: image to pull from. Docker hub assumed if repository does not begin with a
     hostname
    :param tag: tag of image. defaults to "latest"
    :return:
    """
    resolved_tag = tag or "latest"

    registry = parse_registry(repository)
    client = DockerClient.for_registry(registry)
    client.login()

    if not silent and tag is None:
        print("Using default tag: latest")

    event_stream = client.client.api.pull(
        repository, resolved_tag or "latest", stream=not silent, decode=not silent
    )
    if not silent:
        print_docker_transfer_events(event_stream)

    # Print pulled image
    print("{}:{}".format(repository, resolved_tag))


def push_image(repository, tag=None, silent=False):
    """
    Push an image to a registry.

    :param repository: repository to push to. Docker hub  assumed if repository does not begin
     with a hostname
    :param tag: image tag to push
    :param silent: don't output progress, default is False
    :return:
    """
    # default tag to latest
    resolved_tag = tag or "latest"

    registry = parse_registry(repository)
    client = DockerClient.for_registry(registry)
    client.login()

    event_stream = client.client.api.push(
        repository, resolved_tag or "latest", stream=not silent, decode=not silent
    )
    if not silent:
        print_docker_transfer_events(event_stream)
