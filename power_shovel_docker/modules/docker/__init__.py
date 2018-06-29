MODULE_CONFIG = {
    'name': 'DOCKER',
    'tasks': 'power_shovel_docker.modules.docker.tasks',
    'config': 'power_shovel_docker.modules.docker.config.DockerConfig',

    # Dev volumes mounted only in local environment
    'dev_volumes': [
        '{PWD}:{DOCKER.PROJECT_DIR}',
        '{BUILDER}/.bash_history:{DOCKER.HOME_DIR}/.bash_history',
        '{PWD}/bin/:{DOCKER.APP_DIR}/bin',
        '{PWD}/.env:{DOCKER.APP_DIR}/.env',
    ],
}
