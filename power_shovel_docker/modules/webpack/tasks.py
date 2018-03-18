from power_shovel.config import CONFIG
from power_shovel import task
from power_shovel_docker.modules.docker.utils import build_image
from power_shovel_docker.modules.docker.utils import run_builder
from power_shovel_docker.modules.docker.utils import build_volume_from_image
from power_shovel_docker.modules.docker.utils import build_library_image
from power_shovel_docker.modules.npm.utils import npm_local_package_mount_flags


@task()
def build_webpack_builder():
    build_image(CONFIG.WEBPACK.BUILDER_TAG,
                CONFIG.WEBPACK.BUILDER_DOCKERFILE,
                context=CONFIG.WEBPACK.BUILDER_CONTEXT)


def webpack_builder_kwargs(image=CONFIG.WEBPACK.BUILDER_TAG):
    volumes = [
        '{PWD}:{DOCKER.PROJECT_DIR}',
        # TODO : volume names shouldn't be defined here
        'builder.npm.node_modules:{DOCKER.APP_DIR}/node_modules',
        #'{BUILDER}/webpack.bash_history:{DOCKER.HOME_DIR}/.bash_history'
    ]

    # npm local packages are only symlinked. Mount local packages so they are
    # available to webpack.
    volumes.extend(npm_local_package_mount_flags())

    return dict(
        image=image,
        outputs=[
            'compiled_static'
        ],
        env={
            'APP_DIR': CONFIG.DOCKER.APP_DIR,
            'NODE_MODULES_DIR': CONFIG.NPM.NODE_MODULES_DIR,
            'WEBPACK_CONFIG': CONFIG.WEBPACK.CONFIG_FILE_PATH,
            'OUTPUT': CONFIG.WEBPACK.COMPILED_STATIC_DIR
        },
        volumes=volumes
    )


@task()
def build_webpack_image(tag='webpack', image=CONFIG.WEBPACK.BUILDER_TAG):
    build_library_image(tag, **webpack_builder_kwargs(image))


@task()
def build_webpack_volume(tag='webpack'):
    build_webpack_image(tag)
    build_volume_from_image(
        'webpack', CONFIG.WEBPACK.COMPILED_STATIC_DIR, 'webpack')


@task()
def webpack_builder_shell(image=CONFIG.WEBPACK.BUILDER_TAG):
    """
    open a bash shell in the webpack builder with volumes mounted. This allows
    for manually running webpack commands.
    """
    run_builder(command='/bin/bash', **webpack_builder_kwargs(image))


@task()
def webpack_watch(image=CONFIG.WEBPACK.BUILDER_TAG):
    """
    Run webpack builder with --watch flag so it will continuously build.

    :param image:
    :return:
    """
    # TODO this should build into volume so it builds on top of pulled image
    run_builder(flags='--watch', **webpack_builder_kwargs(image))
