MODULE_CONFIG = {
    'name': 'webpack',
    'tasks': 'power_shovel.modules.webpack.tasks',
    'config': 'power_shovel.modules.webpack.config.WebpackConfig',

    # Runtime volumes mounted in all environments.
    'volumes': [
        'builder.webpack.compiled_static:{DOCKER.APP_DIR}/compiled_static',
    ]
}
