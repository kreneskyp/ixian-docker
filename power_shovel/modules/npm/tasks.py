from power_shovel.config import CONFIG
from power_shovel.modules.docker.checker import DockerVolumeExists
from power_shovel.modules.docker.checker import DockerImageExists
from power_shovel.modules.filesystem.file_hash import FileHash
from power_shovel.modules.docker.utils import build_image
from power_shovel.modules.docker.utils import build_library_image
from power_shovel.modules.docker.utils import build_volume_from_image
from power_shovel.modules.docker.utils import run_builder
from power_shovel.modules.filesystem.utils import touch, mkdir
from power_shovel.modules.npm.utils import npm_local_package_mount_flags
from power_shovel.task import task


@task()
def build_npm_builder():
    """
    Build a builder for installing npm packages. The default Dockerfile
    includes includes NodeJS, npm, update tools.
    :return:
    """
    # TODO node version selection
    build_image(CONFIG.NPM.BUILDER_TAG,
                CONFIG.NPM.BUILDER_DOCKERFILE,
                context=CONFIG.NPM.BUILDER_CONTEXT)


def npm_builder_kwargs(image=CONFIG.NPM.BUILDER_TAG):
    volumes = [
        '{PWD}/package.json:{DOCKER.APP_DIR}/package.json',
        #'{BUILDER}/npm.bash_history:{DOCKER.HOME_DIR}/.bash_history'
    ]
    local_package_volumes = npm_local_package_mount_flags()
    if local_package_volumes:
        # handle local packages
        volumes.extend(local_package_volumes)

    # TODO mounting volume like this was breaking the build. looked like
    # it was mounting as a directory instead of a file.
    # volumes.append('{PWD}/package.json:{builder}/package-lock.json')

    return dict(
        image=image,
        outputs=[
            'node_modules',
            '.npm'
        ],
        volumes=volumes)


@task(checker=FileHash('package.json'))
def build_npm_image(tag='npm', image=CONFIG.NPM.BUILDER_TAG):
    """
    Build an image with packages installed via npm.

    This function handles local dependencies automatically. When present all
    packages listed with a path (e.g. file:/path/to/package) are mapped as
    volumes.  A temp package.json with rewritten paths is used to install them
    from their mountpoints.
    :param tag:
    :return:
    """
    build_library_image(tag, **npm_builder_kwargs(image))


@task(checker=DockerVolumeExists(CONFIG.NPM.BUILDER_TAG))
def build_npm_volume(tag=CONFIG.NPM.BUILDER_TAG,
                     image=CONFIG.NPM.BUILDER_TAG):
    """
    Build the npm volume from the library image.
    :param tag: tag for volume, defaults to CONFIG.NPM_BUILDER_TAG.
    :param image: image tag, defaults to CONFIG.NPM_BUILDER_TAG.
    """
    build_volume_from_image(image, '/builder/node_modules', tag)


@task()
def npm_builder_shell(tag='npm', image=CONFIG.NPM.BUILDER_TAG):
    """
    open a bash shell in the npm builder with volumes mounted. This allows for
    manually running npm commands.
    """
    run_builder(command='/bin/bash', **npm_builder_kwargs(image))


@task()
def npm_update(image=CONFIG.NPM.BUILDER_TAG):
    """
    open a bash shell in the npm builder with volumes mounted. This allows for
    manually running npm commands.
    """
    run_builder(command='ncu -u', **npm_builder_kwargs(image))
