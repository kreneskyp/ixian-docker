import docker
from power_shovel.config import CONFIG
from power_shovel.modules.filesystem.file_hash import FileHash
from power_shovel.task import task
from power_shovel_docker.modules.docker.checker import DockerVolumeExists
from power_shovel_docker.modules.docker.tasks import build_app_image
from power_shovel_docker.modules.docker.tasks import compose
from power_shovel_docker.modules.docker.utils import docker_client
from runner import ERROR_TASK

PYTHON_DEPENDS = [build_app_image]
PYTHON_DEPENDS = []


def python_local_package_mount_flags():
    return []


@task(
    category='testing',
    short_description='Run all python test tasks',
    depends=PYTHON_DEPENDS
)
def test_python():
    """Virtual target for python tests"""


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
    return 0


@task(
    category='libraries',
    short_description='PipEnv environment manager',
    depends=PYTHON_DEPENDS,
    clean = clean_pipenv,
)
def pipenv(*args):
    """
    Run a pipenv command.

    This runs in the builder container with volumes mounted.
    """
    return compose('pipenv', *args)


@task(
    category='build',
    clean=clean_pipenv,
    short_description='Install python packages with pipenv',
    depends=PYTHON_DEPENDS,
    parent='build_app',
    check=[
        FileHash('Pipfile', 'Pipfile.lock'),
        DockerVolumeExists('{PYTHON.VIRTUAL_ENV_VOLUME}')
    ]
)
def build_pipenv(*args):
    """Run pipenv install"""
    pass
    #compose('pipenv install', flags=['--dev'], *args)
