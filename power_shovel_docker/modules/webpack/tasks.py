from power_shovel.config import CONFIG
from power_shovel import task
from power_shovel.modules.filesystem.file_hash import FileHash
from power_shovel_docker.modules.docker.checker import DockerImageExists
from power_shovel_docker.modules.docker.utils import build_image
from power_shovel_docker.modules.docker.utils import build_library_volumes
from power_shovel_docker.modules.docker.utils import run_builder
from power_shovel_docker.modules.docker.utils import build_library_image
from power_shovel_docker.modules.npm.tasks import build_npm_volume
from power_shovel_docker.modules.npm.utils import npm_local_package_mount_flags


@task()
def delete_webpack_builder():
    print(CONFIG.FORMAT('TODO: delete image "{WEBPACK.BUILDER_TAG}"'))



@task(
    check=[
        FileHash('{WEBPACK.MODULE_DIR}'),
        DockerImageExists('{WEBPACK.BUILDER_TAG}')
    ],
    clean=delete_webpack_builder)
def build_webpack_builder():
    build_image(CONFIG.WEBPACK.BUILDER_TAG,
                CONFIG.WEBPACK.BUILDER_DOCKERFILE,
                context=CONFIG.WEBPACK.BUILDER_CONTEXT)


def webpack_builder_kwargs(image=CONFIG.WEBPACK.BUILDER_TAG):
    volumes = [
        '{PWD}:{DOCKER.PROJECT_DIR}',
        # TODO : volume names shouldn't be defined here
        '{PROJECT_NAME}.node_modules:{DOCKER.APP_DIR}/node_modules',
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


@task(parent='build_docker_images',
      check=FileHash(
          'webpack.config.js',
          '{PWD}/static'))
def build_webpack_image(tag='webpack', image=CONFIG.WEBPACK.BUILDER_TAG):
    build_library_image(tag, **webpack_builder_kwargs(image))


@task(depends=[build_npm_volume, build_webpack_builder],
      parent='build_docker_volumes')
def build_webpack_volume(image=CONFIG.WEBPACK.BUILDER_TAG):
    build_library_volumes(**webpack_builder_kwargs(image))


@task()
def webpack_builder_shell(image=CONFIG.WEBPACK.BUILDER_TAG):
    """
    open a bash shell in the webpack builder with volumes mounted. This allows
    for manually running webpack commands.
    """
    run_builder(command='/bin/bash', **webpack_builder_kwargs(image))


@task(depends=[build_webpack_volume])
def webpack_watch(image=CONFIG.WEBPACK.BUILDER_TAG):
    """
    Run webpack builder with --watch flag so it will continuously build.

    :param image:
    :return:
    """
    # TODO this should build into volume so it builds on top of pulled image
    run_builder(flags='--watch', **webpack_builder_kwargs(image))
