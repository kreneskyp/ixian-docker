from power_shovel.modules.docker.tasks import compose
from power_shovel.task import task
from power_shovel.utils.process import execute
from power_shovel.config import CONFIG, requires_config



@task()
def manage(*args, **kwargs):
    compose('python3 manage.py', *args, **kwargs)


@task()
def shell():
    manage('shell_plus')


@task()
def shell_plus():
    manage('shell_plus')


@task()
@requires_config('PYTHON', 'DJANGO_SETTINGS_TEST', 'DJANGO_SETTINGS_DIR')
def test_python(path=''):
    execute((
        '''docker-compose run --rm app '''
        '''{python} ./manage.py test {path} '''
        '''--settings={settings} '''
        '''--exclude-dir=DJANGO_SETTINGS_DIR'''.format(
            python='python3',
            settings=CONFIG.DJANGO_SETTINGS_TEST,
            settings_dir=CONFIG.DJANGO_SETTINGS_DIR,
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
    compose(CONFIG.format('{PYTHON.BIN} manage.py runserver 0.0.0.0:8000'))
