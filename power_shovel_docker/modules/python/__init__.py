MODULE_CONFIG = {
    'name': 'python',
    'tasks': 'power_shovel_docker.modules.python.tasks',
    'config': 'power_shovel_docker.modules.python.config.PythonConfig',

    # Runtime volumes mounted in all environments.
    'volumes': [
        # library containing virtualenv with packages
        '{PROJECT_NAME}..venv:{DOCKER.APP_DIR}/.venv',
    ],

    # Dev volumes mounted only in local environment
    'dev_volumes': [
        # Local sources - files that should reflect changes without rebuild
        '{PWD}/Pipfile:{DOCKER.APP_DIR}/Pipfile',
        '{PYTHON.HOST_ROOT_MODULE_PATH}:{PYTHON.ROOT_MODULE_PATH}',

        # ipython history
        '{BUILDER}/.ipython/:{DOCKER.HOME_DIR}/.ipython/'
    ]
}
