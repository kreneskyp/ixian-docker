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
    """Build a docker image.

    Builds a docker image. This is a shim around Docker-py that adds some
    power-shovel utilities to it.

    :param tag: Tag for image.
    :param file: Dockerfile.
    :param context: build context, default is the working directory.
    :param args: args to pass as build-args to build
    """

    # TODO: --no-cache for clean builds

    arg_flags = ' '.join(
        ['--build-arg %s=%s' % item for item in (args or {}).items()])

    execute('docker build -t {name} -f {file} {args} {context}'.format(
        name=tag,
        file=file,
        context=context,
        args=arg_flags
    ))


def build_volume_from_image(image, path, tag=None):
    """Build a volume from a docker image.

    This utility is used to build volumes from an existing image. This allows
    images stored in a registry to pulled and used as libraries.

    :param image: image tag to build from
    :param path: path within docker image to create a volume for
    :param tag: volume tag, defaults to image name
    """
    tag = tag or image

    # TODO: list of outputs instead of single path
    # TODO: remove existing volume first
    #execute('docker volume rm %s' % tag)
    execute('docker run -v {tag}:{path} --rm {image} true'.format(
        image=image,
        path=path,
        tag=tag
    ))


def convert_volume_flags(volumes):
    """Format volume patterns into volume flags.

    TODO: deprecate this and let docker-py handle formatting volumes

    :param volumes: list of volume strings
    :return: list of volume flags
    """
    return ['-v %s' % CONFIG.format(volume) for volume in volumes]


def run_builder(
    image,
    outputs,
    command='build',
    flags=None,
    env=None,
    volumes=None
):
    """Run a docker builder container.

    This function is a helper for using the docker builder pattern.

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
    :param command: command string to execute, default is "build".
    :param flags: additional docker build flags.
    :param env: additional env flags .
    :param volumes: list of volume mappings.
    """
    # TODO use docker-py

    env_flags = ' '.join(['-e %s=%s' % item for item in (env or {}).items()])
    volume_flags = ' '.join(convert_volume_flags(volumes or []))

    # mount outputs into volumes.
    # TODO move this into build_library_volume
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


def build_library_image(tag, image, env=None, volumes=None):
    """Create a library image from the output of a docker builder.

    This runs the builder without any outputs mapped. The builder will save
    to the container. The container will be committed into the new image.

    :param tag: tag for library image
    :param image: builder image to build library with.
    :param env: additional env flags for builder.
    :param volumes: list of volume mappings. Volumes may be used to add caches
        or dependencies to the build.
    """
    # commit the builder first to create a blank container for the new image.
    # This ensures that this command doesn't update the builder container and
    # taint it for other builds.
    library_image_tag = None
    execute('docker commit {container} {library_image}')

    # run the builder and commit the changes
    run_builder(library_image_tag, env=env, volumes=volumes)
    execute('docker commit {container} {library_image}')


def convert_library_volume_to_libary_image():
    """Convert library volumes into a library image.

    This takes existing library volumes and saves them to a volume. The image
    can then be pushed to a registry to share it between builds

    :return:
    """
    # TODO: implement


def build_library_volumes(image, outputs, env=None, volumes=None):
    """Create volumes from the output of a docker builder.

    This runs the builder with volumes mounted for all outputs. The outputted
    library volumes can then be mounted and used by other builders or the
    runtime container.

    `outputs` should be specified as a list of docker volume mapping strings.
    Mappings may contain config variables.




    :param image: builder image to build library with.
    :param outputs: outputs expected for library.
    :param env: additional env flags for builder.
    :param volumes: list of volume mappings. Volumes may be used to add caches
        or dependencies to the build.
    """
    run_builder(image, outputs, env=env, volumes=volumes)


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
