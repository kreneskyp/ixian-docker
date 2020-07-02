# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from pysnap import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestDockerConfig.test_read[APP_BIN] 1'] = '/opt/unittests/bin'

snapshots['TestDockerConfig.test_read[APP_DIR] 1'] = '/opt/unittests'

snapshots['TestDockerConfig.test_read[BASE_IMAGE] 1'] = 'docker.io/library/unittests:base-ce1b44591b99c65d60dd3b7f2619794d4134f376a4436c3e05973e3eee4cceb1'

snapshots['TestDockerConfig.test_read[BASE_IMAGE_FILES] 1'] = [
    '{PWD}/root/{PROJECT_NAME}/bin/',
    '{PWD}/root/{PROJECT_NAME}/etc/base'
]

snapshots['TestDockerConfig.test_read[BASE_IMAGE_TAG] 1'] = 'base-ce1b44591b99c65d60dd3b7f2619794d4134f376a4436c3e05973e3eee4cceb1'

snapshots['TestDockerConfig.test_read[COMPOSE_FLAGS] 1'] = [
    '--rm',
    '-u root'
]

snapshots['TestDockerConfig.test_read[DEFAULT_APP] 1'] = 'app'

snapshots['TestDockerConfig.test_read[DEV_VOLUMES] 1'] = [
    '{PWD}:{DOCKER.PROJECT_DIR}',
    '{BUILDER}/.bash_history:{DOCKER.HOME_DIR}/.bash_history',
    '{PWD}/bin/:{DOCKER.APP_DIR}/bin',
    '{PWD}/.env:{DOCKER.APP_DIR}/.env'
]

snapshots['TestDockerConfig.test_read[DEV_ENV] 1'] = {
}

snapshots['TestDockerConfig.test_read[DOCKERFILE] 1'] = 'Dockerfile'

snapshots['TestDockerConfig.test_read[DOCKERFILE_BASE] 1'] = 'Dockerfile.base'

snapshots['TestDockerConfig.test_read[ENV] 1'] = {
}

snapshots['TestDockerConfig.test_read[ENV_DIR] 1'] = '/opt'

snapshots['TestDockerConfig.test_read[HOME_DIR] 1'] = '/root'

snapshots['TestDockerConfig.test_read[IMAGE_TAG] 1'] = 'runtime-d321d9a5fae7d090947f7111963ef3a2075b473f667df8bb1a37b14b9a9f476b'

snapshots['TestDockerConfig.test_read[MODULE_CONTEXT] 1'] = '.builder/module_context'

snapshots['TestDockerConfig.test_read[MODULE_DIR] 1'] = '/home/runner/work/ixian-docker/ixian-docker/ixian_docker/modules/docker'

snapshots['TestDockerConfig.test_read[REGISTRY] 1'] = 'docker.io'

snapshots['TestDockerConfig.test_read[REGISTRY_PATH] 1'] = 'library'

snapshots['TestDockerConfig.test_read[REPOSITORY] 1'] = 'docker.io/library/unittests'

snapshots['TestDockerConfig.test_read[ROOT_MODULE_DIR] 1'] = '/home/runner/work/ixian-docker/ixian-docker/ixian_docker'

snapshots['TestDockerConfig.test_read[VOLUMES] 1'] = [
]

snapshots['TestDockerConfig.test_read[IMAGE] 1'] = 'docker.io/library/unittests:runtime-d321d9a5fae7d090947f7111963ef3a2075b473f667df8bb1a37b14b9a9f476b'

snapshots['TestDockerConfig.test_task_hash 1'] = GenericRepr('<ixian.config.TaskConfig object at 0x100000000>')

snapshots['TestDockerConfig.test_task_hash 2'] = GenericRepr('<ixian.config.TaskConfig object at 0x100000000>')

snapshots['TestDockerConfig.test_read[DOCKER_IO] 1'] = 'docker.io'

snapshots['TestDockerConfig.test_read[COMPOSE_ENV] 1'] = {
}
