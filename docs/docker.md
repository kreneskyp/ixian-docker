# Docker

Core docker layout and other utility tasks. Features for creating images and
running containers are included. 

## Features
### Layout
TODO describe the layout defined by the docker module

* /srv - project
* /srv/my_project

### Templated Builder Pattern
This module uses Jinja2 to build a Dockerfile for an image containing the 
runtime, app files, and build utilities for the app. A unified app image like
this allows for consistent environment when debugging builder failures. It also
allows build tools to be used within the app image to develop and debug.

This module provides a base template that is configured by default. Modules may
contribute additional snippets of the Dockerfile. The base template renders 
these with `CONFIG` and `MODULES` in the context. 

### Auto-volumes
Builder modules may specify `volumes` and `dev_volumes` that will be mounted in 
prod and dev environments. This allows modules to contribute build artifacts to
the runtime. The modules are mounted automatically by `compose` and `run`

## Config

## Virtual Targets


## Tasks

##### clean_docker
Kill and remove all docker containers

##### build_dockerfile
Build dockerfile from configured modules and settings.

This task compiles a dockerfile based on the settings for the project. Each
module may provide a jinja template snippet. The snippets are passed to
a base template that renders them.

The base template is read from `{DOCKER.DOCKERFILE_TEMPLATE}`. The base
template is passed `CONFIG` and `MODULES` in the context.

Each module may have template snippet to include.

The compiled Dockerfile is written to `{CONFIG.DOCKER.DOCKER_FILE}`.


##### build_app
Builds the docker app using CONFIG.DOCKER_FILE.


##### compose
Run a docker-compose command in app container.


##### bash
Bash shell in app container.


##### up
Start app container.


##### down
Stop app container.


## Utils
