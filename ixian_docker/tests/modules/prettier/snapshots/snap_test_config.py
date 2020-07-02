# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from pysnap import Snapshot


snapshots = Snapshot()

snapshots['TestPrettierConfig.test_read[BIN] 1'] = {
    'field': '/opt/unittests/node_modules/.bin/prettier'
}

snapshots['TestPrettierConfig.test_read[SRC] 1'] = {
    'field': '/srv/wet_arms/src/static'
}
