from power_shovel.task import Task
from power_shovel.config import CONFIG
from power_shovel.modules.filesystem.file_hash import FileHash
from power_shovel_docker.modules.docker.checker import DockerImageExists
from power_shovel_docker.modules.docker.tasks import compose
from power_shovel_docker.modules.docker.utils.images import build_image_if_needed

WEBPACK_DEPENDS = ["build_npm"]


class BuildWebpackImage(Task):
    """
    Build image with javascript, css, etc. compiled by Webpack.
    """

    name = "build_webpack_image"
    parent = "build_image"
    depends = ["build_npm_image"]
    category = "build"
    short_description = "Build Webpack image"
    check = [
        FileHash("{WEBPACK.DOCKERFILE}", "{WEBPACK.CONFIG_FILE}"),
        DockerImageExists("{WEBPACK.IMAGE}"),
    ]

    def execute(self, pull=True):
        build_image_if_needed(
            repository=CONFIG.WEBPACK.REPOSITORY,
            tag=CONFIG.WEBPACK.IMAGE_TAG,
            dockerfile=CONFIG.WEBPACK.DOCKERFILE,
            force=self.__task__.force,
            pull=pull,
            # recheck=self.check.check,
            buildargs={
                "FROM_REPOSITORY": CONFIG.DOCKER.APP_IMAGE,
                "FROM_TAG": CONFIG.NPM.IMAGE_TAG,
            },
        )


class Webpack(Task):
    """
    Run webpack javascript/css compiler.

    This task runs the webpack compiler. It runs using `compose` to run within
    the context of the app image.
    """

    name = "webpack"
    category = "build"
    depends = WEBPACK_DEPENDS
    short_description = "Webpack javascript/css compiler"
    parent = "build_app"
    check = FileHash("{WEBPACK.CONFIG_FILE}", *CONFIG.WEBPACK.SOURCE_DIRS)
    config = [
        "{WEBPACK.CONFIG_FILE}",
        "{WEBPACK.CONFIG_FILE_PATH}",
        "{WEBPACK.COMPILED_STATIC_DIR}",
        "{WEBPACK.COMPILED_STATIC_VOLUME}",
        "{WEBPACK.ARGS}",
    ]

    def execute(self, *args):
        return compose("webpack", *(CONFIG.WEBPACK.ARGS + list(args)))


class WebpackWatch(Task):
    """Run webpack builder with --watch flag so it will continuously build."""

    name = "webpack_watch"
    category = "build"
    depends = WEBPACK_DEPENDS
    short_description = "Webpack builder with file-watching."

    def execute(self, *args):
        return compose("webpack --watch", *(CONFIG.WEBPACK.ARGS + list(args)))
