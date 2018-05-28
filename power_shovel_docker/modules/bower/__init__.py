MODULE_CONFIG = {
    'name': 'bower',
    'tasks': 'power_shovel_docker.modules.bower.tasks',
    'config': 'power_shovel_docker.modules.bower.config.BowerConfig',
    'dockerfile_template': '{BOWER.MODULE_DIR}/Dockerfile.template',
    'dev_volumes': [
        '{BOWER.COMPONENTS_VOLUME}:{BOWER.COMPONENTS_DIR}'
    ],
}
