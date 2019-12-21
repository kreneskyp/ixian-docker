OPTIONS = {
    "name": "WEBPACK",
    "tasks": "power_shovel_docker.modules.webpack.tasks",
    "config": "power_shovel_docker.modules.webpack.config.WebpackConfig",
    "dockerfile_template": "{WEBPACK.MODULE_DIR}/Dockerfile.template",
    "dev_volumes": ["{WEBPACK.COMPILED_STATIC_VOLUME}:{WEBPACK.COMPILED_STATIC_DIR}",],
}
