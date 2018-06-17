from power_shovel import task
from power_shovel_docker.modules.docker.tasks import compose, build_app
from power_shovel_docker.modules.npm.tasks import build_npm


WEBPACK_DEPENDS = [
    build_npm
]


@task(depends=WEBPACK_DEPENDS, category='build')
def webpack(*args, **kwargs):
    """Run webpack builder."""
    compose('./webpack.sh', *args, **kwargs)


@task(depends=WEBPACK_DEPENDS, category='build')
def webpack_watch():
    """Run webpack builder with --watch flag so it will continuously build."""
    compose('./webpack.sh --watch')
