from power_shovel.config import CONFIG
from power_shovel import task
from power_shovel_docker.modules.docker.tasks import compose
from power_shovel_docker.modules.npm.tasks import build_npm


JEST_DEPENDS = [build_npm]


@task(
    category='testing',
    short_description='Run all javascript testing tasks',
    depends=[JEST_DEPENDS]
)
def test_js():
    """Virtual target for testing javascript"""


@task(
    category='testing',
    depends=JEST_DEPENDS,
    parent=['test', 'test_js'],
    short_description='Jest javascript test runner.'
)
def jest(*args):
    """
    Jest javascript test runner.

    This task is a proxy to the Jest javascript test runner. It uses `compose`
    to execute jest within the context of the app container.

    Configuration is configured by default as:
        --config={JEST.CONFIG_FILE_PATH}

    Other arguments and flags are passed through to jest.

    For Jest help type: shovel jest --help
    """
    command = CONFIG.format('{JEST.BIN} --config={JEST.CONFIG_FILE_PATH}')
    compose(command, *args)
