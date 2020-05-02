OPTIONS = {
    "name": "PYTHON",
    "tasks": "ixian_docker.modules.python.tasks",
    "config": "ixian_docker.modules.python.config.PythonConfig",
    "dockerfile_template": "{PYTHON.MODULE_DIR}/Dockerfile.template",
    # Dev volumes mounted only in local environment
    "dev_volumes": [
        # Pipenv
        "{PYTHON.VIRTUAL_ENV_VOLUME}:{PYTHON.VIRTUAL_ENV_DIR}",
        # Mount Pipfile in because it can't be symlinked.
        "{PWD}/Pipfile:{DOCKER.APP_DIR}/Pipfile",
        # ipython history
        "{BUILDER}/.ipython/:{DOCKER.HOME_DIR}/.ipython/",
    ],
}
