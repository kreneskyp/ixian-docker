from ixian.config import CONFIG
from ixian.task import Task, VirtualTarget
from ixian_docker.modules.docker.tasks import run


ESLINT_DEPENDS = ["build_npm"]


class Lint(VirtualTarget):
    """Virtual target for linting."""

    name = "lint"
    category = "testing"
    short_description = "Run all linting tasks"


class lint_js(VirtualTarget):
    """Virtual target for linting javascript."""

    name = "lint_js"
    category = "testing"
    short_description = "Run all javascript linting tasks"


class ESLint(Task):
    """
    ESLint javascript linter.

    This is a proxy to the ESLint linter. This task uses `compose` to run the
    linter within the app container. Arguments are passed through to the

    For ESLint help type: ix eslint --help
    """

    name = "eslint"
    category = "testing"
    depends = ESLINT_DEPENDS
    parent = ["lint", "lint_js"]
    short_description = "ESLint javascript linter"

    def execute(self, *args):
        formatted_args = " ".join(args)
        command = CONFIG.format(
            "{ESLINT.BIN} {args} {DOCKER.PROJECT_DIR}", args=formatted_args
        )
        return run(command)
