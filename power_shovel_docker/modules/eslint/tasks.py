from power_shovel.config import CONFIG
from power_shovel import Task, VirtualTarget
from power_shovel_docker.modules.docker.tasks import compose


ESLINT_DEPENDS = ['build_npm']


class lint(VirtualTarget):
    """Virtual target for linting."""
    name = 'lint'
    category = 'testing'
    short_description = 'Run all linting tasks',


class lint_js(VirtualTarget):
    """Virtual target for linting javascript."""
    name = 'lint_js'
    category = 'testing'
    short_description = 'Run all javascript linting tasks'


class ESLint(Task):
    """
    ESLint javascript linter.

    This is a proxy to the ESLint linter. This task uses `compose` to run the
    linter within the app container. Arguments are passed through to the

    For ESLint help type: shovel eslint --help
    """

    name = 'eslint'
    category = 'testing'
    depends = ESLINT_DEPENDS
    parent = ['lint', 'lint_js']
    short_description = 'ESLint javascript linter'

    def execute(self, *args):
        formatted_args = ' '.join(args)
        command = CONFIG.format(
            '{ESLINT.BIN} {args} {DOCKER.PROJECT_DIR}',
            args=formatted_args
        )
        return compose(command)
