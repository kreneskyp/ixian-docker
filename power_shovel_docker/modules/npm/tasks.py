import docker

from power_shovel import logger
from power_shovel.config import CONFIG
from power_shovel.modules.filesystem.file_hash import FileHash
from power_shovel.task import Task
from power_shovel_docker.modules.docker.checker import DockerVolumeExists
from power_shovel_docker.modules.docker.tasks import compose
from power_shovel_docker.modules.docker.utils import docker_client


NPM_DEPENDS = ['build_app_image']


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


class NPMUpdate(Task):
    """
    Update package.json with Node Check Update (ncu)
    """

    name = 'npm_update'
    category = 'Libraries'
    depends = NPM_DEPENDS
    short_description = 'Update npm libraries in package.json'

    def execute(self, *args):
        args = args or ['-u']
        return compose('ncu', *args)


class NCU(Task):
    """Run NPM Check Updates (NCU)"""

    name = 'ncu'
    category = 'Libraries'
    depends = NPM_DEPENDS
    short_description = 'NPM package updater'

    def execute(self, *args):
        return compose('ncu', *args)


class BuildNPM(Task):
    """Run 'npm install' within the context of the app container."""

    name = 'build_npm'
    category = 'build'
    check = [
        FileHash('{NPM.PACKAGE_JSON}'),
        DockerVolumeExists('{NPM.NODE_MODULES_VOLUME}')
    ]
    clean = clean_npm
    depends = NPM_DEPENDS
    parent = "build_app"
    short_description = 'Install NPM packages.'

    def execute(self, *args):
        return compose('npm install', *args)


class NPM(Task):
    """Run npm within the context of the app container"""

    name = 'npm'
    category = 'Libraries'
    depends = NPM_DEPENDS
    short_description = 'NPM package manager.'

    def execute(self, *args):
        return compose('npm', *args)
