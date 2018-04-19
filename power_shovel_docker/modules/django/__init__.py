MODULE_CONFIG = {
    'name': 'django',
    'tasks': 'power_shovel_docker.modules.django.tasks',
    'config': 'power_shovel_docker.modules.django.config.DjangoConfig',

    # Runtime volumes mounted in all environments.
    'volumes': [
    ],

    # Dev volumes mounted only in local environment
    'dev_volumes': [
        # Local sources - files that should reflect changes without rebuild
        '{PWD}/manage.py:{DOCKER.APP_DIR}/manage.py',
    ],
}
