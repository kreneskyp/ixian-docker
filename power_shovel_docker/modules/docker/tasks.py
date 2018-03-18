from power_shovel import task
from power_shovel.config import CONFIG
from power_shovel.utils.process import execute
from power_shovel_docker.modules.docker.utils import convert_volume_flags


@task()
def compose(*args, **kwargs):
    """
    Docker compose run a command in `app`
    :param args:
    :param kwargs:
    :return:
    """

    # TODO process kwargs
    args_str = ' '.join(args)

    # convert volume configs provided by modules into flags to pass to compose
    volumes = ' '.join(convert_volume_flags(
        CONFIG.DOCKER.DEV_VOLUMES +
        CONFIG.DOCKER.VOLUMES))

    # TODO --service-ports only for runserver
    execute(CONFIG.format(
        'docker-compose run {volumes} '
        '-e APP_DIR={DOCKER.APP_DIR} '
        '-e ROOT_MODULE_PATH={PYTHON.ROOT_MODULE_PATH} '
        ' --rm app {args}',
        args=args_str,
        volumes=volumes
    ))


# =============================================================================
#  Container modules
# =============================================================================


@task()
def bash(*args):
    """Open a bash shell in container"""
    compose('/bin/bash')


@task()
def up():
    """Start app in test-container"""
    compose('up -d app')


@task()
def down():
    compose('down')


# =============================================================================
#  Cleanup
# =============================================================================

def docker_full_teardown():
    # TODO this doesn't work yet because can't pipe modules
    # TODO split these into individual tasks kill_containers|clean_containers|clean_images
    # TODO add clean_volumes
    # TODO --force should be passed to docker commands where appropriate.
    execute("docker ps -q | xargs docker kill")
    execute("docker ps -q -a | xargs docker rm -v")
    execute("docker images -q | xargs docker rmi")

