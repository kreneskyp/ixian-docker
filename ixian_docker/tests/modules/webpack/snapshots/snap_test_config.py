# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from pysnap import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestConfig.test_read[ARGS] 1'] = [
    '--colors',
    '--config {WEBPACK.CONFIG_FILE_PATH}',
    '--output-path {WEBPACK.COMPILED_STATIC_DIR}'
]

snapshots['TestConfig.test_read[COMPILED_STATIC_DIR] 1'] = '/opt/unittests/compiled_static'

snapshots['TestConfig.test_read[CONFIG_FILE] 1'] = 'webpack.config.js'

snapshots['TestConfig.test_read[CONFIG_FILE_PATH] 1'] = '/opt/unittests/etc/webpack/webpack.config.js'

snapshots['TestConfig.test_read[DOCKERFILE] 1'] = '/opt/ixian_docker/ixian_docker/modules/webpack/Dockerfile.jinja'

snapshots['TestConfig.test_read[IMAGE] 1'] = 'docker.io/library/unittests:webpack-a7bc1648c83be24389351892a12fe3adef2e55bc843fb8e29350f28a06369676'

snapshots['TestConfig.test_read[IMAGE_TAG] 1'] = 'webpack-a7bc1648c83be24389351892a12fe3adef2e55bc843fb8e29350f28a06369676'

snapshots['TestConfig.test_read[MODULE_DIR] 1'] = '/opt/ixian_docker/ixian_docker/modules/webpack'

snapshots['TestConfig.test_read[REPOSITORY] 1'] = 'docker.io/library/unittests'

snapshots['TestConfig.test_read[SOURCE_DIRS] 1'] = [
    'src/static'
]

snapshots['TestConfig.test_task_hash 1'] = GenericRepr('<ixian.config.TaskConfig object at 0x100000000>')
