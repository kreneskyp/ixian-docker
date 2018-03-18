from power_shovel.config import Config


class DockerConfig(Config):

    def __init__(self, *args, **kwargs):
        super(DockerConfig, self).__init__(*args, **kwargs)
        self.ENV = {}
        self.VOLUMES = []
        self.DEV_ENV = {}
        self.DEV_VOLUMES = []

    HOME_DIR = '/root'
    ENV_DIR = '/srv'
    APP_DIR = '{DOCKER.ENV_DIR}/{PROJECT_NAME}'
    PROJECT_DIR = '{DOCKER.APP_DIR}/project'
