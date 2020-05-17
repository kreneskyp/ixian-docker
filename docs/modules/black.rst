################
Black
################

The Black python formatter. This module provides the tasks and configs for using Black within your
project.

.. code-block:: text

    Black is the uncompromising Python code formatter. By using it, you agree to cede control over
    minutiae of hand-formatting. In return, Black gives you speed, determinism, and freedom from
    pycodestyle nagging about formatting. You will save time and mental energy for more important
    matters.

    Blackened code looks the same regardless of the project you're reading. Formatting becomes
    transparent after a while and you can focus on the content instead.


https://black.readthedocs.io/en/stable/

.. note::

    This module requires python is installed in your image. Ixian does not *yet* provide a
    Python module that does this for you but one is coming soon based on ``pyenv``. Until then it
    is recommended you install a version of python using ``pyenv``.

Setup
==================

**1. Load the Black module within your** ``ixian.py``

    .. code-block:: python

        # ixian.py

        def init():
            load_module('ixian_docker.modules.black')


**2. Configure Black**

    Black uses ``pyproject.toml`` for configuration. Here is an example config:

    .. code-block::text

        [tool.black]
        line-length = 99
        exclude = '''(
            /home/runner/work/ixian/ixian/dist/*
          | /home/runner/work/ixian/ixian/.tox/*
          | /home/runner/work/ixian/ixian/.eggs/*
          | /home/runner/work/ixian/ixian/venv/*
          | snapshots/*
          )


Config
==================


.. autoclass:: ixian_docker.modules.black.config.BlackConfig
    :members:
    :undoc-members:



Tasks
==================

black
------------------
Run the black formatter.

This is a wrapper around ``black`` that runs it within the docker image using ``compose``.
Args are passed through to ``black``.

For example, this returns ``black`` internal help.

.. code-block:: bash

    $ ix black --help



black_check
------------------
Run the black formatter with ``--check``. This task will return non-zero if any files require
formatting but won't update them.
