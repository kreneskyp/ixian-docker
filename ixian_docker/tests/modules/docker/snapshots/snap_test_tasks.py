# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from pysnap import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestBuildBaseImage.test_build exit_code'] = GenericRepr('<ExitCodes.SUCCESS: 0>')

snapshots['TestCleanDocker.test_help 1'] = '''
\x1b[1mNAME
\x1b[0m    clean_docker -- 
\x1b[1m
DESCRIPTION
\x1b[0m
    Clean Docker:
        - kill and remove all containers
    \x1b[1m

STATUS
\x1b[0m\x1b[90m○\x1b[0m clean_docker

'''

snapshots['TestCleanDocker.test_help 2'] = '''
'''

snapshots['TestBuildBaseImage.test_help 1'] = '''
\x1b[1mNAME
\x1b[0m    build_base_image -- Build app image
\x1b[1m
DESCRIPTION
\x1b[0mBuilds the docker app image using CONFIG.DOCKER_FILE\x1b[1m

STATUS
\x1b[0m\x1b[90m○\x1b[0m build_base_image

'''

snapshots['TestBuildBaseImage.test_help 2'] = '''
'''

snapshots['TestBuildBaseImage.test_scenarios[image_exists] exit_code'] = GenericRepr('<ExitCodes.ERROR_COMPLETE: -1>')

snapshots['TestBuildBaseImage.test_scenarios[image_exists] log'] = [
    'Already complete. Override with --force or --force-all'
]

snapshots['TestBuildBaseImage.test_scenarios[image_exists] sys.out'] = '''
'''

snapshots['TestBuildBaseImage.test_scenarios[image_exists] sys.err'] = '''
'''

snapshots['TestBuildBaseImage.test_scenarios[image_exists] mock_get_image'] = [
]

snapshots['TestBuildBaseImage.test_scenarios[image_exists] mock_image_exists_in_registry'] = [
]

snapshots['TestBuildBaseImage.test_scenarios[image_exists] mock_pull_image'] = [
]

snapshots['TestBuildBaseImage.test_scenarios[image_exists] mock_build_image'] = [
]

snapshots['TestBuildBaseImage.test_scenarios[image_exists_local] exit_code'] = GenericRepr('<ExitCodes.ERROR_COMPLETE: -1>')

snapshots['TestBuildBaseImage.test_scenarios[image_exists_local] log'] = [
    'Already complete. Override with --force or --force-all'
]

snapshots['TestBuildBaseImage.test_scenarios[image_exists_local] sys.out'] = '''
'''

snapshots['TestBuildBaseImage.test_scenarios[image_exists_local] sys.err'] = '''
'''

snapshots['TestBuildBaseImage.test_scenarios[image_exists_local] mock_get_image'] = [
]

snapshots['TestBuildBaseImage.test_scenarios[image_exists_local] mock_image_exists_in_registry'] = [
]

snapshots['TestBuildBaseImage.test_scenarios[image_exists_local] mock_pull_image'] = [
]

snapshots['TestBuildBaseImage.test_scenarios[image_exists_local] mock_build_image'] = [
]

snapshots['TestBuildBaseImage.test_scenarios[image_does_not_exist] exit_code'] = GenericRepr('<ExitCodes.SUCCESS: 0>')

snapshots['TestBuildBaseImage.test_scenarios[image_does_not_exist] log'] = [
    'Attempting to build image=docker.io/library/unittests:base-dbb75cb730f9d31a1e1b1146f0aa9a387ed98c1cfc80f9f2e5fa78641c90d97f dockerfile=/home/runner/work/ixian-docker/ixian-docker/ixian_docker/tests/Dockerfile.one force=False pull=True',
    'Image does not exist.',
    'Image does not exist on registry.'
]

snapshots['TestBuildBaseImage.test_scenarios[image_does_not_exist] sys.out'] = '''
'''

snapshots['TestBuildBaseImage.test_scenarios[image_does_not_exist] sys.err'] = '''
'''

snapshots['TestBuildBaseImage.test_scenarios[image_does_not_exist] mock_get_image'] = [
]

snapshots['TestBuildBaseImage.test_scenarios[image_does_not_exist] mock_image_exists_in_registry'] = [
    (
        (
            'docker.io/library/unittests',
            'base-dbb75cb730f9d31a1e1b1146f0aa9a387ed98c1cfc80f9f2e5fa78641c90d97f'
        ,),
        {
        }
    ,)
]

snapshots['TestBuildBaseImage.test_scenarios[image_does_not_exist] mock_pull_image'] = [
]

