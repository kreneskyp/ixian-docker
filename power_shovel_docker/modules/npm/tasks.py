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


logger = logging.getLogger(__name__)
NPM_DEPENDS = ["build_app_image"]


def clean_npm():
    """
    Remove node_modules volume
    """
    try:
        volume = docker_client().volumes.get(CONFIG.PYTHON.VIRTUAL_ENV_VOLUME)
    except docker.errors.NotFound:
        pass
    else:
        volume.remove(True)
        logger.debug("Deleted docker image: %s" % CONFIG.PYTHON.VIRTUAL_ENV_VOLUME)


class BuildNPMImage(Task):
    name = "build_npm_image"
    parent = "build_app_image"
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


class NPMUpdate(Task):
    """
    Update package.json with Node Check Update (ncu)
    """

    name = "npm_update"
    category = "Libraries"
    depends = NPM_DEPENDS
    short_description = "Update npm libraries in package.json"

    def execute(self, *args):
        args = args or ["-u"]
        return compose("ncu", *args)


class NCU(Task):
    """Run NPM Check Updates (NCU)"""

    name = "ncu"
    category = "Libraries"
    depends = NPM_DEPENDS
    short_description = "NPM package updater"

    def execute(self, *args):
        return compose("ncu", *args)


class BuildNPM(Task):
    """Run 'npm install' within the context of the app container."""

    name = "build_npm"
    category = "build"
    check = [
        FileHash("{NPM.PACKAGE_JSON}"),
    ]
    clean = clean_npm
    depends = NPM_DEPENDS
    parent = "build_app"
    short_description = "Install NPM packages."

    def execute(self, *args):
        return compose("npm install", *args)


class NPM(Task):
    """Run npm within the context of the app container"""

    name = "npm"
    category = "Libraries"
    depends = NPM_DEPENDS
    short_description = "NPM package manager."

    def execute(self, *args):
        return compose("npm", *args)
