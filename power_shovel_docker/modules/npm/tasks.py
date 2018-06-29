import docker

from power_shovel import logger
from power_shovel.config import CONFIG
from power_shovel.modules.filesystem.file_hash import FileHash
from power_shovel.task import task
from power_shovel_docker.modules.docker.checker import DockerVolumeExists
from power_shovel_docker.modules.docker.tasks import build_app_image
from power_shovel_docker.modules.docker.tasks import compose
from power_shovel_docker.modules.docker.utils import docker_client


NPM_DEPENDS = [build_app_image]


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
        logger.debug('Deleted docker image: %s'
                     % CONFIG.PYTHON.VIRTUAL_ENV_VOLUME)


@task(
    category='Libraries',
    depends=NPM_DEPENDS,
    short_description='Update npm libraries in package.json'
)
def npm_update(*args):
    """
    Update package.json with Node Check Update (ncu)


    """
    args = args or ['-u']
    return compose('ncu', args)


@task(
    category='Libraries',
    depends=NPM_DEPENDS,
    short_description='NPM package updater'
)
def ncu(*args):
    """Run NPM Check Updates (NCU)"""
    return compose('ncu', args)


@task(
    category='build',
    check=[
        FileHash('{NPM.PACKAGE_JSON}'),
        DockerVolumeExists('{NPM.NODE_MODULES_VOLUME}')
    ],
    clean=clean_npm,
    depends=NPM_DEPENDS,
    parent="build_app",
    short_description='Install NPM packages.'
)
def build_npm(*args):
    """Run 'npm install' within the context of the app container."""
    return compose('npm install', args)


@task(
    category='Libraries',
    depends=NPM_DEPENDS,
    short_description='NPM package manager.'
)
def npm(*args):
    """Run npm within the context of the app container"""
    return compose('npm', args)
