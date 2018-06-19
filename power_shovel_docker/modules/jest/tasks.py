from power_shovel.config import CONFIG
from power_shovel import task
from power_shovel_docker.modules.docker.tasks import compose
from power_shovel_docker.modules.npm.tasks import build_npm


@task(
    category='testing',
    short_description='Run all test tasks'
)
def test():
    """Virtual target for testing"""


@task(
    category='testing',
    short_description='Run all javascript testing tasks'
)
def test_js():
    """Virtual target for testing javascript"""


@task(
    category='testing',
    depends=[build_npm],
    parent=['test', 'test_js'],
    short_description='Jest javascript tests'
)
def jest(*args):
    command = CONFIG.format('{JEST.BIN} --config={JEST.CONFIG_FILE_PATH}')
    compose(command, *args)
