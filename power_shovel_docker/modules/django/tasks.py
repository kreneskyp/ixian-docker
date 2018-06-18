from power_shovel.task import task
from power_shovel.config import CONFIG
from power_shovel_docker.modules.docker.tasks import compose


@task(
    category='django',
    short_description='Django manage.py script.',
)
def manage(*args):
    compose('{PYTHON.BIN} manage.py', *args)


@task(
    category='django',
    short_description='Django python shell'
)
def shell(*args):
    """Open a django shell_plus shell in app container"""
    manage('shell_plus', *args)


@task(
    category='django',
    short_description='Django extensions shell_plus'
)
def shell_plus(*args):
    manage('shell_plus', *args)


@task(
    category='testing',
    parent = ['test', 'test_python'],
    short_description='Django test runner'
)
def django_test(*args):
    command = (
        '''test '''
        '''--settings={DJANGO.SETTINGS_TEST} '''
        '''--exclude-dir={DJANGO.SETTINGS_MODULE} '''
    )

    # call command with args, if no args are given run tests from root module.
    manage(command, *(args or [CONFIG.PYTHON.ROOT_MODULE]))


@task(
    category='django',
    short_description='Run database migrations'
)
def migrate(*args):
    manage('migrate', *args)


@task(
    category='django',
    short_description='Generate database migrations'
)
def makemigrations(*apps):
    manage('makemigrations %s' % ' '.join(apps or [CONFIG.PROJECT_NAME]))


@task(
    category='django',
    short_description='Database shell'
)
def dbshell(*args):
    manage('dbshell', *args)


@task(
    category='django',
    short_description='Django test server'
)
def runserver(*args):
    compose(
        CONFIG.format('{PYTHON.BIN} manage.py runserver 0.0.0.0:8000'),
        flags=['-p 8000:8000'],
        *args
    )
