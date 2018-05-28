MODULE_CONFIG = {
    'name': 'webpack',
    'tasks': 'power_shovel_docker.modules.webpack.tasks',
    'config': 'power_shovel_docker.modules.webpack.config.WebpackConfig',
    'dockerfile_template': '{WEBPACK.MODULE_DIR}/Dockerfile.template',
    'docker_context': '{WEBPACK.DOCKER_CONTEXT}',
    'dev_volumes': [
        '{WEBPACK.COMPILED_STATIC_VOLUME}:{WEBPACK.COMPILED_STATIC_DIR}',
        '{WEBPACK.DOCKER_CONTEXT}/webpack.sh:{DOCKER.APP_DIR}/webpack.sh'
    ]
}
