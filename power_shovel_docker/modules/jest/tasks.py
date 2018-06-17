from power_shovel.config import CONFIG
from power_shovel import task
from power_shovel_docker.modules.docker.tasks import compose
from power_shovel_docker.modules.npm.tasks import build_npm


@task(parent='test_js', depends=[build_npm], auto_help=False)
def jest(*args):
    command = CONFIG.format('{JEST.BIN} --config={JEST.CONFIG_FILE_PATH}')
    compose(command, *args)


@task(depends=[build_npm])
def jest_update(*args):
    command = CONFIG.format('{JEST.BIN} -u --config={JEST.CONFIG_FILE_PATH}')
    compose(command, *args)
