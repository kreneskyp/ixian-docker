# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from pysnap import Snapshot


snapshots = Snapshot()

snapshots['TestBlackConfig.test_read[CONFIG] 1'] = {
    'field': '/opt/unittests/etc/runtime/pyproject.toml'
}

snapshots['TestBlackConfig.test_read[SRC] 1'] = {
    'field': '/opt/unittests/src/unittests'
}

snapshots['TestBlackConfig.test_read[ARGS] 1'] = {
    'field': [
        '--config {BLACK.CONFIG}',
        '{BLACK.SRC}'
    ]
}
