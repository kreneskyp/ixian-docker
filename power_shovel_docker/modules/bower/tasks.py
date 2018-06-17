from power_shovel import task
from power_shovel.config import CONFIG
from power_shovel_docker.modules.docker.tasks import build_app, compose


@task(depends=[build_app], category='build')
def build_bower(*args):
    """Install bower components in app container"""
    compose('./bower.sh', *args)


@task(depends=[build_app], category='build')
def bower(*args):
    """Run bower in app container"""
    compose(CONFIG.format('{BOWER.BIN}'), *args)
