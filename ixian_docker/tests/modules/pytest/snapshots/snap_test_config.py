# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from pysnap import Snapshot


snapshots = Snapshot()

snapshots['TestBlackConfig.test_read[ARGS] 1'] = {
    'field': [
        '--config {BLACK.CONFIG}',
        '{BLACK.SRC}'
    ]
}

snapshots['TestBlackConfig.test_read[SRC] 1'] = {
    'field': '/opt/unittests/src/unittests'
}

snapshots['TestPytestConfig.test_read[ARGS] 1'] = {
    'field': [
        '-c {PYTEST.INI_FILE}',
        '-o cache_dir={PYTEST.CACHE_DIR}'
    ]
}

snapshots['TestPytestConfig.test_read[CACHE_DIR] 1'] = {
    'field': '/opt/unittests/.pytest_cache'
}

snapshots['TestPytestConfig.test_read[INI_FILE] 1'] = {
    'field': '/opt/unittests/etc/runtime/pytest.ini'
}

snapshots['TestPytestConfig.test_read[SRC] 1'] = {
    'field': '/opt/unittests/src/unittests'
}
