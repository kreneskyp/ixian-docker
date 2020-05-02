class PythonModuleConfig(object):
    """Custom config object for Python module.

    Custom config to enable dynamically generated `dev_volumes`
    """

    name = "PYTHON"
    tasks = "ixian_docker.modules.python2.tasks"
    config = "ixian_docker.modules.python2.config.PythonConfig"
    dockerfile_template = "{PYTHON.MODULE_DIR}/Dockerfile.template"

    def __getitem__(self, key):
        try:
            return getattr(self, key)
        except AttributeError:
            if key == "dev_volumes":
                return self.dev_volumes
            else:
                raise KeyError(key)

    def __contains__(self, key):
        return key in self.__dict__ or key == "dev_volumes"

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    @property
    def dev_volumes(self):
        from ixian_docker.modules.python2.utils import (
            pipenv_local_package_mount_flags,
        )

        return [
            # Pipenv
            "{PYTHON.VIRTUAL_ENV_VOLUME}:{PYTHON.VIRTUAL_ENV_DIR}",
            # Mount Pipfile in because it can't be symlinked.
            "{PWD}/Pipfile:{DOCKER.APP_DIR}/Pipfile",
            # ipython history
            "{BUILDER}/.ipython/:{DOCKER.HOME_DIR}/.ipython/",
        ] + pipenv_local_package_mount_flags()


MODULE_CONFIG = PythonModuleConfig()
