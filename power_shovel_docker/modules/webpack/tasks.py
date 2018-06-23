from power_shovel import task
from power_shovel_docker.modules.docker.tasks import compose
from power_shovel_docker.modules.npm.tasks import build_npm


WEBPACK_DEPENDS = [
    build_npm
]


@task(
    category='build',
    depends=WEBPACK_DEPENDS,
    short_description='Webpack javascript/css compiler'
)
def webpack(*args):
    """
    Run webpack javascript/css compiler.

    This task runs the webpack compiler. It runs using `compose` to run within
    the context of the app image.

    Configuration:
      - WEBPACK.CONFIG_FILE:             {WEBPACK.CONFIG_FILE}
      - WEBPACK.CONFIG_FILE_PATH:        {WEBPACK.CONFIG_FILE_PATH}
      - WEBPACK.COMPILED_STATIC_DIR:     {WEBPACK.COMPILED_STATIC_DIR}
      - WEBPACK.COMPILED_STATIC_VOLUME:  {WEBPACK.COMPILED_STATIC_VOLUME}
    """
    compose('./webpack.sh', *args)


@task(
    category='build',
    depends = WEBPACK_DEPENDS,
    short_description='Webpack builder with file-watching.'
)
def webpack_watch(*args):
    """Run webpack builder with --watch flag so it will continuously build."""
    compose('./webpack.sh --watch', *args)
