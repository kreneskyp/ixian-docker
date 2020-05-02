import jinja2
import os

from ixian.config import CONFIG


def build_dockerfile(template_path=None, context=None):
    """Build dockerfile from configured modules and settings.

    :param template_path: base template to use for rendering Dockerfile
    :return: DockerFile as a string.
    """

    # build loader that includes files from:
    #  - directory for base template
    #  - directories for each of the module's template snippets.
    path, filename = os.path.split(template_path or CONFIG.DOCKER.DOCKERFILE_TEMPLATE)
    prefixes = {"base": jinja2.FileSystemLoader(path)}
    loader = jinja2.PrefixLoader(prefixes)

    # render template
    environment = jinja2.Environment(loader=loader)
    template = environment.get_template("base/%s" % filename)
    return template.render({"CONFIG": CONFIG, "FOO": "123123"})
