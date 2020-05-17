################
Django
################

This module provides the tasks and configs for using the Django web framework within your app. It
provides high level functions for interacting with django while it's running inside a docker
container.

.. code-block:: text

    Django is a high-level Python Web framework that encourages rapid development and clean,
    pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web
    development, so you can focus on writing your app without needing to reinvent the wheel. It’s
    free and open source.


https://www.djangoproject.com/

.. note::

    This module requires python is installed in your image. Ixian does not *yet* provide a
    Python module that does this for you but one is coming soon based on ``pyenv``. Until then it
    is recommended you install a version of python using ``pyenv``.

Setup
==================

**1. Load the Django module within your** ``ixian.py``

    .. code-block:: python

        # ixian.py

        def init():
            load_module('ixian_docker.modules.django')


**2. Install Django**

    Ixian doesn't install ``django`` for you. There are too many versions so it's up to you to install
    the version compatibile with your code.

    If you're using the ``PYTHON`` module then just add ``django`` to your ``requirements.txt``.

    .. code-block:: bash

        pip install django


**3. Create your django app**

    TODO: need to describe how to setup file structure and configure along with the python module


Config
==================


.. autoclass:: ixian_docker.modules.django.config.DjangoConfig
    :members:
    :undoc-members:



Tasks
==================

manage
------------------
Run the django manage.py management script.

This task is a proxy to the Django management script. It uses `compose` to execute ``manage.py``
within the context of the app container.

Other arguments and flags are passed through to Pytest. For example, this returns ``manage.py``
internal help.

.. code-block:: bash

    ix manage --help


shell
------------------
Shortcut to ``manage.py shell`` within ``compose`` environment.


shell_plus
------------------
Shortcut to ``manage.py shell_plus`` within ``compose`` environment.


django_test
------------------
Shortcut to Django test runner

This shortcut runs within the context of the app container. Volumes and
environment variables for loaded modules are loaded automatically via
docker-compose.

The command automatically sets these settings:
   --settings={DJANGO.SETTINGS_TEST}
   --exclude-dir={DJANGO.SETTINGS_MODULE}

Arguments are passed through to the command.


migrate
------------------
Shortcut to ``manage.py migrate`` within ``compose`` environment.


makemigrations
------------------
Shortcut to ``manage.py makemigrations`` within ``compose`` environment.


dbshell
------------------
Shortcut to ``manage.py dbshell`` within ``compose`` environment.


runserver
------------------
Shortcut to ``manage.py runserver 0.0.0.0:8000`` within ``compose`` environment.

``runserver`` automatically sets ``--service-ports``.

By default runserver will start on ``0.0.0.0:8000``. If any args are passed the first arg must be
the ``host:port``. For example this changes the port.

.. code-block:: bash

    ix runserver 0.0.0.0:8001




Utils
===================

manage
-------------------
``manage`` is a shortcut to calling manage.py with ``run``
