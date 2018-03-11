from power_shovel import task
from power_shovel.modules.docker.utils import build_image
from power_shovel.modules.docker.utils import run_builder
from power_shovel.modules.docker.utils import build_volume_from_image
from power_shovel.modules.docker.utils import build_library_image
from power_shovel.modules.npm.utils import npm_local_package_mount_flags
from power_shovel.config import CONFIG


@task()
def build_bower_builder():
    build_image(CONFIG.BOWER.BUILDER_TAG,
                CONFIG.BOWER.BUILDER_DOCKERFILE,
                context=CONFIG.BOWER.BUILDER_CONTEXT)


def bower_builder_kwargs(image=CONFIG.BOWER.BUILDER_TAG):
    volumes = [
        '{PWD}:{DOCKER.PROJECT_DIR}',
        # TODO : volume names shouldn't be defined here
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


@task()
def build_bower_image(tag='bower', image=CONFIG.BOWER.BUILDER_TAG):
    build_library_image(tag, **bower_builder_kwargs(image))


@task()
def build_bower_volume(tag='bower'):
    build_bower_image(tag)
    build_volume_from_image(
        'bower', CONFIG.BOWER.MODULES_DIR, 'bower')


@task()
def bower_builder_shell(image=CONFIG.BOWER.BUILDER_TAG):
    """
    open a bash shell in the bower builder with volumes mounted. This allows
    for manually running bower commands.
    """
    run_builder(command='/bin/bash', **bower_builder_kwargs(image))

