

Usage
==============

Basics
--------------
Ixian apps are executed using the ``ix`` runner. This is the entry point for ``ixian`` apps. The
general help page lists the available tasks.

    .. code-block:: bash

        $ ix build_image

        usage: ixian [--help] [--log LOG] [--force] [--force-all] [--clean]
             [--clean-all]
             ...

        Run an ixian task.

        positional arguments:
          remainder    arguments for task.

        optional arguments:
          --help       show this help message and exit
          --log LOG    Log level (DEBUG|INFO|WARN|ERROR|NONE)
          --force      force task execution
          --force-all  force execution including task dependencies
          --clean      clean before running task
          --clean-all  clean all dependencies before running task

        Type 'ix help <subcommand>' for help on a specific subcommand.

        Available subcommands:

        [ Build ]
          build_image                Build app image



Internal flags should be placed before the ``task``.

    .. code-block:: bash

        ix --force build_image


Any args after the task name are passed to task's execute method.

For example, many tasks are wrappers around other command line tools. Pass ``--help`` after the
command to get that tool's internal help.

    .. code-block:: bash

        ix pytest --help


Tasks
-----

Once configured you will have access to a number of tasks for building and interacting with the app
in your image. These will vary depending on what modules you've enabled. Here are a couple of
examples.

* Build a docker image.

   .. code-block:: bash

      ix build_image


* Run the django test server.

   .. code-block:: bash

      ix runserver


* Run automated tests.

   .. code-block:: bash

      ix test



Task checks
-----------
Many tasks have state checks that determine if they are already complete. This can be viewed in
ixian task help. Completed dependencies are indicated by a check.

.. code-block:: bash

    STATUS
    ○ build_image
        ✔ build_base_image
        ○ build_npm_image
        ○ build_webpack_image
        ○ build_python_image

If the task or any of it's dependency are incomplete then the task and it's incomplete dependencies
will be run.

.. code-block:: bash

    STATUS
    ○ build_image
        ✔ build_base_image
        ✔ build_npm_image
        ○ build_webpack_image
        ○ build_python_image


When all are complete then the task can be skipped. If checkers detect changes, such as modified
config files, the checkers will indicate a build.

.. code-block:: bash

    STATUS
    ✔ build_image
        ✔ build_base_image
        ✔ build_npm_image
        ✔ build_webpack_image
        ✔ build_python_image


.. Note::

    If there are no checkers then a task runs every time it is called.



Forcing tasks
-------------

Task checks may be bypassed with ``--force``. Pass ``--force-all`` to bypass checks for all
dependencies.

Clean build
-----------

Some tasks have a clean function that removes build artifacts. Pass ``--clean`` to call the clean
function prior to building. Pass ``--clean-all`` to trigger clean for all dependencies. If a task
doesn't define a clean method then ``--clean`` does nothing.

Passing ``--clean`` also implies ``--force``.


Built-in help
-------------

All tasks have built in help generated from task docstrings and metadata. The help page should
explain how to configure and use the task. It also displays the state of tasks and any
dependencies.

When in doubt, check ``help``.


.. code-block:: bash

    $ ix help build_image

    NAME
        build_image -- Build app image

    DESCRIPTION
    Builds a docker image using CONFIG.DOCKER_FILE

    STATUS
    ○ build_image
        ○ build_base_image
        ○ build_npm_image
        ○ build_webpack_image
        ○ build_python_image
