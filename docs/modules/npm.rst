################
NPM
################

The NPM module provides tasks for installing and managing javascript packages using the NPM package
manager.

.. code-block:: text

    Relied upon by more than 11 million developers worldwide, npm is committed to making JavaScript
    development elegant, productive, and safe. The free npm Registry has become the center of
    JavaScript code sharing, and with more than one million packages, the largest software registry
    in the world. Our other tools and services take the Registry, and the work you do around it, to
    the next level.

https://www.npmjs.com/

This module builds an image containing installed NPM packages in ``NPM.NODE_MODULES``. When used as
an intermediate image ``NPM.NODE_MODULES`` may be copied into the runtime image.


.. note::

    This module is requires NodeJS be installed in your image. Ixian does not *yet* provide a
    NodeJS module but one based on NVM is in the works. Until then it is recommended you install a
    node version using NVM.

Setup
==================

**1. Load the NPM module within your** ``ixian.py``

    .. code-block:: python

        # ixian.py

        def init():
            load_module('ixian_docker.modules.npm')


**2. Configure NPM**

    NPM uses ``package.json`` for configuration which your project must provide


Config
==================


.. autoclass:: ixian_docker.modules.npm.config.NPMConfig
    :members:
    :undoc-members:



Tasks
==================

build_npm_image
------------------
Build the NPM image.

This is an intermediate image built using ``DOCKER.BASE_IMAGE`` as it's base. The resulting image
will contain all packages as defined by ``NPM.PACKAGE_JSON``.

This task will reuse existing images if possible. It will only build if there is no image available
locally or in the registry. If ``--force`` is received the image will build even if an image
already exists.

``--force`` implies skip-cache for docker build.


ncu
------------------

Update packages using Node Check Update (ncu).

This task is used to update package versions defined in ``NPM.PACKAGE_JSON``. By default this will
only update the config file without updating the installed versions.

This task is is a wrapper around the ``ncu`` command line utility. It runs within the container
started by ``compose``. You may use it to manage packages in a development environment.

Other arguments and flags are passed through to ``ncu``. For example, this returns ``ncu`` internal
help.

.. code-block:: text

    ix ncu --help



npm
------------------

The NPM package manager.

This task is is a wrapper around the ``npm`` command line utility. It runs within the container
started by ``compose``. You may use it to manage packages in a development environment.

Other arguments and flags are passed through to ``npm``. For example, this returns ``npm`` internal
help.

.. code-block:: text

    ix npm --help