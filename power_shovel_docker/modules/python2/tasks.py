import docker

from power_shovel.config import CONFIG
from power_shovel.modules.filesystem.file_hash import FileHash
from power_shovel.task import Task, VirtualTarget
from power_shovel_docker.modules.docker.checker import DockerVolumeExists
from power_shovel_docker.modules.docker.tasks import run
from power_shovel_docker.modules.docker.utils import docker_client
from power_shovel.runner import ERROR_TASK

PYTHON_DEPENDS = ["build_app_image"]


class TestPython(VirtualTarget):
    """Virtual target for python tests"""

    name = "test_python"
    category = "testing"
    short_description = "Run all python test tasks"


def clean_pipenv():
    """
    Remove pipenv volume
    """
    try:
        volume = docker_client().volumes.get(CONFIG.PYTHON.VIRTUAL_ENV_VOLUME)
    except docker.errors.NotFound:
        return ERROR_TASK
    else:
        volume.remove(True)


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
        return run("pipenv", *args)


class BuildPipenv(Task):
    """Run pipenv install"""

    name = "build_pipenv"
    category = "build"
    clean = clean_pipenv
    short_description = "Install python packages with pipenv"
    parent = "build_app"
    depends = PYTHON_DEPENDS
    check = [
        FileHash("Pipfile", "Pipfile.lock",),
        DockerVolumeExists("{CONFIG.PYTHON.VIRTUAL_ENV_VOLUME}"),
    ]

    def execute(self, *args):
        pass
        # return compose('pipenv install', flags=['--dev'], *args)