snapshots['TestBuildBaseImage.test_scenarios[image_does_not_exist] mock_build_image'] = [
    (
        (
            '/home/runner/work/ixian-docker/ixian-docker/ixian_docker/tests/Dockerfile.one',
            'docker.io/library/unittests:base-dbb75cb730f9d31a1e1b1146f0aa9a387ed98c1cfc80f9f2e5fa78641c90d97f'
        ,),
        {
            'context': None
        }
    ,)
]

snapshots['TestBuildBaseImage.test_scenarios[image_exists_registry] exit_code'] = GenericRepr('<ExitCodes.SUCCESS: 0>')

snapshots['TestBuildBaseImage.test_scenarios[image_exists_registry] log'] = [
    'Attempting to build image=docker.io/library/unittests:base-dbb75cb730f9d31a1e1b1146f0aa9a387ed98c1cfc80f9f2e5fa78641c90d97f dockerfile=/home/runner/work/ixian-docker/ixian-docker/ixian_docker/tests/Dockerfile.one force=False pull=True',
    'Image does not exist.',
    'Image exists on registry. Pulling image.',
    'Image pulled.',
    'Check passed, skipping build.'
]

snapshots['TestBuildBaseImage.test_scenarios[image_exists_registry] sys.out'] = '''
'''

snapshots['TestBuildBaseImage.test_scenarios[image_exists_registry] sys.err'] = '''
'''

snapshots['TestBuildBaseImage.test_scenarios[image_exists_registry] mock_get_image'] = [
]

snapshots['TestBuildBaseImage.test_scenarios[image_exists_registry] mock_image_exists_in_registry'] = [
    (
        (
            'docker.io/library/unittests',
            'base-dbb75cb730f9d31a1e1b1146f0aa9a387ed98c1cfc80f9f2e5fa78641c90d97f'
        ,),
        {
        }
    ,)
]

snapshots['TestBuildBaseImage.test_scenarios[image_exists_registry] mock_pull_image'] = [
    (
        (
            'docker.io/library/unittests',
            'base-dbb75cb730f9d31a1e1b1146f0aa9a387ed98c1cfc80f9f2e5fa78641c90d97f'
        ,),
        {
        }
    ,)
]

snapshots['TestBuildBaseImage.test_scenarios[image_exists_registry] mock_build_image'] = [
]

snapshots['TestBuildBaseImage.test_scenarios[pull_image_not_found] exit_code'] = GenericRepr('<ExitCodes.SUCCESS: 0>')

snapshots['TestBuildBaseImage.test_scenarios[pull_image_not_found] log'] = [
    'Attempting to build image=docker.io/library/unittests:base-dbb75cb730f9d31a1e1b1146f0aa9a387ed98c1cfc80f9f2e5fa78641c90d97f dockerfile=/home/runner/work/ixian-docker/ixian-docker/ixian_docker/tests/Dockerfile.one force=False pull=True',
    'Image does not exist.',
    'Image exists on registry. Pulling image.',
    'Image could not be pulled: NotFound'
]

snapshots['TestBuildBaseImage.test_scenarios[pull_image_not_found] sys.out'] = '''
'''

snapshots['TestBuildBaseImage.test_scenarios[pull_image_not_found] sys.err'] = '''
'''

snapshots['TestBuildBaseImage.test_scenarios[pull_image_not_found] mock_get_image'] = [
]

snapshots['TestBuildBaseImage.test_scenarios[pull_image_not_found] mock_image_exists_in_registry'] = [
    (
        (
            'docker.io/library/unittests',
            'base-dbb75cb730f9d31a1e1b1146f0aa9a387ed98c1cfc80f9f2e5fa78641c90d97f'
        ,),
        {
        }
    ,)
]

snapshots['TestBuildBaseImage.test_scenarios[pull_image_not_found] mock_pull_image'] = [
    (
        (
            'docker.io/library/unittests',
            'base-dbb75cb730f9d31a1e1b1146f0aa9a387ed98c1cfc80f9f2e5fa78641c90d97f'
        ,),
        {
        }
    ,)
]

snapshots['TestBuildBaseImage.test_scenarios[pull_image_not_found] mock_build_image'] = [
    (
        (
            '/home/runner/work/ixian-docker/ixian-docker/ixian_docker/tests/Dockerfile.one',
            'docker.io/library/unittests:base-dbb75cb730f9d31a1e1b1146f0aa9a387ed98c1cfc80f9f2e5fa78641c90d97f'
        ,),
        {
            'context': None
        }
    ,)
]

snapshots['TestBuildBaseImage.test_custom_tag exit_code'] = GenericRepr('<ExitCodes.SUCCESS: 0>')

