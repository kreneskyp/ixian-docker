from itertools import chain
from pipenv.patched.pipfile.api import PipfileParser


def pipenv_local_package_mount_flags():
    from power_shovel.config import CONFIG
    pipfile = PipfileParser(CONFIG.PYTHON.PIPFILE)
    data = pipfile.parse()

    flags = []
    items = chain(data['default'].items(), data['develop'].items())
    for package, datum in items:
        if isinstance(datum, dict) and datum.get('editable', False):
            flags.append('{path}:{path}'.format(**datum))
    return flags
