################
Pytest
################

The Pytest python test runner. This module provides the tasks and configs for using Pytest within
your project.

.. code-block:: text

    pytest is a mature full-featured Python testing tool that helps you write better programs.

    The pytest framework makes it easy to write small tests, yet scales to support complex
    functional testing for applications and libraries.


https://docs.pytest.org/en/latest/

.. note::

    This module requires python is installed in your image. Ixian does not *yet* provide a
    Python module that does this for you but one is coming soon based on ``pyenv``. Until then it
    is recommended you install a version of python using ``pyenv``.

Setup
==================

**1. Load the Pytest module within your** ``ixian.py``

    .. code-block:: python

        # ixian.py

        def init():
            load_module('ixian_docker.modules.pytest')


**2. Install pytest**

    Ixian doesn't install ``pytest`` for you. There are too many versions so it's up to you to install
    the version compatibile with your code.

    If you're using the ``PYTHON`` module then just add ``pytest`` to your ``requirements.txt``.

    .. code-block:: bash

        pip install pytest

**3. Configure pytest**

    Pytest may be configured by creating a ``pytest.ini`` file. This is where you configure your app
    specific settings.

    Here is a very basic config file

    .. code-block:: text

        [pytest]
        python_files = tests.py test_*.py *_tests.py
        testpaths = src/my_app

    .. warning::

        Pytest normally may be configured by other means such as ``pyproject.toml`` but those are not
        officially supported. It may be possible to alter ``PYTEST.ARGS`` to use these other means.


Config
==================


.. autoclass:: ixian_docker.modules.pytest.config.PytestConfig
    :members:
    :undoc-members:



Tasks
==================

pytest
------------------
Run the pytest python test runner.

This task is a proxy to the Pytest python test runner. It uses `compose` to execute ``pytest``
within the context of the app container.

Other arguments and flags are passed through to Pytest. For example, this returns ``pytest``
internal help.

.. code-block:: bash

    ix pytest --help
