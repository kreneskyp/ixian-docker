from power_shovel.task import task
from power_shovel.utils.process import execute
from power_shovel.config import CONFIG
from power_shovel.config import requires_config
from power_shovel_docker.modules.docker.tasks import compose


@task()
def manage(*args):
    compose('python3 manage.py', *args)


@task()
def shell():
    """Open a django shell_plus shell in app container"""
    manage('shell_plus')


@task()
def shell_plus():
    manage('shell_plus')


@task(parent=['test', 'test_python'])
def django_test(*args):
    command = (
        '''test '''
        '''--settings={DJANGO.SETTINGS_TEST} '''
        '''--exclude-dir={DJANGO.SETTINGS_MODULE} '''
    )
    manage(command, *args)
    return

    execute((
        '''docker-compose run --rm app '''
        '''{python} ./manage.py test {path} '''
        '''--settings={settings} '''
        '''--exclude-dir=DJANGO_SETTINGS_DIR'''.format(
            python=CONFIG.PYTHON.BIN,
            settings=CONFIG.DJANGO.SETTINGS_TEST,
            settings_dir=CONFIG.DJANGO.SETTINGS_DIR,
            path=path
        )),
        fail_silent=True)


@task()
def migrate():
    manage('migrate')


@task()
def makemigrations(*apps):
    manage('makemigrations %s' % ' '.join(apps or [CONFIG.PROJECT_NAME]))


@task()
def dbshell():
    manage('dbshell')


@task()
def runserver():
    compose(
        CONFIG.format('{PYTHON.BIN} manage.py runserver 0.0.0.0:8000'),
        flags=['-p 8000:8000']
    )
