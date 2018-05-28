from power_shovel.task import task
from power_shovel_docker.modules.docker.tasks import compose, build_app


NPM_DEPENDS = [build_app]


@task(depends=NPM_DEPENDS)
def npm_update(*args, **kwargs):
    """Update package.json with ncu"""
    compose('ncu -u', *args, **kwargs)


@task(depends=NPM_DEPENDS)
def build_npm(*args, **kwargs):
    """Run 'npm install' within the context of the app container."""
    compose('npm install', *args, **kwargs)


@task(depends=NPM_DEPENDS)
def npm(*args, **kwargs):
    """Run npm within the context of the app container"""
    compose('npm', *args, **kwargs)
