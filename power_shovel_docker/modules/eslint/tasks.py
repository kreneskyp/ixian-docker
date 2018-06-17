from power_shovel.config import CONFIG
from power_shovel import task
from power_shovel_docker.modules.docker.tasks import compose
from power_shovel_docker.modules.npm.tasks import build_npm


@task(parent=['lint_js', 'lint'], depends=[build_npm], auto_help=False)
def eslint(*args):
    formatted_args = ' '.join(args)
    command = CONFIG.format(
        '{ESLINT.BIN} {args} {DOCKER.PROJECT_DIR}',
        args=formatted_args
    )
    compose(command)
