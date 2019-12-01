from power_shovel.task import Task
from power_shovel.config import CONFIG
from power_shovel_docker.modules.docker.tasks import compose, Compose


class Manage(Task):
    """
    Shortcut to Django's manage.py script.

    This shortcut gives access to manage.py within the context of the app
    container. Volumes and environment variables for loaded modules are loaded
    automatically via docker-compose.

    The script is run by calling `{PYTHON.BIN} manage.py`. Arguments are passed
    through to the script.

    Type `shovel manage --help` for it's built-in help.
    """

    name = "manage"
    category = "django"
    short_description = "Django manage.py script."
    depends = ["build_pipenv"]

    def execute(self, *args):
        return compose("{PYTHON.BIN} manage.py", *args)


def manage(*args):
    """Shim around `Manage`"""
    return Manage()(*args)


class Shell(Task):
    """
    Shortcut to Django python shell.

    This shortcut runs within the context of the app container. Volumes and
    environment variables for loaded modules are loaded automatically via
    docker-compose.
    """

    name = "shell"
    category = "django"
    short_description = "open django python shell"

    def execute(self, *args):
        return manage("shell_plus", *args)


class ShellPlus(Task):
    """
    Shortcut to Django extensions shell_plus.

    This shortcut runs within the context of the app container. Volumes and
    environment variables for loaded modules are loaded automatically via
    docker-compose.
    """

    name = "shell_plus"
    category = "django"
    short_description = "open django shell_plus"

    def execute(self, *args):
        return manage("shell_plus", *args)


class DjangoTest(Task):
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

    name = "django_test"
    category = "testing"
    parent = ["test", "test_python"]
    short_description = "django test runner"

    def execute(self, *args):
        command = (
            """test """
            """--settings={DJANGO.SETTINGS_TEST} """
            """--exclude-dir={DJANGO.SETTINGS_MODULE} """
        )
        return manage(command, *(args or [CONFIG.PYTHON.ROOT_MODULE]))


class Migrate(Task):
    """
    Run django migrations.
    """

    name = "migrate"
    category = "django"
    short_description = "run database migrations"

    def execute(self, *args):
        return manage("migrate", *args)


class MakeMigrations(Task):
    """
    Generate missing django migrations. This is a shortcut to
    `manage.py makemigrations`.

    By default this will generate migrations only for {CONFIG.PROJECT_NAME}.
    This is overridden whenever args are passed to this task.
    """

    name = "makemigrations"
    category = "django"
    short_description = "generate missing database migrations"

    def execute(self, *args):
        return manage("makemigrations %s" % " ".join(args or [CONFIG.PROJECT_NAME]))


class DBShell(Task):
    """
    Shortcut to `manage.py dbshell`
    """

    name = "dbshell"
    category = "django"
    short_description = "open a database shell"

    def execute(self, *args):
        return manage("dbshell", *args)


class Runserver(Task):
    """
    Shortcut to `manage.py runserver 0.0.0.0:8000`

    This command maps port 8000:8000 so the server is accessible outside the
    container. Additional args are passed through to the command but the IP and
    port can not be changed.
    """

    name = "runserver"
    category = "django"
    short_description = "start django test server"
    depends = ["build_pipenv"]

    def execute(self, *args):
        return Compose().execute(
            CONFIG.format("{PYTHON.BIN} manage.py runserver"),
            *(args or ["0.0.0.0:8000"]),
            flags=["-p 8000:8000"],
        )
