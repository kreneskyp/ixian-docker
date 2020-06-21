# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from pysnap import Snapshot


snapshots = Snapshot()

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

snapshots['TestBuildBaseImage.test_execute[image_exists] log'] = [
    'Attempting to build image=docker.io/library/unittests:base-cb2b61a3ab3b91b612b16472e48791c117955b65912ac88efeed75fe478b8742 dockerfile=/home/runner/work/ixian-docker/ixian-docker/ixian_docker/tests/Dockerfile.one',
    'Image exists, skipping build.'
]

snapshots['TestBuildBaseImage.test_execute[image_exists] sys.out'] = '''
'''

snapshots['TestBuildBaseImage.test_execute[image_exists] sys.err'] = '''
'''

snapshots['TestBuildBaseImage.test_execute[image_exists] mock_image_exists'] = [
    (
        (
            'docker.io/library/unittests:base-cb2b61a3ab3b91b612b16472e48791c117955b65912ac88efeed75fe478b8742'
        ,),
        {
        }
    ,)
]

snapshots['TestBuildBaseImage.test_execute[image_exists] mock_image_exists_in_registry'] = [
]

snapshots['TestBuildBaseImage.test_execute[image_exists] mock_pull_image'] = [
]

snapshots['TestBuildBaseImage.test_execute[image_exists_local] log'] = [
    'Attempting to build image=docker.io/library/unittests:base-cb2b61a3ab3b91b612b16472e48791c117955b65912ac88efeed75fe478b8742 dockerfile=/home/runner/work/ixian-docker/ixian-docker/ixian_docker/tests/Dockerfile.one',
    'Image exists, skipping build.'
]

snapshots['TestBuildBaseImage.test_execute[image_exists_local] sys.out'] = '''
'''

snapshots['TestBuildBaseImage.test_execute[image_exists_local] sys.err'] = '''
'''

snapshots['TestBuildBaseImage.test_execute[image_exists_local] mock_image_exists'] = [
    (
        (
            'docker.io/library/unittests:base-cb2b61a3ab3b91b612b16472e48791c117955b65912ac88efeed75fe478b8742'
        ,),
        {
        }
    ,)
]

snapshots['TestBuildBaseImage.test_execute[image_exists_local] mock_image_exists_in_registry'] = [
]

snapshots['TestBuildBaseImage.test_execute[image_exists_local] mock_pull_image'] = [
]

snapshots['TestBuildBaseImage.test_execute[image_does_not_exist] log'] = [
    'Attempting to build image=docker.io/library/unittests:base-cb2b61a3ab3b91b612b16472e48791c117955b65912ac88efeed75fe478b8742 dockerfile=/home/runner/work/ixian-docker/ixian-docker/ixian_docker/tests/Dockerfile.one',
    'Image does not exist.',
    'Image does not exist on registry.',
    'Building image dockerfile=/home/runner/work/ixian-docker/ixian-docker/ixian_docker/tests/Dockerfile.one tag=docker.io/library/unittests:base-cb2b61a3ab3b91b612b16472e48791c117955b65912ac88efeed75fe478b8742 context=/home/runner/work/ixian-docker/ixian-docker',
    'Step 1/2 : FROM alpine',
    ' ---> [IMAGE]',
    'Step 2/2 : RUN touch /tmp/bar',
    ' ---> Running in [CONTAINER]',
    ' ---> [IMAGE]',
    'Successfully built [IMAGE]',
    'Successfully tagged unittests:base-cb2b61a3ab3b91b612b16472e48791c117955b65912ac88efeed75fe478b8742'
]

snapshots['TestBuildBaseImage.test_execute[image_does_not_exist] sys.out'] = '''
'''

snapshots['TestBuildBaseImage.test_execute[image_does_not_exist] sys.err'] = '''
'''

snapshots['TestBuildBaseImage.test_execute[image_does_not_exist] mock_image_exists'] = [
    (
        (
            'docker.io/library/unittests:base-cb2b61a3ab3b91b612b16472e48791c117955b65912ac88efeed75fe478b8742'
        ,),
        {
        }
    ,)
]

