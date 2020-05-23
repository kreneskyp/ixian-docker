.. ixian-docker documentation master file, created by
   sphinx-quickstart on Sun May 10 17:33:49 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


Ixian-Docker
================

.. toctree::
   :maxdepth: 2
   :caption: Getting Started
   :hidden:

   Installation <intro/setup>
   intro/usage
   intro/building_images
   intro/registries

.. toctree::
   :maxdepth: 2
   :caption: Advanced
   :hidden:

   advanced/modules
   advanced/build_stages
   advanced/image_layout

.. toctree::
   :maxdepth: 2
   :caption: Core Modules
   :hidden:

   modules/docker

.. toctree::
   :maxdepth: 2
   :caption: Python Modules
   :hidden:

   modules/python
   modules/pytest
   modules/black
   modules/django

.. toctree::
   :maxdepth: 4
   :caption: Javascript Modules
   :hidden:

   modules/npm
   modules/jest
   modules/prettier
   modules/webpack
   modules/eslint


Ixian-Docker is a tool that manages docker builds and provides development tooling for interacting
with your docker app. Prebuilt modules are included to construct an application stack quickly.
Ixian's goal is to build applications with sane defaults, but not stand in your way if you'd like
to configure or extend it to better suit your needs.

There are several things Ixian-docker will help you with:

* Building a heirarchy of docker images.
* Pluggable platform features like Python, NodeJS, Django, and more.
* Provides a command line interface to your application running within a local container.

.. include:: intro/setup.rst

.. include:: intro/usage.rst


What's an Ixian?
================

`Ixian <https://github.com/kreneskyp/ixian>`_ is a flexible build tool that this project is built
with. Ixian provides the platform to define and arrange a heirarchy of interrelated tasks into
a command line app.


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
