from power_shovel.config import CONFIG
from power_shovel.modules.filesystem.file_hash import FileHash
from power_shovel.task import task
from power_shovel_docker.modules.docker.checker import DockerImageExists
from power_shovel_docker.modules.docker.utils import build_image
from power_shovel_docker.modules.docker.utils import build_library_volumes
from power_shovel_docker.modules.docker.utils import build_library_image
from power_shovel_docker.modules.docker.utils import run_builder


def python_local_package_mount_flags():
    return []


@task()
def delete_python_builder():
    print(CONFIG.FORMAT('TODO: delete image "{PYTHON.BUILDER_TAG}"'))


@task(
    check=[
        FileHash('{PYTHON.MODULE_DIR}'),
        DockerImageExists('{PYTHON.BUILDER_TAG}')
    ],
    clean=delete_python_builder
)
def build_python_builder():
    """
    Build a builder for installing python packages. The default Dockerfile
    includes includes python runtime, pip, and pip-updater.
    :return:
    """
    # TODO node version selection
    build_image(CONFIG.PYTHON.BUILDER_TAG,
                CONFIG.PYTHON.BUILDER_DOCKERFILE,
                context=CONFIG.PYTHON.BUILDER_CONTEXT)


def python_builder_kwargs(image=CONFIG.PYTHON.BUILDER_TAG, dev=False):
    """Update all packages installed by pip"""
    volumes = [
        # TODO switch away from requirements file
        '{PWD}/requirements.txt:{DOCKER.APP_DIR}/requirements.txt',
        # TODO Pipfile.lock causes problems when starting a new project. There are parse
        # errors with an empty file.  Need some way of initializing it.
        #'{PWD}/Pipfile.lock:{DOCKER.APP_DIR}/Pipfile.lock',
        '{PWD}/Pipfile:{DOCKER.APP_DIR}/Pipfile',
        '{BUILDER}/python.bash_history:{DOCKER.HOME_DIR}/.bash_history'
    ]

    if dev:
        volumes.append(
            '{PWD}/requirements.txt:{DOCKER.APP_DIR}/requirements.dev.txt')

    local_package_volumes = python_local_package_mount_flags()
    if local_package_volumes:
        # handle local packages
        volumes.extend(local_package_volumes)

    return dict(
        image=image,
        volumes=volumes)


@task(parent='build_docker_images',
      check=FileHash('requirements.txt', 'Pipfile'),
      depends=[build_python_builder])
def build_python_image(
        tag=CONFIG.PYTHON.TAG,
        image=CONFIG.PYTHON.BUILDER_TAG,
        dev=False
):
    """Update all packages installed by pip"""
    build_library_image(tag, **python_builder_kwargs(image, dev))


@task(parent='build_docker_volumes',
      check=FileHash('requirements.txt'),
      depends=[build_python_builder])
def build_python_volume(image=CONFIG.PYTHON.BUILDER_TAG):
    build_library_volumes(
        outputs=CONFIG.PYTHON.OUTPUTS[0],
        **python_builder_kwargs(image))


@task(depends=[build_python_volume])
def python_builder_shell(image=CONFIG.PYTHON.BUILDER_TAG):
    """
    open a bash shell in the webpack builder with volumes mounted. This allows
    for manually running webpack commands.
    """
    run_builder(
        command='/bin/bash',
        outputs=CONFIG.PYTHON.OUTPUTS[0],
        **python_builder_kwargs(image))


@task(depends=[build_python_volume])
def pipenv(*args, **kwargs):
    """
    Run a pipenv command.

    This runs in the builder container with volumes mounted.
    """
    image = CONFIG.PYTHON.BUILDER_TAG
    args_str = ' '.join(args)
    run_builder(
        command='pipenv %s' % args_str,
        outputs=CONFIG.PYTHON.OUTPUTS[0],
        **python_builder_kwargs(image))
