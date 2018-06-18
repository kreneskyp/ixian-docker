from power_shovel import task
from power_shovel_docker.modules.docker.tasks import compose, build_app
from power_shovel_docker.modules.npm.tasks import build_npm


WEBPACK_DEPENDS = [
    build_npm
]


@task(
    category='build',
    depends=WEBPACK_DEPENDS,
    short_description='Webpack javascript compiler'
)
def webpack(*args, **kwargs):
    """Run webpack builder."""
    compose('./webpack.sh', *args, **kwargs)


@task(
    category='build',
    depends = WEBPACK_DEPENDS,
    short_description='Webpack builder with file-watching.'
)
def webpack_watch():
    """Run webpack builder with --watch flag so it will continuously build."""
    compose('./webpack.sh --watch')
