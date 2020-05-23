Writing modules
===============


Basics
------

Ixian provides a module system. See their documentation for the basics on how to build a module:
https://ixian.readthedocs.io/en/latest/modules.html

Modules for Ixian-docker may provide a few things:

* Build stages - A stage that produces an image.
* Build fragments - A fragment that contributes to another build stage.
* Runtime tools - Anything needed for runtime, including development tools.
* Config - Configuration settings to make all of the above configurable.



Designing Build Stages
----------------------

Check out the documentation for :doc:`multi-stage builds</advanced/build_stages>` to learn more
about how build stages work and how to construct a custom build stage.


Image Layout
------------

Ixian modules use a Dockerfile layout designed to support modular
:doc:`multi stage builds</advanced/build_stages>`. This requires a common image layout scheme so
modules play nice together.

Checkout the documentation on the :doc:`common image layout</advanced/image_layout>` for more
information.




