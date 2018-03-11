import docker
from docker.errors import NotFound

from power_shovel.modules.filesystem.utils import pwd
from power_shovel.utils.process import execute, get_dev_uid, get_dev_gid
from power_shovel.config import CONFIG


def build_image(
        tag,
        file='Dockerfile',
        context='.',
        args=None):

    arg_flags = ' '.join(
        ['--build-arg %s=%s' % item for item in (args or {}).items()])

    execute('docker build -t {name} -f {file} {args} {context}'.format(
        name=tag,
        file=file,
        context=context,
        args=arg_flags
    ))


def build_volume_from_image(image, path, tag=None):
    """
    Build a volume from a docker image
    :param image: image tag to build from
    :param path: path within docker image to create a volume for
    :param tag: volume tag, defaults to image name
    """
    tag = tag or image

    # remove existing volume first
    #execute('docker volume rm %s' % tag)
    execute('docker run -v {tag}:{path} --rm {image} true'.format(
        image=image,
        path=path,
        tag=tag
    ))


def convert_volume_flags(volumes):
    """
    Format volume patterns into volume flags.

    :param volumes: list of volume strings
    :return: list of volume flags
    """
    return ['-v %s' % CONFIG.format(volume) for volume in volumes]


def run_builder(image, outputs, command='build', flags=None, env=None, volumes=None):
    """
    Run a docker builder container. This function is a helper for using the
    docker builder pattern.

    The default command is is the `build` script. This script should perform
    a library specific build process. (e.g. npm install, webpack compile). The
    default command may be overridden to obtain a shell or run additional tools
    such as a package updater.

    Dependencies may be mounted in using `volumes`.

    Outputs are mounted into volumes tagged with `{tag}.{output}`. Build
    scripts should direct all output to these directories. The volumes can be
    mounted by other builders or containers. The volumes may also be converted
    into images with `image_from_volume('{tag}.{output}')`.

    :param image: builder image to use.
    :param outputs: list of outputs.  May be files or directories.
    :param volumes: list of volume mappings.
    """
    env_flags = ' '.join(['-e %s=%s' % item for item in (env or {}).items()])
    volume_flags = ' '.join(convert_volume_flags(volumes or []))

    # mount outputs into volumes.
    output_volume_flags = ' '.join([
        CONFIG.format('-v {image}.{output}:{DOCKER.APP_DIR}/{output}',
                      image=image,
                      output=output)
        for output in outputs])

    # run builder
    execute(CONFIG.format(
        'docker run -it ' +
        # '--name container.npm ' +
        '-e APP_DIR={DOCKER.APP_DIR} ' +
        '-e DEV_UID={uid} ' +
        '-e DEV_GID={gid} ' +
        '{flags} {env_flags} {output_volumes} {volumes} {image} {command}',
        image=image,
        command=command or 'build',
        uid=get_dev_uid(),
        gid=get_dev_gid(),
        env_flags=env_flags,
        flags=flags or '',
        output_volumes=output_volume_flags,
        volumes=volume_flags
    ))


def build_library_image(tag, image, outputs, env=None, volumes=None):
    """
    Create an image from the output of a docker builder.

    :param image: builder image to use.
    :param volumes: list of volume mappings. Volumes may be used to add caches
        or dependencies to the build.
    """
    run_builder(image, outputs, env=env, volumes=volumes)

    output = '%s/%s' % (CONFIG.DOCKER_BUILDER_OUTPUT_LOCAL, image)
    build_image(
        tag,
        CONFIG.DOCKER_FILE_LIBRARY,
        args={
            'INPUT': output
        }
    )
    # TODO need to copy files from volume to non-volume location. Quickest way
    # to do this is mount volumes in a different location and then copy them
    # to the build location.
    execute('docker commit {container} {library_image}')


def docker_client():
    return docker.from_env()


def volume_exists(tag):
    client = docker.from_env()
    try:
        client.images.get(tag)
    except NotFound:
        return False
    else:
        return True


def image_exists(tag):
    client = docker.from_env()
    try:
        client.images.get(tag)
    except NotFound:
        return False
    else:
        return True
