import docker

from power_shovel.check.checker import MultiValueChecker
from power_shovel.config import CONFIG
from power_shovel_docker.modules.docker.utils.client import docker_client


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

    keys are image repositories.
    """

    def check(self):
        """All images must be present for this checker to pass"""
        return all((self.state().get(key) for key in self.keys))

    def state(self):
        """
        State is the current set of image ids.

        Note that while the checker passes if the image exists, the exact state uses the image id.
        Downstream tasks should rebuild if the state changes. If the downstream image depends on
        this one, then it should use state to determine it was not built with the same image that
        is present.
        """
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
