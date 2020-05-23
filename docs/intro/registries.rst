Docker Registries
===========================

Ixian has support baked in to push and pull images from your docker registry.


Build Cache
-----------

Caching is baked into image building tasks and utilities. The docker registry is used as a
cache. Images, including intermediate images, may be pushed to the registry. Subsequent builds
will pull those images when available.

This is built into existing image building tasks (e.g. ``build_image``) and can be extended to
other build layers.


Setup
-----

Image Registry
^^^^^^^^^^^^^^

#. Setup the image registry.

    .. code-block::

        # Specify the registry for your images. The image's name will be generated
        # from this url and path.
        #
        #   e.g. my.registries.domain.name.com/my_project
        #
        CONFIG.DOCKER.REGISTRY = 'my.registry.domain.name.com'
        CONFIG.DOCKER.REGISTRY_PATH = 'my_project'

        # Registries for built-in modules default to DOCKER.REGISTRY but
        # you may override if needed.
        CONFIG.PYTHON.REGISTRY = 'my.other.registry.domain.name.com'


#. Configure the registry

    All registries that are configured for images must be configured in ``DOCKER.REGISTRIES`` to
    be able to push/pull

    .. code-block:: python

        CONFIG.DOCKER.REGISTRIES = {
            'my.registry.domain.name.com': {
                # registry specific config goes here.
            }
        }


Docker Registry / Docker.io
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The default docker registry requires authentication to push images.

.. code-block:: python

    from ixian_docker.modules.docker.utils.client.DockerClient

    def init():
        # ... load modules ...

        CONFIG.DOCKER.REGISTRIES = {
            'my.registry.domain.name.com': {
                'client': DockerClient,

                # addtional options may be passed in
                'options': {
                    'username': "my_registry_user"
                    'password': "my_registry_password"
                }
            }
        }


.. warning::

    This hasn't been tested, but it may work.


.. warning::

    Don't store your password in ``ixian.py`` use vault or similar to load it at runtime.


Openshift
^^^^^^^^^

Not supported yet.


Amazon ECR
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Elastic Container Registry (ECR) is Amazon's docker registry.

#. Setup AWS CLI

    ECR integration uses boto3 to authenticate via the AWS API. You must configure the AWS CLI
    in your host environment. Ixian-docker will use whichever authentication method is configured
    for the CLI.


#. Configure registry


    .. code-block:: python

        from ixian_docker.modules.docker.utils.client.ECRDockerClient

        def init():
            # ... load modules ...

            CONFIG.DOCKER.REGISTRIES = {
                'my.registry.domain.name.com': {
                    'client': ECRDockerClient,

                    # addtional options may be passed in
                    'options': {
                        'region_name': "us-west-2"
                    }
                }
            }


.. error::

    ``~/.docker/config.json`` must be cleared manually for ECR authentication. Tokens aren't
    removed when they expire. Once a token expires it will cause login failures until it's manually
    cleared.