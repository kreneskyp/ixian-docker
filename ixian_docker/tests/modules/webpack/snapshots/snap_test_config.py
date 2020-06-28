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

snapshots['TestConfig.test_read[DOCKERFILE] 1'] = '/home/runner/work/ixian-docker/ixian-docker/ixian_docker/modules/webpack/Dockerfile.jinja'

snapshots['TestConfig.test_read[IMAGE] 1'] = 'docker.io/library/unittests:webpack-4e1e0e15e19d17912a7f29939ce0f8d937268106fd137ddd0d2f4902f6667761'

snapshots['TestConfig.test_read[IMAGE_TAG] 1'] = 'webpack-4e1e0e15e19d17912a7f29939ce0f8d937268106fd137ddd0d2f4902f6667761'

snapshots['TestConfig.test_read[MODULE_DIR] 1'] = '/home/runner/work/ixian-docker/ixian-docker/ixian_docker/modules/webpack'

snapshots['TestConfig.test_read[REPOSITORY] 1'] = 'docker.io/library/unittests'

snapshots['TestConfig.test_read[SOURCE_DIRS] 1'] = [
    'src/static'
]

snapshots['TestConfig.test_task_hash 1'] = GenericRepr('<ixian.config.TaskConfig object at 0x100000000>')
