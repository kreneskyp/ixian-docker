OPTIONS = {
    "name": "BOWER",
    "tasks": "ixian_docker.modules.bower.tasks",
    "config": "ixian_docker.modules.bower.config.BowerConfig",
    "dockerfile_template": "{BOWER.DOCKERFILE_TEMPLATE}",
    "dev_volumes": ["{BOWER.COMPONENTS_VOLUME}:{BOWER.COMPONENTS_DIR}",],
}
