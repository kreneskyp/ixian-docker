MODULE_CONFIG = {
    'name': 'bower',
    'tasks': 'power_shovel_docker.modules.bower.tasks',
    'config': 'power_shovel_docker.modules.bower.config.BowerConfig',

    # Runtime volumes mounted in all environments.
    'volumes': [
        'builder.bower.bower_components:{DOCKER.APP_DIR}/bower_components',
    ]
}
