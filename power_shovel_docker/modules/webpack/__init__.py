MODULE_CONFIG = {
    'name': 'webpack',
    'tasks': 'power_shovel_docker.modules.webpack.tasks',
    'config': 'power_shovel_docker.modules.webpack.config.WebpackConfig',

    # Runtime volumes mounted in all environments.
    'volumes': [
        '{PROJECT_NAME}.compiled_static:{DOCKER.APP_DIR}/compiled_static',
    ]
}
