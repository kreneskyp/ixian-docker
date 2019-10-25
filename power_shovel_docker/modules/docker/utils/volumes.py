import docker
from docker.errors import NotFound as DockerNotFound

from power_shovel.utils.process import execute
from power_shovel.config import CONFIG


def volume_exists(tag):
    client = docker.from_env()
    try:
        client.images.get(tag)
    except DockerNotFound:
        return False
    else:
        return True

g
def build_volume_from_image(image, path, tag=None):
    """Build a volume from a docker image.

    This utility is used to build volumes from an existing image. This allows
    images stored in a registry to pulled and used as libraries.

    :param image: image tag to build from
    :param path: path within docker image to create a volume for
    :param tag: volume tag, defaults to image name
    """
    tag = tag or image

    # TODO: list of outputs instead of single path
    # TODO: remove existing volume first
    #execute('docker volume rm %s' % tag)
    execute('docker run -v {tag}:{path} --rm {image} true'.format(
        image=image,
        path=path,
        tag=tag
    ))


def convert_volume_flags(volumes):
    """Format volume patterns into volume flags.

    TODO: deprecate this and let docker-py handle formatting volumes

    :param volumes: list of volume strings
    :return: list of volume flags
    """
    return ['-v %s' % CONFIG.format(volume) for volume in volumes]