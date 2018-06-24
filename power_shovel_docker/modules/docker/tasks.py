from power_shovel import logger
from power_shovel import task
from power_shovel.config import CONFIG
from power_shovel.modules.filesystem.file_hash import FileHash
from power_shovel.utils.process import execute
from power_shovel_docker.modules.docker.utils import build_image
from power_shovel_docker.modules.docker.utils import convert_volume_flags
from power_shovel_docker.modules.docker import utils


@task(
    category='build',
    check=FileHash(
        '{POWER_SHOVEL}',
        '{DOCKER.ROOT_MODULE_DIR}'
    ),
    short_description='build app\'s dockerfile',
)
def build_dockerfile():
    """
    Build dockerfile from configured modules and settings.

    This compiles a dockerfile based on the settings for the project. Each
    module may provide a jinja template snippet. The snippets are passed to
    a base template that renders them.

    The base template is read from {{DOCKER.DOCKERFILE_TEMPLATE}}. The base
    template is passed CONFIG and MODULES in the context.

    Each module may have template snippet to include.

    The compiled Dockerfile is written to {{CONFIG.DOCKER.DOCKER_FILE}}.

    Config:
        - DOCKER.DOCKERFILE_TEMPLATE:  Jinja2 base template.
        - DOCKER.DOCKER_FILE:          Dockerfile output.
    """
    text = utils.build_dockerfile()
    with open(CONFIG.DOCKER.DOCKER_FILE, 'w') as dockerfile:
        dockerfile.write(text)


def remove_app_image():
    try:
        image = docker_client().images.get(CONFIG.DOCKER.APP_IMAGE)
    except docker.errors.NotFound:
        pass
    else:
        image.remove(True)


@task(
    category='build',
    short_description='Virtual target for building app'
)
def build_app():
    """
    Runs all build steps for the app. Other modules should target this task as
    their parent.
    """


@task(
    category='build',
    depends=[build_dockerfile],
    check=FileHash(
        'Dockerfile'
    ),
    parent='build_app',
    clean=remove_app_image,
    short_description='Build app image',
)
def build_app_image():
    """Builds the docker app image using CONFIG.DOCKER_FILE"""
    build_image(CONFIG.DOCKER.APP_IMAGE, CONFIG.DOCKER.DOCKER_FILE)


@task(
    category='docker',
    short_description='Docker compose command'
)
def compose(
    command=None,
    app=None,
    flags=None,
    env=None,
    volumes=None
):
    """
    Docker compose run a command in `app`
    :param command: command and args as single string.
    :param app: docker-compose app to run, default is {DOCKER.DEFAULT_APP}
    :param flags: docker-compose flags
    :param env: ENV variables to set.
    :param volumes: volumes to set.
    :return:
    """
    app = app or CONFIG.DOCKER.DEFAULT_APP
    volumes = convert_volume_flags(
        CONFIG.DOCKER.DEV_VOLUMES +
        CONFIG.DOCKER.VOLUMES +
        (volumes or [])
    )
    env_ = {
        'APP_DIR': CONFIG.DOCKER.APP_DIR,
        'ROOT_MODULE_PATH': CONFIG.PYTHON.ROOT_MODULE_PATH
    }
    env_.update(env or {})
    formatted_env = [
        '-e {key}={value}'.format(key=k, value=v) for k, v in env_.items()
    ]
    flags = flags or ['--rm']

    template = (
        'docker-compose run{CR} {flags} {volumes} {env} {app} {command}'
    )

    def render_command():
        with_cr = '{} \\\n'
        formatted = template.format(
            CR=' \\\n',
            app=app,
            command=command or '',
            env=' '.join((with_cr.format(line) for line in formatted_env)),
            flags=' '.join((with_cr.format(line) for line in flags)),
            volumes=' '.join((with_cr.format(line) for line in volumes))
        )
        logger.info(CONFIG.format(formatted))

    render_command()
    execute(template.format(
        CR='',
        app=app,
        command=command or '',
        env=' '.join(formatted_env),
        flags=' '.join(flags),
        volumes=' '.join(volumes)
    ), silent=True)


# =============================================================================
#  Container modules
# =============================================================================


@task(
    category='Docker',
    short_description='Bash shell in docker container'
)
def bash(*args):
    """Open a bash shell in container"""
    compose('/bin/bash', *args)


@task(
    category='Docker',
    short_description='Start docker container'
)
def up():
    """Start app container"""
    compose('up -d app')


@task(
    category='Docker',
    short_description='Stop docker container'
)
def down():
    """Stop app container"""
    compose('down')


# =============================================================================
#  Cleanup
# =============================================================================


def docker_full_teardown():
    # TODO this doesn't work yet because can't pipe commands
    # TODO split these into individual tasks kill_containers|clean_containers|clean_images
    # TODO add clean_volumes
    # TODO --force should be passed to docker commands where appropriate.
    execute("docker ps -q | xargs docker kill")
    execute("docker ps -q -a | xargs docker rm -v")
    execute("docker images -q | xargs docker rmi")

