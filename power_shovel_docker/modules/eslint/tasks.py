from power_shovel.config import CONFIG
from power_shovel import task
from power_shovel_docker.modules.docker.tasks import compose
from power_shovel_docker.modules.npm.tasks import build_npm


ESLINT_DEPENDS = [build_npm]


@task(
    category='testing',
    short_description='Run all linting tasks',
    depends=[ESLINT_DEPENDS]
)
def lint():
    """Virtual target for linting."""


@task(
    category='testing',
    short_description='Run all javascript linting tasks'
)
def lint_js():
    """Virtual target for linting javascript."""


@task(
    category='testing',
    depends=ESLINT_DEPENDS,
    parent=['lint', 'lint_js'],
    short_description='ESLint javascript linter'
)
def eslint(*args):
    """
    ESLint javascript linter.

    This is a proxy to the ESLint linter. This task uses `compose` to run the
    linter within the app container. Arguments are passed through to the

    For ESLint help type: shovel eslint --help
    """
    formatted_args = ' '.join(args)
    command = CONFIG.format(
        '{ESLINT.BIN} {args} {DOCKER.PROJECT_DIR}',
        args=formatted_args
    )
    return compose(command)
