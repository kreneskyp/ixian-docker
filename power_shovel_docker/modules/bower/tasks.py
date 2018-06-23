from power_shovel import task
from power_shovel.config import CONFIG
from power_shovel.modules.filesystem.file_hash import FileHash
from power_shovel_docker.modules.docker.checker import DockerVolumeExists
from power_shovel_docker.modules.docker.tasks import build_app_image
from power_shovel_docker.modules.docker.tasks import compose


BOWER_DEPENDS = [build_app_image]


@task(
    depends=BOWER_DEPENDS,
    category='build',
    short_description='Install bower packages',
    parent='build_app',
    check=[
        FileHash('{BOWER.CONFIG_FILE}'),
        DockerVolumeExists('{BOWER.COMPONENTS_VOLUME}'),
    ]
)
def build_bower(*args):
    """Install bower packages to the app container"""
    compose('./bower.sh', *args)


@task(
    depends=BOWER_DEPENDS,
    category='libraries',
    short_description='Bower package manager'
)
def bower(*args):
    """
    Bower package manager.

    This task is a proxy to the bower package manager. It runs within the
    context of the app container. Changes made persist for local dev
    environments.

    For bower help type: shovel bower --help
    """
    compose(CONFIG.format('{BOWER.BIN}'), *args)
