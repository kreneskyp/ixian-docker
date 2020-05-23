Building Images
=============================

Ixian-docker can help you build images. More specifically, it orchestrates multi-stage builds
that produce heirarchies of docker images. It enable projects to stand up application stacks
without worrying (as much) how to configure it all. The goal is that you spend less time on the
platform tooling and more building your application.

Ixian-docker projects combine a set of modules to form an application stack. Ixian modules provide
tasks that build intermediate images for platform features and provide development tools such as
test runners and linters.


Setup
-----

The set of modules that make up your stack is configured in ``ixian.py``.

.. code-block:: python

    # ixian.py

    def init():
        # load ixian core
        load_module('ixian.modules.core')

        # load core docker module - provides core framework for building docker apps
        load_module('ixian_docker.modules.docker')

        # load modules to build your stack to your needs
        load_module('ixian_docker.modules.python')

        # Most modules provide config to customize their usage.
        # Update config as needed after loading modules.
        CONFIG.PYTHON.REQUIREMENTS_FILES += [
            "{PYTHON.ETC}/requirements-dev.txt"
        ]


Choosing Stages
---------------

Built-ins
^^^^^^^^^

Ixian-docker comes with built-in modules that provide support for common build tools. They're
pre-wired to work with each other making it the easiest way to stand up a project.

All modules are built on the core ixian module and the docker module. For all other modules see
their pages for setup instructions.


Python
""""""""""""

* :doc:`Python</modules/python>` - pip python packaging
* :doc:`Black</modules/black>` - black code formatter
* :doc:`Pytest</modules/pytest>` - pytest test runner
* :doc:`Django</modules/django>` - django web framework


NodeJS
""""""""""""""

* :doc:`Python</modules/npm>` - NPM package manager
* :doc:`Black</modules/prettier>` - Prettier code formatter
* :doc:`Pytest</modules/jest>` - Jest test runner
* :doc:`Django</modules/webpack>` - Webpack javascript bundler
* :doc:`Django</modules/eslint>` - ESLint javascript linter



Custom Build Stages
^^^^^^^^^^^^^^^^^^^

Ixian is a modular system that's easily extended to add additional build stages. Read more about
that :doc:`here</advanced/modules>`







