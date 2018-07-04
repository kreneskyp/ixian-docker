import docker
from power_shovel import Task
from power_shovel.config import CONFIG
from power_shovel.modules.filesystem.file_hash import FileHash
from power_shovel_docker.modules.docker.checker import DockerVolumeExists
from power_shovel_docker.modules.docker.tasks import compose
from power_shovel_docker.modules.docker.utils import docker_client


BOWER_DEPENDS = ['build_app_image']


def clean_bower():
    """
    Remove bower volume
    """
    try:
        volume = docker_client().volumes.get(CONFIG.BOWER.COMPONENTS_VOLUME)
    except docker.errors.NotFound:
        pass
    else:
        volume.remove(True)


class BuildBower(Task):
    """Install bower packages to the app container"""
    name = 'build_bower'
    depends = BOWER_DEPENDS
    category = 'build'
    short_description = 'Install bower packages'
    parent = 'build_app'
    clean = clean_bower
    check = [
        FileHash('{BOWER.CONFIG_FILE}'),
        DockerVolumeExists('{BOWER.COMPONENTS_VOLUME}')
    ]

    def execute(self, *args):
        compose('{BOWER.BIN} install {BOWER.CONFIG_FILE_PATH}',
                *(CONFIG.BOWER.ARGS + list(args)))


class Bower(Task):
    """
    Bower package manager.

    This task is a proxy to the bower package manager. It runs within the
    context of the app container. Changes made persist for local dev
    environments.

    For bower help type: shovel bower --help
    """
    name = 'bower'
    depends = BOWER_DEPENDS
    category = 'libraries'
    short_description = 'Bower package manager'
    clean = clean_bower

    def execute(self, *args):
        compose('{BOWER.BIN}', *(CONFIG.BOWER.ARGS + list(args)))
