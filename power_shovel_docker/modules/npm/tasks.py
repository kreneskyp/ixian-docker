import docker
import logging

from power_shovel.config import CONFIG
from power_shovel.modules.filesystem.file_hash import FileHash
from power_shovel.task import Task
from power_shovel_docker.modules.docker.checker import (
    DockerImageExists,
)
from power_shovel_docker.modules.docker.tasks import compose
from power_shovel_docker.modules.docker.utils.client import docker_client
from power_shovel_docker.modules.docker.utils.images import build_image_if_needed
from power_shovel_docker.modules.docker.utils.volumes import delete_volume

logger = logging.getLogger(__name__)
NPM_DEPENDS = ["build_app_image"]


def remove_npm_volume():
    """
    Remove node_modules volume
    """
    delete_volume(CONFIG.NPM.NODE_MODULES_VOLUME)


class BuildNPMImage(Task):
    name = "build_npm_image"
    parent = ["build_image", "compose_runtime"]
    depends = ["build_base_image"]
    category = "build"
    short_description = "Build NPM image"
    check = [
        FileHash(
            "{NPM.DOCKERFILE}",
            *CONFIG.resolve('NPM.IMAGE_FILES')
        ),
        DockerImageExists("{NPM.IMAGE}")
    ]

    def execute(self, pull=True):
        build_image_if_needed(
            repository=CONFIG.NPM.REPOSITORY,
            tag=CONFIG.NPM.IMAGE_TAG,
            dockerfile=CONFIG.NPM.DOCKERFILE,
            force=self.__task__.force,
            pull=pull,
            # recheck=self.check.check,
            buildargs={
                "FROM_REPOSITORY": CONFIG.DOCKER.REPOSITORY,
                "FROM_TAG": CONFIG.DOCKER.BASE_IMAGE_TAG,
            },
        )


class NCU(Task):
    """Update package.json with Node Check Update (ncu)"""

    name = "ncu"
    category = "Libraries"
    # TODO: depends without injecting it into parent task
    depends = ["compose_runtime"]
    short_description = "Update npm libraries in package.json"
    clean = remove_npm_volume

    def execute(self, *args):
        return compose("ncu", args)


class NPM(Task):
    """Run npm within the context of the app container"""

    name = "npm"
    category = "Libraries"
    depends = ["compose_runtime"]
    short_description = "NPM package manager."
    clean = remove_npm_volume

    def execute(self, *args):
        args = args or ["install"]
        return compose("npm", args)
