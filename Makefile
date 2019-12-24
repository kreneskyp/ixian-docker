PROJECT_NAME=power_shovel_docker
IMAGE=chang_docker_tests
PROJECT_DIR=/opt/${PROJECT_NAME}
DOCKER_RUN=docker run -it -v `pwd`:${PROJECT_DIR} -v /var/run/docker.sock:/var/run/docker.sock ${IMAGE}
PYENV_DIR=/opt/pyenv


.image_created: Dockerfile requirements*.txt
	docker build -f Dockerfile -t ${IMAGE} .
	touch $@


.python_version:
	${DOCKER_RUN} cp ${PYENV_DIR}/.python-version ${PROJECT_DIR}


test: .image_created .python_version
	${DOCKER_RUN} tox


BLACK_EXCLUDE=--exclude=snapshots/*


black: .image_created .python_version
	${DOCKER_RUN} black ${BLACK_EXCLUDE} .


black-check: .image_created .python_version
	${DOCKER_RUN} black ${BLACK_EXCLUDE} --check .


bash: .image_created .python_version
	${DOCKER_RUN} /bin/bash


