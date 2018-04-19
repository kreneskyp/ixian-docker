MODULE_CONFIG = {
    'name': 'docker',
    'tasks': 'power_shovel_docker.modules.docker.tasks',
    'config': 'power_shovel_docker.modules.docker.config.DockerConfig',

    # Runtime volumes mounted in all environments.
    'volumes': [
    ],

    # Dev volumes mounted only in local environment
    'dev_volumes': [
        '{BUILDER}/app.bash_history:{DOCKER.HOME_DIR}/.bash_history',
        '{PWD}/bin/:{DOCKER.APP_DIR}/bin',
    ],
}
