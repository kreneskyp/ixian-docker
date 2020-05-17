################
Webpack
################

The Webpack javascript bundler. This module provides the tasks and configs for using Webpack within
your project.

.. code-block:: text

    webpack is a module bundler. Its main purpose is to bundle JavaScript files for usage in a
    browser, yet it is also capable of transforming, bundling, or packaging just about any resource
    or asset.


https://github.com/webpack/webpack


Setup
==================

**1. Load the Webpack module within your** ``ixian.py``

    .. code-block:: python

        # ixian.py

        def init():
            load_module('ixian_docker.modules.webpack')


**2. Install webpack**

    Ixian doesn't install ``webpack`` for you. There are too many versions so it's up to you to
    install the version compatibile with your code.

    If you're using the ``NPM`` module then just add ``webpack`` to your ``package.json``.

    .. code-block:: bash

        npm install --save webpack


**3. Configure webpack**

    Webpack config is stored in ``webpack.config.js``.




Config
==================


.. autoclass:: ixian_docker.modules.webpack.config.WebpackConfig
    :members:
    :undoc-members:



Tasks
==================

build_webpack_image
---------------------
Build image with javascript, css, etc. compiled by Webpack.

This is an intermediate image that extends ``DOCKER.BASE_IMAGE``.

Ixian includes a template for this image. The dockerfile is configured by ``WEBPACK.DOCKERFILE``.
By default it's a jinja template that renders to ``WEBPACK.RENDERED_DOCKERFILE``.

The image will store compiled output in ``WEPBACK.COMPILED_STATIC_DIR`` by default.

This task will reuse existing images if possible. It will only build if there is no image available
locally or in the registry. If ``--force`` is received the image will build even if an image
already exists.

``--force`` implies skip-cache for docker build.


webpack
------------------

Run the webpack javascript/css compiler.

This is a wrapper around ``webpack`` that runs it within the docker image using ``compose``.
Args are passed through to ``webpack``.

For example, this returns ``webpack`` internal help.

.. code-block:: bash

    $ ix webpack --help