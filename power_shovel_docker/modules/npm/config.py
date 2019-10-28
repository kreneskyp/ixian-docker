import os

from power_shovel.check.checker import hash_object
from power_shovel.config import Config, CONFIG
from power_shovel.modules.filesystem.file_hash import FileHash
from power_shovel.utils.decorators import classproperty


class NPMConfig(Config):

    @classproperty
    def MODULE_DIR(cls):
        """Directory where shovel.npm is installed"""
        from power_shovel_docker.modules import npm
        return os.path.dirname(os.path.realpath(npm.__file__))

    # file name for NPM config
    PACKAGE_JSON = 'package.json'

    # Directory in container where node_modules is located.
    NODE_MODULES_DIR = '{DOCKER.APP_DIR}/node_modules'

    # Tag for docker volume containing node_modules.
    NODE_MODULES_VOLUME = '{PROJECT_NAME}.node_modules'

    # Dockerfile template for NPM support. This snippet is rendered with the
    # base dockerfile template to create a single combined docker image.
    DOCKERFILE_TEMPLATE = '{NPM.MODULE_DIR}/Dockerfile.template'
    DOCKERFILE = 'Dockerfile.npm'

    @classproperty
    def IMAGE_HASH(cls):
        return hash_object(
            [
                CONFIG.DOCKER.BASE_IMAGE_HASH,
                FileHash(
                    '{NPM.DOCKERFILE}',
                    '{NPM.PACKAGE_JSON}'
                ).state()
            ]
        )

    REPOSITORY = "{DOCKER.REPOSITORY}"
    IMAGE_TAG = "npm-{NPM.IMAGE_HASH}"
    IMAGE = "{NPM.REPOSITORY}:{NPM.IMAGE_TAG}"