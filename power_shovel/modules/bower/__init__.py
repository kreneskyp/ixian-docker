MODULE_CONFIG = {
    'name': 'bower',
    'tasks': 'power_shovel.modules.bower.tasks',
    'config': 'power_shovel.modules.bower.config.BowerConfig',

    # Runtime volumes mounted in all environments.
    'volumes': [
        'builder.bower.bower_components:{DOCKER.APP_DIR}/bower_components',
    ]
}
