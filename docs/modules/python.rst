################
Python
################

The Python module

https://www.npmjs.com/

This module builds an image containing installed python packages

.. warning::

    This module is requires Python be installed in your image. Ixian does not *yet* provide a
    module that installs python for you but one is on the drawing board. For now install a system
    python. Likely the new module will use pyenv to install python versions.


Setup
==================

**1. Load the Python module within your** ``ixian.py``

    .. code-block:: python

        # ixian.py

        def init():
            load_module('ixian_docker.modules.python')




Config
==================


.. autoclass:: ixian_docker.modules.python.config.PythonConfig
    :members:
    :undoc-members:



Tasks
==================

build_python_image
------------------

Build image with packages installed from requirements.txt



pip
------------------

The Pip package manager.

This task is is a wrapper around the ``pip`` command line utility. It runs within the container
started by ``compose``. You may use it to manage packages in a development environment.

Other arguments and flags are passed through to ``pip``. For example, this returns ``pip`` internal
help.

.. code-block:: text

    ix pip --help