import docker
from power_shovel import logger
from power_shovel.task import Task, VirtualTarget
from power_shovel.config import CONFIG
from power_shovel.modules.filesystem.file_hash import FileHash
from power_shovel.utils.process import execute
from power_shovel_docker.modules.docker.checker import DockerImageExists
from power_shovel_docker.modules.docker.utils.images import (
    build_image_if_needed,
    pull_image,
    push_image,
)
from power_shovel_docker.modules.docker.utils.client import docker_client
from power_shovel_docker.modules.docker import utils


class CleanDocker(Task):
    """
    Clean Docker:
        - kill and remove all containers
    """

    name = "clean_docker"
    category = "docker"

    def execute(self):
        execute("docker-compose kill")
        execute("docker-compose rm -f -v")


class BuildDockerfile(Task):
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

    name = "build_dockerfile"
    category = "build"
    check = FileHash("{POWER_SHOVEL}", "shovel.py")
    short_description = "build app's dockerfile"

    def execute(self):
        text = utils.build_dockerfile()
        with open(CONFIG.DOCKER.DOCKER_FILE, "w") as dockerfile:
            dockerfile.write(text)


def remove_app_image():
    try:
        image = docker_client().images.get(CONFIG.DOCKER.APP_IMAGE)
    except docker.errors.NotFound:
        pass
    else:
        image.remove(True)


class BuildApp(VirtualTarget):
    """
    Runs all build steps for the app. Other modules should target this task as
    their parent.
    """

    name = "build_app"
    category = "build"
    short_description = "Virtual target for building app"


class BuildAppImage(Task):
    """Builds the docker app image using CONFIG.DOCKER_FILE"""

    name = "build_app_image"
    depends = ["build_base_image"]
    category = "build"
    check = [FileHash("Dockerfile",), DockerImageExists("{DOCKER.APP_IMAGE_FULL}")]
    clean = remove_app_image
    short_description = "Build app image"

    def execute(self, pull=True):
        build_image_if_needed(
            repository=CONFIG.DOCKER.REPOSITORY,
            tag=CONFIG.DOCKER.IMAGE_TAG,
            file=CONFIG.DOCKER.DOCKERFILE,
            force=self.__task__.force,
            pull=pull,
            recheck=self.check.check,
            args={
                "PYTHON_IMAGE": CONFIG.PYTHON.IMAGE,
                "COMPILED_STATIC_IMAGE": CONFIG.WEBPACK.IMAGE,
                "BOWER_IMAGE": CONFIG.BOWER.IMAGE,
            },
        )


class BuildBaseImage(Task):
    """Builds the docker app image using CONFIG.DOCKER_FILE"""

    name = "build_base_image"
    category = "build"
    parent = "build_image"
    check = [
        FileHash(
            "{DOCKER.DOCKERFILE_BASE}",
            # TODO: FileHash should recursively expand and format list values
            # *CONFIG.format('{DOCKER.BASE_IMAGE_FILES}')
        ),
        DockerImageExists("{DOCKER.BASE_IMAGE}"),
    ]
    clean = remove_app_image
    short_description = "Build app image"

    def execute(self, pull=True):
        build_image_if_needed(
            repository=CONFIG.DOCKER.REPOSITORY,
            tag=CONFIG.DOCKER.BASE_IMAGE_TAG,
            file=CONFIG.DOCKER.DOCKERFILE_BASE,
            force=self.__task__.force,
            pull=pull,
            recheck=self.check.check)


class PullImage(Task):
    """
    Pull the Image as specified by {DOCKER.IMAGE}
    """

    name = "pull"
    short_description = "Pull the image"

    def execute(self):
        pull_image(CONFIG.DOCKER.IMAGE)


class PushImage(Task):
    """
    Push the Image as specified by {DOCKER.IMAGE}
    """

    name = "push"
    short_description = "Push the image"

    def execute(self):
        push_image(CONFIG.DOCKER.IMAGE)


# TODO: TaskRunner/Shim doesn't support multiple args or kwargs. fix that.
class Compose(Task):
    """
    Docker compose run a command in `app`

    :param command: command and args as single string.
    :param app: docker-compose app to run, default is {DOCKER.DEFAULT_APP}
    :param flags: docker-compose flags
    :param env: ENV variables to set.
    :param volumes: volumes to set.
    :return:
    """

    name = "compose"
    category = "docker"
    short_description = "Docker compose command"

    def execute(self, command=None, *args, **kwargs):
        app = kwargs.get("app", CONFIG.DOCKER.DEFAULT_APP)
        # volumes = convert_volume_flags(
        #    CONFIG.DOCKER.DEV_VOLUMES +
        #    CONFIG.DOCKER.VOLUMES +
        #    kwargs.get('volumes', [])
        # )
        env = {
            "APP_DIR": CONFIG.DOCKER.APP_DIR,
            "ROOT_MODULE_PATH": CONFIG.PYTHON.ROOT_MODULE_PATH,
        }
        env.update(kwargs.get("env", {}))
        formatted_env = [
            "-e {key}={value}".format(key=k, value=v) for k, v in env.items()
        ]
        flags = CONFIG.DOCKER.COMPOSE_FLAGS + kwargs.get("flags", [])
        formatted_args = [CONFIG.format(arg) for arg in args or []]

        template = (
            "docker-compose run{CR} {flags} {volumes} {env} {app} {command} {args}"
        )

        def render_command():
            with_cr = "{} \\\n"
            formatted = template.format(
                CR=" \\\n",
                app=app,
                args=" ".join(formatted_args),
                command=CONFIG.format(command or ""),
                env=" ".join((with_cr.format(line) for line in formatted_env)),
                flags=" ".join((with_cr.format(line) for line in flags)),
                volumes=" ".join((with_cr.format(line) for line in volumes)),
                image=CONFIG.DOCKER.APP_IMAGE,
            )
            logger.info(CONFIG.format(formatted))

        render_command()
        return execute(
            template.format(
                CR="",
                app=app,
                args=" ".join(formatted_args),
                command=command or "",
                env=" ".join(formatted_env),
                flags=" ".join(flags),
                volumes=" ".join(volumes),
            ),
            silent=True,
        )


def compose(*args, **kwargs):
    return Compose()(*args, **kwargs)


# =============================================================================
#  Container modules
# =============================================================================


class Bash(Task):
    """Open a bash shell in container"""

    name = "bash"
    category = "Docker"
    short_description = "Bash shell in docker container"

    def execute(self, *args):
        return compose("/bin/bash", *args)


class Up(Task):
    """Start app container"""

    name = "up"
    category = "Docker"
    short_description = "Start docker container"

    def execute(self):
        return compose("up -d app")


class Down(Task):
    """Stop app container"""

    name = "task"
    category = "Docker"
    short_description = "Stop docker container"

    def execute(self):
        return compose("down")


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
