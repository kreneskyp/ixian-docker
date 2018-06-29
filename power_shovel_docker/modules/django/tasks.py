from power_shovel import logger
from power_shovel.task import task
from power_shovel.config import CONFIG
from power_shovel_docker.modules.docker.tasks import compose


@task(
    category='django',
    short_description='Django manage.py script.',
)
def manage(*args):
    """
    Shortcut to Django's manage.py script.

    This shortcut gives access to manage.py within the context of the app
    container. Volumes and environment variables for loaded modules are loaded
    automatically via docker-compose.

    The script is run by calling `{PYTHON.BIN} manage.py`. Arguments are passed
    through to the script.

    Type `shovel manage --help` for it's built-in help.
    """
    compose('{PYTHON.BIN} manage.py', args)


@task(
    category='django',
    short_description='open django python shell'
)
def shell(*args):
    """
    Shortcut to Django python shell.

    This shortcut runs within the context of the app container. Volumes and
    environment variables for loaded modules are loaded automatically via
    docker-compose.
    """
    manage('shell_plus', *args)


@task(
    category='django',
    short_description='open django shell_plus'
)
def shell_plus(*args):
    """
    Shortcut to Django extensions shell_plus.

    This shortcut runs within the context of the app container. Volumes and
    environment variables for loaded modules are loaded automatically via
    docker-compose.
    """
    manage('shell_plus', *args)


@task(
    category='testing',
    parent = ['test', 'test_python'],
    short_description='django test runner'
)
def django_test(*args):
    """
    Shortcut to Django test runner

    This shortcut runs within the context of the app container. Volumes and
    environment variables for loaded modules are loaded automatically via
    docker-compose.

    The command automatically sets these settings:
       --settings={DJANGO.SETTINGS_TEST}
       --exclude-dir={DJANGO.SETTINGS_MODULE}

    Arguments are passed through to the command.
    """
    command = (
        '''test '''
        '''--settings={DJANGO.SETTINGS_TEST} '''
        '''--exclude-dir={DJANGO.SETTINGS_MODULE} '''
    )

    # call command with args, if no args are given run tests from root module.
    manage(command, *(args or [CONFIG.PYTHON.ROOT_MODULE]))


@task(
    category='django',
    short_description='run database migrations'
)
def migrate(*args):
    manage('migrate', *args)


@task(
    category='django',
    short_description='generate missing database migrations'
)
def makemigrations(*args):
    """
    Generate missing django migrations. This is a shortcut to
    `manage.py makemigrations`.

    By default this will generate migrations only for {CONFIG.PROJECT_NAME}.
    This is overridden whenever args are passed to this task.
    """
    manage('makemigrations %s' % ' '.join(args or [CONFIG.PROJECT_NAME]))


@task(
    category='django',
    short_description='open a database shell'
)
def dbshell(*args):
    """
    Shortcut to `manage.py dbshell`
    """
    manage('dbshell', *args)


@task(
    category='django',
    short_description='start django test server'
)
def runserver(*args):
    """
    Shortcut to `manage.py runserver 0.0.0.0:8000`

    This command maps port 8000:8000 so the server is accessible outside the
    container. Additional args are passed through to the command but the IP and
    port can not be changed.
    """
    compose(
        CONFIG.format('{PYTHON.BIN} manage.py runserver'),
        args,
        flags=['-p 8000:8000'],
    )
