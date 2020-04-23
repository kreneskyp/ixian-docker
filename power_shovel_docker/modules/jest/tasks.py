from power_shovel.config import CONFIG
from power_shovel.task import Task, VirtualTarget
from power_shovel_docker.modules.docker.tasks import run


JEST_DEPENDS = ["compose_runtime"]


class TestJS(VirtualTarget):
    """Virtual target for testing javascript"""

    name = "test_js"
    category = "testing"
    short_description = "Run all javascript testing tasks"


class Jest(Task):
    """
    Jest javascript test runner.

    This task is a proxy to the Jest javascript test runner. It uses `compose`
    to execute jest within the context of the app container.

    Configuration is configured by default as:
        --config={JEST.CONFIG_FILE_PATH}

    Other arguments and flags are passed through to jest.

    For Jest help type: shovel jest --help
    """

    name = "jest"
    category = "testing"
    depends = JEST_DEPENDS
    parent = ["test", "test_js"]
    short_description = "Jest javascript test runner."

    def execute(self, *args):
        command = CONFIG.format("{JEST.BIN} --config={JEST.CONFIG_FILE_PATH}")
        return run(command, args)
