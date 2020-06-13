# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from pysnap import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestPythonConfig.test_read[BIN] 1'] = 'python'

snapshots['TestPythonConfig.test_read[DOCKERFILE] 1'] = '/home/runner/work/ixian-docker/ixian-docker/ixian_docker/modules/python/Dockerfile.lib.jinja'

snapshots['TestPythonConfig.test_read[HOST_ROOT_MODULE_PATH] 1'] = '/home/runner/work/ixian-docker/ixian-docker/unittests'

snapshots['TestPythonConfig.test_read[IMAGE] 1'] = 'docker.io/library/unittests:python-fafedf5f121f5d67ba65a6f871a7a7e4c2aa3ad55ffe4b0e36a5c34c799d6904'

snapshots['TestPythonConfig.test_read[IMAGE_TAG] 1'] = 'python-fafedf5f121f5d67ba65a6f871a7a7e4c2aa3ad55ffe4b0e36a5c34c799d6904'

snapshots['TestPythonConfig.test_read[REPOSITORY] 1'] = 'docker.io/library/unittests'

snapshots['TestPythonConfig.test_read[ROOT_MODULE] 1'] = 'unittests'

snapshots['TestPythonConfig.test_read[ROOT_MODULE_PATH] 1'] = '/opt/unittests/src/unittests'

snapshots['TestPythonConfig.test_read[VIRTUAL_ENV] 1'] = '.venv'

snapshots['TestPythonConfig.test_read[VIRTUAL_ENV_DIR] 1'] = '/opt/unittests/.venv'

snapshots['TestPythonConfig.test_read[VIRTUAL_ENV_RUN] 1'] = 'python'

snapshots['TestPythonConfig.test_read[MODULE_DIR] 1'] = '/home/runner/work/ixian-docker/ixian-docker/ixian_docker/modules/python'

snapshots['TestPythonConfig.test_read[APT_PACKAGES] 1'] = [
    'make',
    'build-essential',
    'libssl-dev',
    'zlib1g-dev',
    'libbz2-dev',
    'libreadline-dev',
    'libsqlite3-dev',
    'wget',
    'curl',
    'llvm',
    'libncurses5-dev',
    'libncursesw5-dev',
    'xz-utils',
    'tk-dev',
    'libffi-dev',
    'liblzma-dev'
]

snapshots['TestPythonConfig.test_read[ETC] 1'] = '/opt/unittests/etc/python'

snapshots['TestPythonConfig.test_read[HOST_ETC] 1'] = 'root/opt/unittests/etc/python'

snapshots['TestPythonConfig.test_read[IMAGE_FILES] 1'] = [
    '{PYTHON.ETC}/'
]

snapshots['TestPythonConfig.test_read[PIP] 1'] = 'pip'

snapshots['TestPythonConfig.test_read[RENDERED_DOCKERFILE] 1'] = '/home/runner/work/ixian-docker/ixian-docker/.builder/Dockerfile.python'

snapshots['TestPythonConfig.test_read[REQUIREMENTS_FILES] 1'] = [
    '{PYTHON.ETC}/requirements.txt'
]

snapshots['TestPythonConfig.test_task_hash 1'] = GenericRepr('<ixian.config.TaskConfig object at 0x100000000>')
