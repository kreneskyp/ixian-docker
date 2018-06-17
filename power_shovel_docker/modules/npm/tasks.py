from power_shovel.modules.filesystem.file_hash import FileHash
from power_shovel.task import task
from power_shovel_docker.modules.docker.tasks import compose, build_app


NPM_DEPENDS = [build_app]
# TODO disable build_app until it can determine rebuilds better
NPM_DEPENDS = []


@task(depends=NPM_DEPENDS, category='build')
def npm_update(*args):
    """Update package.json with ncu"""
    compose('ncu -u', *args)


@task(depends=NPM_DEPENDS, auto_help=False, category='build')
def ncu(*args):
    """Run NPM Check Updates (NCU)"""
    compose('ncu', *args)


@task(
    depends=NPM_DEPENDS,
    category='build',
    check=FileHash('{NPM.PACKAGE_JSON}')
)
def build_npm(*args, **kwargs):
    """Run 'npm install' within the context of the app container."""
    compose('npm install', *args, **kwargs)


@task(depends=NPM_DEPENDS, category='build', auto_help=False)
def npm(*args):
    """Run npm within the context of the app container"""
    compose('npm', *args)
