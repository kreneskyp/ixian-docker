from ixian.config import CONFIG
from ixian.task import Task
from ixian_docker.modules.docker.tasks import run


PYTEST_DEPENDS = ["compose_runtime"]


class Pytest(Task):
    """
    Pytest python test runner.

    This task is a proxy to the Pytest python test runner. It uses `compose`
    to execute Pytest within the context of the app container.

    Other arguments and flags are passed through to Pytest.

    For Pytest help type: ix pytest --help
    """

    name = "pytest"
    category = "testing"
    depends = PYTEST_DEPENDS
    short_description = "Pytest test runner."

    def execute(self, *args):
        args = [*CONFIG.PYTEST.ARGS, *args]
        print("args: ", args)
        return run("pytest", args)
