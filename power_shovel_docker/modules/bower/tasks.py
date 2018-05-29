from power_shovel import task
from power_shovel.config import CONFIG
from power_shovel_docker.modules.docker.tasks import build_app, compose


@task(depends=[build_app])
def build_bower(*args, **kwargs):
    """Install bower components in app container"""
    compose('./bower.sh', *args, **kwargs)


@task(depends=[build_app])
def bower(*args, **kwargs):
    """Run bower in app container"""
    compose(CONFIG.format('{BOWER.BIN}'), *args, **kwargs)
