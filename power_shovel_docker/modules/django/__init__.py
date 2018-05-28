MODULE_CONFIG = {
    'name': 'django',
    'tasks': 'power_shovel_docker.modules.django.tasks',
    'config': 'power_shovel_docker.modules.django.config.DjangoConfig',
    'dockerfile_template': '{DJANGO.MODULE_DIR}/Dockerfile.template',

    # Runtime volumes mounted in all environments.
    'volumes': [],
}