snapshots['TestBuildBaseImage.test_custom_tag log'] = [
    'Attempting to build image=docker.io/library/unittests:CUSTOM_TAG dockerfile=/home/runner/work/ixian-docker/ixian-docker/ixian_docker/tests/Dockerfile.one force=False pull=True',
    'Image does not exist.',
    'Image does not exist on registry.'
]

snapshots['TestBuildBaseImage.test_custom_tag sys.out'] = '''
'''

snapshots['TestBuildBaseImage.test_custom_tag sys.err'] = '''
'''

snapshots['TestBuildBaseImage.test_custom_tag mock_get_image'] = [
]

snapshots['TestBuildBaseImage.test_custom_tag mock_image_exists_in_registry'] = [
    (
        (
            'docker.io/library/unittests',
            'CUSTOM_TAG'
        ,),
        {
        }
    ,)
]

snapshots['TestBuildBaseImage.test_custom_tag mock_pull_image'] = [
]

snapshots['TestBuildBaseImage.test_custom_tag mock_build_image'] = [
    (
        (
            '/home/runner/work/ixian-docker/ixian-docker/ixian_docker/tests/Dockerfile.one',
            'docker.io/library/unittests:CUSTOM_TAG'
        ,),
        {
            'context': None
        }
    ,)
]

snapshots['TestBuildBaseImage.test_custom_repository exit_code'] = GenericRepr('<ExitCodes.SUCCESS: 0>')

snapshots['TestBuildBaseImage.test_custom_repository log'] = [
    'Attempting to build image=CUSTOM_REPOSITORY.FAKE:base-dbb75cb730f9d31a1e1b1146f0aa9a387ed98c1cfc80f9f2e5fa78641c90d97f dockerfile=/home/runner/work/ixian-docker/ixian-docker/ixian_docker/tests/Dockerfile.one force=False pull=True',
    'Image does not exist.',
    'Image does not exist on registry.'
]

snapshots['TestBuildBaseImage.test_custom_repository sys.out'] = '''
'''

snapshots['TestBuildBaseImage.test_custom_repository sys.err'] = '''
'''

snapshots['TestBuildBaseImage.test_custom_repository mock_get_image'] = [
]

snapshots['TestBuildBaseImage.test_custom_repository mock_image_exists_in_registry'] = [
    (
        (
            'CUSTOM_REPOSITORY.FAKE',
            'base-dbb75cb730f9d31a1e1b1146f0aa9a387ed98c1cfc80f9f2e5fa78641c90d97f'
        ,),
        {
        }
    ,)
]

snapshots['TestBuildBaseImage.test_custom_repository mock_pull_image'] = [
]

snapshots['TestBuildBaseImage.test_custom_repository mock_build_image'] = [
    (
        (
            '/home/runner/work/ixian-docker/ixian-docker/ixian_docker/tests/Dockerfile.one',
            'CUSTOM_REPOSITORY.FAKE:base-dbb75cb730f9d31a1e1b1146f0aa9a387ed98c1cfc80f9f2e5fa78641c90d97f'
        ,),
        {
            'context': None
        }
    ,)
]

snapshots['TestBuildBaseImage.test_build_force exit_code'] = GenericRepr('<ExitCodes.SUCCESS: 0>')

snapshots['TestBuildBaseImage.test_build_force log'] = [
    'Attempting to build image=docker.io/library/unittests:base-dbb75cb730f9d31a1e1b1146f0aa9a387ed98c1cfc80f9f2e5fa78641c90d97f dockerfile=/home/runner/work/ixian-docker/ixian-docker/ixian_docker/tests/Dockerfile.one force=True pull=True'
]

snapshots['TestBuildBaseImage.test_build_force sys.out'] = '''
'''

snapshots['TestBuildBaseImage.test_build_force sys.err'] = '''
'''

snapshots['TestBuildBaseImage.test_build_force mock_get_image'] = [
]

snapshots['TestBuildBaseImage.test_build_force mock_image_exists_in_registry'] = [
]

snapshots['TestBuildBaseImage.test_build_force mock_pull_image'] = [
]

snapshots['TestBuildBaseImage.test_build_force mock_build_image'] = [
    (
        (
            '/home/runner/work/ixian-docker/ixian-docker/ixian_docker/tests/Dockerfile.one',
            'docker.io/library/unittests:base-dbb75cb730f9d31a1e1b1146f0aa9a387ed98c1cfc80f9f2e5fa78641c90d97f'
        ,),
        {
            'context': None
        }
    ,)
]
