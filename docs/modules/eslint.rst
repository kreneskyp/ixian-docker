################
ESLint
################

The ESLint javascript linter. This module provides the tasks and configs for using ESLint within
your project.

.. code-block:: text

    ESLint is a tool for identifying and reporting on patterns found in ECMAScript/JavaScript code.

https://eslint.org/



Setup
==================

**1. Load the ESLint module within your** ``ixian.py``

    .. code-block:: python

        # ixian.py

        def init():
            load_module('ixian_docker.modules.eslint')


**2. Install ESLint**

    Ixian doesn't install ``eslint`` for you. There are too many versions so it's up to you to
    install the version compatibile with your code.

    If you're using the ``NPM`` module then just add ``eslint`` to your ``package.json``.

    .. code-block:: bash

        npm install --save eslint


**3. Customize config if needed**

    ESLint works without it but you may customize settings with ``.eslintrc``



Config
==================


.. autoclass:: ixian_docker.modules.eslint.config.ESLintConfig
    :members:
    :undoc-members:



Tasks
==================

eslint
------------------
Run the ESLint javascript linter.

This task is a proxy to the Prettier python formatter. It uses ``compose`` to execute ``eslint``
within the context of the app container. This task returns non-zero if linting fails.

Other arguments and flags are passed through to prettier. For example, this returns ``eslint``
internal help.

.. code-block:: bash

    ix eslint --help
