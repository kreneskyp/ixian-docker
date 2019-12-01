MODULE_CONFIG = {
    "name": "BOWER",
    "tasks": "power_shovel_docker.modules.bower.tasks",
    "config": "power_shovel_docker.modules.bower.config.BowerConfig",
    "dockerfile_template": "{BOWER.DOCKERFILE_TEMPLATE}",
    "dev_volumes": ["{BOWER.COMPONENTS_VOLUME}:{BOWER.COMPONENTS_DIR}",],
}
