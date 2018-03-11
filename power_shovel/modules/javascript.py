from power_shovel.task import task
from power_shovel.modules.filesystem.utils import pwd
from power_shovel.utils.process import execute
from power_shovel.config import CONFIG


# TODO this isn't working, has an issue resolving base config
@task()
def lint_js():
    # TODO update this to use a helper to add volumes
    execute(('docker run --rm -i ' +
             '-v {PWD}:{DOCKER.APP_DIR} ' +
             '-v {PWD}/.node_modules:{DOCKER.APP_DIR}/node_modules ' +
             'builder.npm ' +
             '{DOCKER.APP_DIR}/node_modules/.bin/eslint ' +
             '{DOCKER.APP_DIR}'
             ).format(
                pwd=pwd(),
                app_env_dir=CONFIG.DOCKER.APP_DIR
            ))


@task()
def test_js():
    # TODO update this to use a helper to add volumes
    execute(('docker run --rm -i ' +
             '-v {PWD}:{DOCKER.APP_DIR} ' +
             '-v {PWD}/.node_modules:{DOCKER.APP_DIR}/node_modules ' +
             '-w {DOCKER.APP_DIR} ' +
             'builder.npm ' +
             '{DOCKER.APP_DIR}/node_modules/.bin/jest ' +
             '--config={DOCKER.APP_DIR}/jest.config.json'
             ).format(
                pwd=pwd(),
                app_env_dir=CONFIG.DOCKER.APP_DIR
            ))
