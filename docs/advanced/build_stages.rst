
Designing Build Stages
============================


Multi stage builds
------------------

Ixian-docker provides tools to create and arrange build images in stages. Each stage produces an
image which may be cached in the registry. Each stage builds on the stages before it.

    .. code-block:: text

       # For example, a python web app with a javascript front-end might have these build steps.

       Base -> Python -> NodeJS -> Pip -> NPM -> Webpack -> Runtime

By splitting the build into stages earlier steps can be cached and skipped, reducing the length of
rebuilds. The ideal stage to cache is one that is lengthy to build but doesn't change too often.

Stages can be linked together dynamically using args in the Dockerfile for the image name and tag.

.. code-block:: dockerfile

    # The base image can be configured dynamically using build args
    ARG $BASE_IMAGE
    FROM $BASE_IMAGE


Nonlinear Builds
----------------

Multi stage builds need not be linear. They may be arranged in a tree structure to decouple lengthy
build steps that aren't interdependent.

.. code-block:: text

   # For example, NPM and Python can be decoupled.

   Base -> Python -------------> Runtime
        |                    /
        -> NPM -> Webpack -/


Once all intermediate images are built, they must be merged into a final runtime.

#. Pick one of your images to be the main branch. This should probably be the largest image.
#. ``COPY`` files in from other intermediate images


.. code-block:: dockerfile

    # build can be configured at runtime with tagged images.
    ARG $PYTHON_IMAGE
    ARG $WEBPACK_IMAGE

    # merge compiled static from webpack into runtime
    FROM $WEBPACK_IMAGE AS webpack
    FROM $PYTHON_IMAGE
    COPY --from=webpack compiled_static $APP_ENV/


Registry Caching
----------------

Docker-ix supports using your docker registry as a cache for building images. Task state hashes can
be used as identifiers for builds. When building the registry is checked for a matching identifier.
If an image is present it's pulled instead of built.

.. hint::

    if a stage is built, all descendant stages will be built too. Order your stages so slower and
    least frequently updated stages come first.


Registries are configured in your ``ixian.py`` see :doc:`Registry Setup</intro/registry_caching>` for
details.