Installation
===================

.. code-block:: bash

   pip install ixian_docker


Setup
===============

1. Create ``ixian.py``
-----------------------------------

Ixian apps must be initialize in ``ixian.py``. Here is a basic setup for a django app.

.. code-block:: python

   # ixian.py
   from ixian.config import CONFIG
   from ixian.module import load_module

   def init():
       # Load ixian core + docker core.
       CONFIG.PROJECT_NAME = 'my_project'
       load_module('ixian.modules.core')
       load_module('ixian_docker.modules.docker')

       # Minimal setup for Django backend + Webpack compiled front end
       load_module('ixian_docker.modules.python')
       load_module('ixian_docker.modules.django')
       load_module('ixian_docker.modules.npm')
       load_module('ixian_docker.modules.webpack')


2. Configure Docker Registries
----------------------------------------

Configure docker registries for pulling and pushing images.

    .. code-block::

        # Specify the registry for your images. The image's name will be generated
        # from this url and path.
        #
        #   e.g. my.registries.domain.name.com/my_project
        #
        CONFIG.DOCKER.REGISTRY = 'my.registry.domain.name.com'
        CONFIG.DOCKER.REGISTRY_PATH = 'my_project'
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


See the section on :doc:`docker registries</intro/registries>` for more information.


3. Module config
----------------------------------------

Modules each have their own requirements for configuration. Built-in modules have sane defaults
where possible. See specific module docs for details.