from power_shovel.config import CONFIG
from power_shovel import task
from power_shovel_docker.modules.docker.tasks import compose
from power_shovel_docker.modules.npm.tasks import build_npm


@task(depends=[build_npm])
def test_js():
    command = CONFIG.format('{JEST.BIN} --config={JEST.CONFIG_FILE_PATH}')
    compose(command)
