PROJECT_NAME=ixian_docker
IMAGE=ixian_docker_tests
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


.PHONY: black
black: .image_created .python_version
	${DOCKER_RUN} black .


.PHONY: black-check
black-check: .image_created .python_version
	${DOCKER_RUN} black --check .


.PHONY: bash
bash: .image_created .python_version
	${DOCKER_RUN} /bin/bash

.PHONY: version
version: .image_created .python_version
	${DOCKER_RUN} python3 setup.py --version

.PHONY: dist
dist:
	${DOCKER_RUN} python3 setup.py sdist bdist_wheel

.PHONY: dist-check
dist-check:
	${DOCKER_RUN} twine check dist/*

.PHONY: docs
docs: docs/Makefile
	${DOCKER_RUN} tox -e docs

.PHONY: publish
publish:
	${DOCKER_RUN} twine upload dist/*

.PHONY: publish-test
publish-test:
	${DOCKER_RUN} twine upload --repository-url https://test.pypi.org/legacy/ dist/*

.PHONY: clean
clean:
	rm -rf .tox
	rm -rf .coverage
	rm -rf .eggs
	rm -rf dist
	rm -rf build

.PHONY: teardown
teardown: clean
	rm -rf .image_created
	rm -rf .python-version
