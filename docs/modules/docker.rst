################
Docker
################

Core docker layout and other utility tasks. Features for creating images and
running containers are included. 




Config
==================

------------------



Tasks
==================

clean_docker
------------------
Kill and remove all docker containers

build_base_image
------------------

Builds the docker app using :code:`CONFIG.DOCKER_FILE_BASE`. This image is built prior to all
intermediate layers.

build_image
------------------
Builds the final docker image using :code:`CONFIG.DOCKER_FILE`


compose
------------------
Run a docker-compose command in app container.


bash
------------------
Bash shell in app container.


up
------------------
Start app container.


down
------------------
Stop app container.

