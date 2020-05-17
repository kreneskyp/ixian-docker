################
Prettier
################

The Prettier javascript formatter. This module provides the tasks and configs for using Prettier
within your project.

.. code-block:: text

    # What is Prettier?

    - An opinionated code formatter
    - Supports many languages
    - Integrates with most editors
    - Has few options

https://prettier.io/



Setup
==================

**1. Load the Prettier module within your** ``ixian.py``

    .. code-block:: python

        # ixian.py

        def init():
            load_module('ixian_docker.modules.prettier')


**2. Install Prettier**

    Ixian doesn't install ``prettier`` for you. There are too many versions so it's up to you to
    install the version compatibile with your code.

    If you're using the ``NPM`` module then just add ``prettier`` to your ``package.json``.

    .. code-block:: bash

        npm install --save prettier


**3. Customize config if needed**

    Prettier works without them but if you want to customize config as needed:

    * .prettierrc - config file
    * .prettierignore - ignore files

    These files should be present or symlinked in the working directory of the app
    (``DOCKER.APP_ENV``).



Config
==================


.. autoclass:: ixian_docker.modules.prettier.config.PrettierConfig
    :members:
    :undoc-members:



Tasks
==================

prettier
------------------
Run the Prettier javascript formatter.

This task is a proxy to the Prettier python formatter. It uses ``compose`` to execute ``prettier``
within the context of the app container.

Other arguments and flags are passed through to prettier.

For example, this returns ``prettier`` internal help.

.. code-block:: bash

    ix prettier --help



prettier_check
------------------
Run the prettier formatter with ``--check``. This task will return non-zero if any files require
formatting but won't update them.
