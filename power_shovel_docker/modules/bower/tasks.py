from power_shovel import task
from power_shovel.config import CONFIG
from power_shovel.modules.filesystem.file_hash import FileHash
from power_shovel_docker.modules.docker.checker import DockerVolumeExists
from power_shovel_docker.modules.docker.tasks import build_app, compose


@task(
    depends=[build_app],
    category='build',
    short_description='Install bower packages',
    parent='build_app',
    check=[
        FileHash('{BOWER.CONFIG_FILE}'),
        DockerVolumeExists('{BOWER.COMPONENTS_VOLUME}'),
    ]
)
def build_bower(*args):
    """Install bower components in app container"""
    compose('./bower.sh', *args)


@task(
    depends=[build_app],
    category='libraries',
    short_description='Bower package manager'
)
def bower(*args):
    """Run bower in app container"""
    compose(CONFIG.format('{BOWER.BIN}'), *args)
