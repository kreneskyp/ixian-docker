import docker

from power_shovel.check.checker import MultiValueChecker
from power_shovel.config import CONFIG
from power_shovel_docker.modules.docker.utils import docker_client


class DockerVolumeExists(MultiValueChecker):
    """Check if docker volumes exist

    keys are volume tags.
    """

    def state(self):
        volume_ids = {}
        for volume_tag in self.keys:
            try:
                volume = docker_client().volumes.get(volume_tag)
            except docker.errors.NotFound:
                volume_id = None
            else:
                volume_id = volume.id
            volume_ids[volume_tag] = volume_id
        return volume_ids


class DockerImageExists(MultiValueChecker):
    """Check if a docker volume exists

    keys are image tags.
    """

    def state(self):
        client = docker_client()
        image_ids = {}
        for image_tag in self.keys:
            try:
                image = client.images.get(CONFIG.format(image_tag))
            except docker.errors.NotFound:
                image_id = None
            else:
                image_id = image.id
            image_ids[image_tag] = image_id
        return image_ids
