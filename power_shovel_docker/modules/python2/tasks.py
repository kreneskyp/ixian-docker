from power_shovel.task import task
from power_shovel_docker.modules.docker.tasks import compose


def python_local_package_mount_flags():
    return []


@task(
    category='testing',
    short_description='Run all test tasks'
)
def test():
    """Virtual target for testing"""


@task(
    category='testing',
    short_description='Run all python test tasks'
)
def test_python():
    """Virtual target for python tests"""


@task(
    category='libraries',
    short_description = 'PipEnv environment manager'
)
def pipenv(*args):
    """
    Run a pipenv command.

    This runs in the builder container with volumes mounted.
    """
    compose('pipenv', *args)


@task(
    category='build',
    short_description='Install python packages with pipenv'
)
def build_pip(*args):
    """Run pipenv install"""
    compose('pipenv install', *args)
