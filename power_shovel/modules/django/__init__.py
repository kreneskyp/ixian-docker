MODULE_CONFIG = {
    'name': 'django',
    'tasks': 'power_shovel.modules.django.tasks',
    'config': 'power_shovel.modules.django.config.DjangoConfig',

    # Runtime volumes mounted in all environments.
    'volumes': [
        # library containing virtualenv with packages
        'builder.python..venv:{DOCKER.APP_DIR}/.venv',
    ],

    # Dev volumes mounted only in local environment
    'dev_volumes': [
        # Local sources - files that should reflect changes without rebuild
        '{PWD}/manage.py:{DOCKER.APP_DIR}/manage.py',
    ],
}
