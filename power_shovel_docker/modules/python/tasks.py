import docker
from power_shovel.config import CONFIG
from power_shovel.modules.filesystem.file_hash import FileHash
from power_shovel.task import Task, VirtualTarget
from power_shovel_docker.modules.docker.checker import (
    DockerVolumeExists,
    DockerImageExists,
)
from power_shovel_docker.modules.docker.tasks import compose
from power_shovel_docker.modules.docker.utils.client import docker_client
from power_shovel_docker.modules.docker.utils.images import build_image_if_needed
from power_shovel.runner import ExitCodes

PYTHON_DEPENDS = ["build_base_image"]


def python_local_package_mount_flags():
    return []


class BuildPythonImage(Task):

    name = "build_python_image"
    parent = ["build_image", "compose_runtime"]
    depends = ["build_base_image"]
    category = "build"
    short_description = "Build Python image"
    check = [
        FileHash(
            "{PYTHON.DOCKERFILE}",
            *CONFIG.resolve('PYTHON.IMAGE_FILES')
        ),
        DockerImageExists("{PYTHON.IMAGE}"),
    ]

    def execute(self, pull=True):
        build_image_if_needed(
            repository=CONFIG.PYTHON.REPOSITORY,
            tag=CONFIG.PYTHON.IMAGE_TAG,
            dockerfile=CONFIG.PYTHON.DOCKERFILE,
            force=self.__task__.force,
            pull=pull,
            # recheck=self.check.check,
            buildargs={
                "FROM_REPOSITORY": CONFIG.DOCKER.REPOSITORY,
                "FROM_TAG": CONFIG.DOCKER.BASE_IMAGE_TAG,
            },
        )


class TestPython(VirtualTarget):
    """Virtual target for python tests"""

    name = "test_py"
    category = "testing"
    short_description = "Run all python test tasks"


def clean_pipenv():
    """
    Remove pipenv volume
    """
    try:
        volume = docker_client().volumes.get(CONFIG.PYTHON.VIRTUAL_ENV_VOLUME)
    except docker.errors.NotFound:
        return ExitCodes.ERROR_TASK
    else:
        volume.remove(True)
    return ExitCodes.SUCCESS


class Pip(Task):
    """
    Pip package manager
    """
    name = "pip"
    category = "libraries"
    depends = PYTHON_DEPENDS
    short_description = "Pip python package manager"
    clean = clean_pipenv

    def execute(self, *args):
        return compose("pip", *args)


class Pipenv(Task):
    """
    Run a pipenv command.

    This runs in the builder container with volumes mounted.
    """

    name = "pipenv"
    category = "libraries"
    short_description = "PipEnv environment manager"
    depends = PYTHON_DEPENDS
    clean = clean_pipenv

    def execute(self, *args):
        return compose("pipenv", *args)


class BuildPipenv(Task):
    """Run pipenv install"""

    name = "build_pipenv"
    category = "build"
    clean = clean_pipenv
    short_description = "Install python packages with pipenv"
    depends = PYTHON_DEPENDS
    parent = "build_app"
    check = [
        FileHash("Pipfile", "Pipfile.lock"),
        DockerVolumeExists("{PYTHON.VIRTUAL_ENV_VOLUME}"),
    ]

    def execute(self, *args):
        pass
        # return compose('pipenv install', flags=['--dev'], *args)
