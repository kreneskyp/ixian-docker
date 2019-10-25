import jinja2
import os

from power_shovel.module import MODULES
from power_shovel.config import CONFIG


def build_dockerfile(
    template_path=None,
    context=None
):
    """Build dockerfile from configured modules and settings.

    This compiles a dockerfile based on the settings for the project. Each
    module may provide a jinja template snippet. The snippets are passed to
    a base template that renders them.

    The base template

    :param template_path: base template to use for rendering Dockerfile
    :return: DockerFile as a string.
    """

    # build loader that includes files from:
    #  - directory for base template
    #  - directories for each of the module's template snippets.
    path, filename = os.path.split(
        template_path or CONFIG.DOCKER.DOCKERFILE_TEMPLATE)
    prefixes = {'base': jinja2.FileSystemLoader(path)}
    module_templates = []
    for module in MODULES:
        template = module.get('dockerfile_template', None)

        if not template:
            continue

        path, filename = os.path.split(CONFIG.format(template))
        prefixes[module['name']] = jinja2.FileSystemLoader(path)
        module_templates.append({
            'name': module['name'],
            'template': '{}/{}'.format(module['name'], filename)
        })
    loader = jinja2.PrefixLoader(prefixes)

    # render template
    environment = jinja2.Environment(loader=loader)
    template = environment.get_template('base/%s' % filename)
    return template.render(context or {
        'modules': module_templates,
        'CONFIG': CONFIG
    })