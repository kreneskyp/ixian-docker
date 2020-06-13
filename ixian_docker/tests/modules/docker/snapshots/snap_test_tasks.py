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

snapshots['TestBuildBaseImage.test_execute[image_exists] 1'] = '''
'''

snapshots['TestBuildBaseImage.test_execute[image_exists] 2'] = '''
'''

snapshots['TestBuildBaseImage.test_execute[image_exists] 3'] = [
    (
        (
            'docker.io/library/unittests:base-cb2b61a3ab3b91b612b16472e48791c117955b65912ac88efeed75fe478b8742'
        ,),
        {
        }
    ,)
]

snapshots['TestBuildBaseImage.test_execute[image_exists] 4'] = [
]

snapshots['TestBuildBaseImage.test_execute[image_exists] 5'] = [
]

snapshots['TestBuildBaseImage.test_execute[image_exists_local] 1'] = '''
'''

snapshots['TestBuildBaseImage.test_execute[image_exists_local] 2'] = '''
'''

snapshots['TestBuildBaseImage.test_execute[image_exists_local] 3'] = [
    (
        (
            'docker.io/library/unittests:base-cb2b61a3ab3b91b612b16472e48791c117955b65912ac88efeed75fe478b8742'
        ,),
        {
        }
    ,)
]

snapshots['TestBuildBaseImage.test_execute[image_exists_local] 4'] = [
]

snapshots['TestBuildBaseImage.test_execute[image_exists_local] 5'] = [
]

snapshots['TestBuildBaseImage.test_execute[image_does_not_exist] 1'] = '''
'''

snapshots['TestBuildBaseImage.test_execute[image_does_not_exist] 2'] = '''
'''

snapshots['TestBuildBaseImage.test_execute[image_does_not_exist] 3'] = [
    (
        (
            'docker.io/library/unittests:base-cb2b61a3ab3b91b612b16472e48791c117955b65912ac88efeed75fe478b8742'
        ,),
        {
        }
    ,)
]

snapshots['TestBuildBaseImage.test_execute[image_does_not_exist] 4'] = [
    (
        (
            'docker.io/library/unittests',
            'base-cb2b61a3ab3b91b612b16472e48791c117955b65912ac88efeed75fe478b8742'
        ,),
        {
        }
    ,)
]

snapshots['TestBuildBaseImage.test_execute[image_does_not_exist] 5'] = [
]

snapshots['TestBuildBaseImage.test_execute[pull_image] 1'] = '''
'''

snapshots['TestBuildBaseImage.test_execute[pull_image] 2'] = '''
'''

snapshots['TestBuildBaseImage.test_execute[pull_image] 3'] = [
    (
        (
            'docker.io/library/unittests:base-cb2b61a3ab3b91b612b16472e48791c117955b65912ac88efeed75fe478b8742'
        ,),
        {
        }
    ,)
]

snapshots['TestBuildBaseImage.test_execute[pull_image] 4'] = [
    (
        (
            'docker.io/library/unittests',
            'base-cb2b61a3ab3b91b612b16472e48791c117955b65912ac88efeed75fe478b8742'
        ,),
        {
        }
    ,)
]

snapshots['TestBuildBaseImage.test_execute[pull_image] 5'] = [
    (
        (
            'docker.io/library/unittests',
            'base-cb2b61a3ab3b91b612b16472e48791c117955b65912ac88efeed75fe478b8742'
        ,),
        {
        }
    ,)
]

snapshots['TestBuildBaseImage.test_execute[pull_image_not_found] 1'] = '''
'''

snapshots['TestBuildBaseImage.test_execute[pull_image_not_found] 2'] = '''
'''

snapshots['TestBuildBaseImage.test_execute[pull_image_not_found] 3'] = [
    (
        (
            'docker.io/library/unittests:base-cb2b61a3ab3b91b612b16472e48791c117955b65912ac88efeed75fe478b8742'
        ,),
        {
        }
    ,)
]

snapshots['TestBuildBaseImage.test_execute[pull_image_not_found] 4'] = [
    (
        (
            'docker.io/library/unittests',
            'base-cb2b61a3ab3b91b612b16472e48791c117955b65912ac88efeed75fe478b8742'
        ,),
        {
        }
    ,)
]

snapshots['TestBuildBaseImage.test_execute[pull_image_not_found] 5'] = [
    (
        (
            'docker.io/library/unittests',
            'base-cb2b61a3ab3b91b612b16472e48791c117955b65912ac88efeed75fe478b8742'
        ,),
        {
        }
    ,)
]
