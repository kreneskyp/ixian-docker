from power_shovel import Task
from power_shovel.config import CONFIG
from power_shovel.modules.filesystem.file_hash import FileHash
from power_shovel_docker.modules.docker.tasks import compose


WEBPACK_DEPENDS = [
    'build_npm'
]


class Webpack(Task):
    """
    Run webpack javascript/css compiler.

    This task runs the webpack compiler. It runs using `compose` to run within
    the context of the app image.
    """

    name = 'webpack'
    category = 'build'
    depends = WEBPACK_DEPENDS
    short_description = 'Webpack javascript/css compiler'
    parent = 'build_app'
    check = FileHash(
        '{WEBPACK.CONFIG_FILE}',
        *CONFIG.WEBPACK.SOURCE_DIRS
    )
    config = [
        '{WEBPACK.CONFIG_FILE}',
        '{WEBPACK.CONFIG_FILE_PATH}',
        '{WEBPACK.COMPILED_STATIC_DIR}',
        '{WEBPACK.COMPILED_STATIC_VOLUME}',
    ]

    def execute(self, *args):
        return compose('./webpack.sh', *args)


class WebpackWatch(Task):
    """Run webpack builder with --watch flag so it will continuously build."""

    name = 'webpack_watch'
    category = 'build'
    depends = WEBPACK_DEPENDS
    short_description = 'Webpack builder with file-watching.'

    def execute(self, *args):
        return compose('./webpack.sh --watch', *args)