snapshots['TestBuildBaseImage.test_execute[image_does_not_exist] mock_image_exists_in_registry'] = [
    (
        (
            'docker.io/library/unittests',
            'base-cb2b61a3ab3b91b612b16472e48791c117955b65912ac88efeed75fe478b8742'
        ,),
        {
        }
    ,)
]

snapshots['TestBuildBaseImage.test_execute[image_does_not_exist] mock_pull_image'] = [
]

snapshots['TestBuildBaseImage.test_execute[pull_image] log'] = [
    'Attempting to build image=docker.io/library/unittests:base-cb2b61a3ab3b91b612b16472e48791c117955b65912ac88efeed75fe478b8742 dockerfile=/home/runner/work/ixian-docker/ixian-docker/ixian_docker/tests/Dockerfile.one',
    'Image does not exist.',
    'Image exists on registry. Pulling image.',
    'Image pulled.',
    'Check passed, skipping build.'
]

snapshots['TestBuildBaseImage.test_execute[pull_image] sys.out'] = '''
'''

snapshots['TestBuildBaseImage.test_execute[pull_image] sys.err'] = '''
'''

snapshots['TestBuildBaseImage.test_execute[pull_image] mock_image_exists'] = [
    (
        (
            'docker.io/library/unittests:base-cb2b61a3ab3b91b612b16472e48791c117955b65912ac88efeed75fe478b8742'
        ,),
        {
        }
    ,)
]

snapshots['TestBuildBaseImage.test_execute[pull_image] mock_image_exists_in_registry'] = [
    (
        (
            'docker.io/library/unittests',
            'base-cb2b61a3ab3b91b612b16472e48791c117955b65912ac88efeed75fe478b8742'
        ,),
        {
        }
    ,)
]

snapshots['TestBuildBaseImage.test_execute[pull_image] mock_pull_image'] = [
    (
        (
            'docker.io/library/unittests',
            'base-cb2b61a3ab3b91b612b16472e48791c117955b65912ac88efeed75fe478b8742'
        ,),
        {
        }
    ,)
]

snapshots['TestBuildBaseImage.test_execute[pull_image_not_found] log'] = [
    'Attempting to build image=docker.io/library/unittests:base-cb2b61a3ab3b91b612b16472e48791c117955b65912ac88efeed75fe478b8742 dockerfile=/home/runner/work/ixian-docker/ixian-docker/ixian_docker/tests/Dockerfile.one',
    'Image does not exist.',
    'Image exists on registry. Pulling image.',
    'Image could not be pulled: NotFound',
    'Building image dockerfile=/home/runner/work/ixian-docker/ixian-docker/ixian_docker/tests/Dockerfile.one tag=docker.io/library/unittests:base-cb2b61a3ab3b91b612b16472e48791c117955b65912ac88efeed75fe478b8742 context=/home/runner/work/ixian-docker/ixian-docker',
    'Step 1/2 : FROM alpine',
    ' ---> [IMAGE]',
    'Step 2/2 : RUN touch /tmp/bar',
    ' ---> Running in [CONTAINER]',
    ' ---> [IMAGE]',
    'Successfully built [IMAGE]',
    'Successfully tagged unittests:base-cb2b61a3ab3b91b612b16472e48791c117955b65912ac88efeed75fe478b8742'
]

snapshots['TestBuildBaseImage.test_execute[pull_image_not_found] sys.out'] = '''
'''

snapshots['TestBuildBaseImage.test_execute[pull_image_not_found] sys.err'] = '''
'''

snapshots['TestBuildBaseImage.test_execute[pull_image_not_found] mock_image_exists'] = [
    (
        (
            'docker.io/library/unittests:base-cb2b61a3ab3b91b612b16472e48791c117955b65912ac88efeed75fe478b8742'
        ,),
        {
        }
    ,)
]

