
Image Layout
------------------------------

Ixian modules use a Dockerfile layout designed to support modular
:doc:`multi stage builds</advanced/build_stages>`. The layout is structured minimize ``COPY``
commands and simplify task checks when working with multiple stages.

Base Image
^^^^^^^^^^

Image builds must specify a base image. This may be a stock image such as ``Phusion/base-image`` or
your own base image.

A customized base image is a good place to put lengthy installs or configuration that doesn't
change very often. Note that all other images extend the base image. Changes here trigger a rebuild
of all other images.

Examples of files that belong in the base:
* Package updates and installs (e.g. apt, yum)
* Certificates
* Any other common tooling

.. note::

    Ixian tries to be platform agnostic but when needed it's build stages will be designed for
    Phusion/base-image, a docker optimized Ubuntu variant.

    http://phusion.github.io/baseimage-docker/


Modules
^^^^^^^

Modules build a heirarchy of stages on top of the base image.

Modules files are stored in ``DOCKER.WORK_DIR``. Files are arranged by the stages they are added
in.

.. code-block:: text

    /opt/project
         +- bin            // All module executables may go in this directory.
         |   exe_1         // These do not trigger rebuilds.
         |   exe_2
         |
         \- etc
            +- module_1    // Module config belongs in etc. Each module uses it's own
            |    file_a    // directory
            |    file_b
            \- module_2
                 file_c

Executables share a directory. Changes to executables don't trigger rebuilds so they share a
directory.

.. code-block:: text

    /opt/project
         +- bin
             exe_1
             exe_2


Config files are split up into separate directories to simplify completeness checks and building
images. Built-in modules each only use their own directory. Only this directory needs to be checked
by completeness checks.

.. code-block:: python

    class MyImageBuildTask(Task)
        check = [
            # Checking the entire directory without enumerating specific files
            FileHash("/opt/project/etc/my_module")
        ]


When the image is built only these two directories need to be copied in.

.. code-block:: docker

    # In the modules Dockerfile, copy in the related files.
    COPY root/project/bin/ /opt/project/bin
    COPY root/project/etc/my_module /opt/project/etc/



Runtime Image
^^^^^^^^^^^^^

The runtime image is used to combine files from the intermediate images. It also adds runtime
config files that weren't needed by build stages. This is the final step to building an image.

Examples of runtime files:

* Test runner and lint configs
* Web server configs
* ``.env`` files


.. code-block:: text

         \- etc
            +- runtime    // The runtime has a config directory like everything other module
            |    file_a
            |    file_b



If they can be, built-in tools are configured to expect the config file in the modules ``etc``.
Some build tools require symlinks to the config file to be added to the ``DOCKER.WORKING_DIR``.
Built-ins that require this will indicate so in their setup instructions. These symlinks can be
created in either base image or runtime image.

.. code-block:: docker

    # for example, package.json must be in the working directory ``NPM install`` is called from
    RUN ln -s /opt/project/etc/npm/package.json


Development Environment
^^^^^^^^^^^^^^^^^^^^^^^

Development enviroment uses docker-compose to buid a runtime rather than the runtime itself. Within
docker-compose volumes may be used for live-code editing. This avoids rebuilding the runtime image
whenever it's dependencies change. If your build-stage stages are designed well, the runtime image
only has operations to merge intermediate images making it simple to replicate with
docker-compose volumes.

``bin`` and ``etc`` only require a single volume each. Modules don't need to do anything special
as they store their files under this directory.

    .. code-block:: bash

        docker-compose run \
        -v root/project/bin/:/opt/project/bin \
        -v root/project/etc/:/opt/project/etc
        app
