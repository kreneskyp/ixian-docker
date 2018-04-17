from power_shovel import task
from power_shovel.modules.filesystem.file_hash import FileHash
from power_shovel_docker.modules.docker.checker import DockerImageExists
from power_shovel_docker.modules.docker.utils import build_image
from power_shovel_docker.modules.docker.utils import build_library_volumes
from power_shovel_docker.modules.docker.utils import run_builder
from power_shovel_docker.modules.docker.utils import build_library_image
from power_shovel_docker.modules.npm.utils import npm_local_package_mount_flags
from power_shovel.config import CONFIG


@task(
    check=[
        FileHash('{BOWER.MODULE_DIR}'),
        DockerImageExists('{BOWER.BUILDER_TAG}')
    ],
)
def build_bower_builder():
    """Builder image for building bower library."""
    build_image(CONFIG.BOWER.BUILDER_TAG,
                CONFIG.BOWER.BUILDER_DOCKERFILE,
                context=CONFIG.BOWER.BUILDER_CONTEXT)


def bower_builder_kwargs(image=CONFIG.BOWER.BUILDER_TAG):
    """Build kwargs needed when using the bower builder.

    :param image: tag of builder image to use.
    :return: dict of kwarg to pass to `compose`
    """
    volumes = [
        '{PWD}:{DOCKER.PROJECT_DIR}',

        # bash_history isn't working, might need to generate empty file first
        #'{BUILDER}/bower.bash_history:{DOCKER.HOME_DIR}/.bash_history'
    ]

    # npm local packages are only symlinked. Mount local packages so they are
    # available to bower.
    volumes.extend(npm_local_package_mount_flags())

    return dict(
        image=image,
        outputs=[
            'bower_components'
        ],
        env={
            'APP_DIR': CONFIG.DOCKER.APP_DIR,
            'BOWER_CONFIG': CONFIG.BOWER.CONFIG_FILE_PATH,
            'OUTPUT': CONFIG.BOWER.COMPONENTS_DIR
        },
        volumes=volumes
    )


@task(depends=[build_bower_builder],
      parent='build_docker_images')
def build_bower_image(tag='bower', image=CONFIG.BOWER.BUILDER_TAG):
    """Build bower library image."""
    build_library_image(tag, **bower_builder_kwargs(image))


@task(check=FileHash('bower.json'),
      depends=[build_bower_builder],
      parent='build_docker_volumes')
def build_bower_volume():
    """Build bower library volume."""
    build_library_volumes(**bower_builder_kwargs())


@task(depends=[build_bower_builder])
def bower_builder_shell(image=CONFIG.BOWER.BUILDER_TAG):
    """
    open a bash shell in the bower builder with volumes mounted. This allows
    for manually running bower commands.
    """
    run_builder(command='/bin/bash', **bower_builder_kwargs(image))