snapshots['TestBuildBaseImage.test_execute[pull_image_not_found] mock_image_exists_in_registry'] = [
    (
        (
            'docker.io/library/unittests',
            'base-cb2b61a3ab3b91b612b16472e48791c117955b65912ac88efeed75fe478b8742'
        ,),
        {
        }
    ,)
]

snapshots['TestBuildBaseImage.test_execute[pull_image_not_found] mock_pull_image'] = [
    (
        (
            'docker.io/library/unittests',
            'base-cb2b61a3ab3b91b612b16472e48791c117955b65912ac88efeed75fe478b8742'
        ,),
        {
        }
    ,)
]

snapshots['TestBuildBaseImage.test_custom_tag log'] = [
    'Attempting to build image=docker.io/library/unittests:CUSTOM_TAG dockerfile=/home/runner/work/ixian-docker/ixian-docker/ixian_docker/tests/Dockerfile.one',
    'Image does not exist.',
    'Image does not exist on registry.',
    'Building image dockerfile=/home/runner/work/ixian-docker/ixian-docker/ixian_docker/tests/Dockerfile.one tag=docker.io/library/unittests:CUSTOM_TAG context=/home/runner/work/ixian-docker/ixian-docker',
    'Step 1/2 : FROM alpine',
    ' ---> [IMAGE]',
    'Step 2/2 : RUN touch /tmp/bar',
    ' ---> Running in [CONTAINER]',
    ' ---> [IMAGE]',
    'Successfully built [IMAGE]',
    'Successfully tagged unittests:CUSTOM_TAG'
]

snapshots['TestBuildBaseImage.test_custom_tag sys.out'] = '''
'''

snapshots['TestBuildBaseImage.test_custom_tag sys.err'] = '''
'''

snapshots['TestBuildBaseImage.test_custom_tag mock_image_exists'] = [
    (
        (
            'docker.io/library/unittests:CUSTOM_TAG'
        ,),
        {
        }
    ,)
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

snapshots['TestBuildBaseImage.test_build_failure log'] = [
    'Attempting to build image=docker.io/library/unittests:base-0c3e1d19600e3b1c6b10c84dff9c6bc7e7021c9765294aef867635449241629c dockerfile=/home/runner/work/ixian-docker/ixian-docker/ixian_docker/tests/Dockerfile.failure',
    'Image does not exist.',
    'Image does not exist on registry.',
    'Building image dockerfile=/home/runner/work/ixian-docker/ixian-docker/ixian_docker/tests/Dockerfile.failure tag=docker.io/library/unittests:base-0c3e1d19600e3b1c6b10c84dff9c6bc7e7021c9765294aef867635449241629c context=/home/runner/work/ixian-docker/ixian-docker',
    'Step 1/2 : FROM alpine',
    ' ---> [IMAGE]',
    'Step 2/2 : RUN this_command_will_fail',
    ' ---> Running in [CONTAINER]',
    '''\x1b[91m/bin/sh: this_command_will_fail: not found
\x1b[0m''',
    "The command '/bin/sh -c this_command_will_fail' returned a non-zero code: 127"
]

snapshots['TestBuildBaseImage.test_build_failure sys.out'] = '''
'''

snapshots['TestBuildBaseImage.test_build_failure sys.err'] = '''
'''

snapshots['TestBuildBaseImage.test_build_failure mock_image_exists'] = [
    (
        (
            'docker.io/library/unittests:base-0c3e1d19600e3b1c6b10c84dff9c6bc7e7021c9765294aef867635449241629c'
        ,),
        {
        }
    ,)
]

snapshots['TestBuildBaseImage.test_build_failure mock_image_exists_in_registry'] = [
    (
        (
            'docker.io/library/unittests',
            'base-0c3e1d19600e3b1c6b10c84dff9c6bc7e7021c9765294aef867635449241629c'
        ,),
        {
        }
    ,)
]

snapshots['TestBuildBaseImage.test_build_failure mock_pull_image'] = [
]
