from power_shovel.config import CONFIG
from power_shovel.task import Task, VirtualTarget
from power_shovel_docker.modules.docker.tasks import run


PRETTIER_DEPENDS = ["compose_runtime"]


class LintJS(VirtualTarget):
    """Virtual target for linting javascript"""

    name = "lint_js"
    parent = "lint"
    category = "testing"
    short_description = "Run all javascript linting tasks"


class Prettier(Task):
    """
    Prettier javascript formatter.

    This task is a proxy to the Prettier python formatter. It uses `compose`
    to execute prettier within the context of the app container.

    Other arguments and flags are passed through to prettier.

    For Prettier help type: shovel prettier --help
    """

    name = "prettier"
    category = "testing"
    depends = PRETTIER_DEPENDS
    short_description = "Black python formatter."

    def execute(self, *args):
        args = args or [
            "--write",
            "--list-different",
            "--color",
            "{PRETTIER.SRC}/**/*.js",
        ]
        return run("{PRETTIER.BIN}", args)


class PrettierCheck(Task):
    """
    Verify javascript code has been formatted with Prettier
    """

    name = "prettier_check"
    category = "testing"
    parent = ["lint", "lint_js"]
    depends = PRETTIER_DEPENDS
    short_description = "Prettier javascript lint check."

    def execute(self, *args):
        args = args or [
            "--check",
            "--color",
            "{PRETTIER.SRC}/**/*.js",
        ]
        return run("{PRETTIER.BIN}", args)
