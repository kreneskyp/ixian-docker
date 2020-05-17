################
Jest
################

The Jest javascript test runner. This module provides the tasks and configs for using Jest within
your project.

.. code-block:: text

    Jest is a delightful JavaScript Testing Framework with a focus on simplicity.

    It works with projects using: Babel, TypeScript, Node, React, Angular, Vue and more!

https://jestjs.io/


Setup
==================

**1. Load the Jest module within your** ``ixian.py``

    .. code-block:: python

        # ixian.py

        def init():
            load_module('ixian_docker.modules.jest')


**2. Install Jest**

    Ixian doesn't install ``jest`` for you. There are too many versions so it's up to you to install
    the version compatible with your code.

    If you're using the `NPM` module then just add ``prettier`` to your ``package.json``.

**3. Configure Jest**

    Jest is configured by ``CONFIG.JEST.CONFIG_FILE`` which defaults to ``jest.config.json``.
    Your project must provide this config file.




Config
==================

.. autoclass:: ixian_docker.modules.jest.config.JestConfig
    :members:
    :undoc-members:



Tasks
==================

jest
------------------
Run the Jest javascript test runner.

This task is a proxy to the Jest javascript test runner. It uses ``compose``
to execute jest within the context of the app container.

Configuration is configured by default as:

.. code-block:: text

    --config={JEST.CONFIG_FILE_PATH}

Other arguments and flags are passed through to ``jest``.

For example, this returns ``jest`` internal help.

.. code-block:: text

    $ ix jest --help
