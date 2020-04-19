from power_shovel.config import CONFIG
from power_shovel.task import Task, VirtualTarget
from power_shovel_docker.modules.docker.tasks import compose


BLACK_DEPENDS = ["compose_runtime"]


class LintPython(VirtualTarget):
    """Virtual target for testing javascript"""

    name = "lint_py"
    parent = "lint"
    category = "testing"
    short_description = "Run all python linting tasks"


class Black(Task):
    """
    Black python formatter.

    This task is a proxy to the Black python formatter. It uses `compose`
    to execute jest within the context of the app container.

    Other arguments and flags are passed through to black.

    For Black help type: shovel black --help
    """

    name = "black"
    category = "testing"
    depends = BLACK_DEPENDS
    short_description = "Black python formatter."

    def execute(self, *args):
        args = args or CONFIG.BLACK.ARGS
        return compose("black", args)


class BlackCheck(Task):
    """
    Verify python code has been formatted with Black
    """

    name = "black_check"
    category = "testing"
    parent = ["lint", "lint_py"]
    depends = BLACK_DEPENDS
    short_description = "Black lint check."

    def execute(self, *args):
        args = args or CONFIG.BLACK.ARGS
        return compose("black", ["--check", *args])
