import pytest

from ixian.config import CONFIG
from ixian.runner import run
from ixian_docker.tests.conftest import get_tests_dir


DOCKERFILE_ONE = f"{get_tests_dir()}/Dockerfile.one"
DOCKERFILE_TWO = f"{get_tests_dir()}/Dockerfile.one"
DOCKERFILE_FAILURE = f"{get_tests_dir()}/Dockerfile.failure"


class TaskTests:
    def test_help(self, snapshot, mock_cli, capsys):
        """
        Tests ixian help message for task.
        """
        mock_cli.mock_in(f"help {self.task}")
        run()
        out, err = capsys.readouterr()
        snapshot.assert_match(f"\n{out}")
        snapshot.assert_match(f"\n{err}")


class TestCleanDocker(TaskTests):
    task = "clean_docker"

    def test_execute(self, mock_docker_environment):
        raise NotImplementedError


class ___TestBuildDockerfile(TaskTests):
    """
    Tests for building a project's dockerfile
    """

    task = "build_dockerfile"

    def test_execute(self):
        raise NotImplementedError

    def test_already_built(self):
        """
        If image is built and checkers pass then don't build
        """
        raise NotImplementedError

    def test_builds_for_changes(self):
        """
        If image is built and checkers pass then build
        """
        raise NotImplementedError

    def test_builds_custom_dockerfile(self):
        """
        If image is built and checkers pass then build
        """
        raise NotImplementedError


# TODO: test `remove_app_image`


class ___TestBuildApp(TaskTests):
    """
    Tests the BuildApp virtual task
    """

    task = "build_app"
    # TODO: how to make this generic since it's currently hardcoded with

    def test_execute(self):
        raise NotImplementedError

    def test_execute_with_configured_build_targets(self):
        raise NotImplementedError

    def test_build_failure(self):
        # TODO: test multiple stages
        raise NotImplementedError


@pytest.fixture
def mock_build_task(
    base_mock_ixian_environment, mock_docker_registries, build_image_if_needed_scenarios
):
    """
    Fixture that runs through build_image_if_needed_scenarios for a build task
    """

    yield (
        build_image_if_needed_scenarios["assert_build"],
        build_image_if_needed_scenarios["mock_pull_image"],
        build_image_if_needed_scenarios["mock_image_exists_in_registry"],
        build_image_if_needed_scenarios["mock_image_exists"],
        base_mock_ixian_environment,
        mock_docker_registries,
    )


class TestBuildBaseImage(TaskTests):
    """
    Tests the `BuildBaseImae` task which builds the base image.
    """

    task = "build_base_image"

    def test_execute(self, mock_cli, mock_build_task):
        CONFIG.DOCKER.DOCKERFILE_BASE = DOCKERFILE_ONE
        mock_cli.mock_in("build_base_image")
        assert_build, *_ = mock_build_task
        assert_build(CONFIG.DOCKER.BASE_IMAGE)

    def test_custom_tag(self, mock_cli, mock_build_image_if_needed):
        CONFIG.DOCKER.DOCKERFILE_BASE = DOCKERFILE_ONE
        CONFIG.DOCKER.BASE_IMAGE_TAG = f"CUSTOM_TAG"
        mock_cli.mock_in("build_base_image")
        assert_build = mock_build_image_if_needed["assert_build"]
        assert_build(CONFIG.DOCKER.BASE_IMAGE)

    def test_custom_repository(self, mock_cli, mock_build_image_if_needed):
        CONFIG.DOCKER.DOCKERFILE_BASE = DOCKERFILE_ONE
        CONFIG.DOCKER.REPOSITORY = f"CUSTOM_REPOSITORY.FAKE"
        mock_cli.mock_in("build_base_image")

        assert_build = mock_build_image_if_needed["assert_build"]
        assert_build(CONFIG.DOCKER.BASE_IMAGE)

    def test_build_failure(self, mock_cli, mock_build_image_if_needed):
        CONFIG.DOCKER.DOCKERFILE_BASE = DOCKERFILE_FAILURE
        mock_cli.mock_in("build_base_image")
        assert_build = mock_build_image_if_needed["assert_build"]
        assert_build(CONFIG.DOCKER.BASE_IMAGE, builds=False)

    def test_build_no_pull(self):
        """Build without pulling the remote image"""
        raise NotImplementedError

    def test_build_force(self):
        """Force build using ``--force``"""
        raise NotImplementedError


class ___TestPullAppImage(TaskTests):
    """
    Tests the BuildApp virtual task
    """

    task = "pull"

    def test_execute(self):
        raise NotImplementedError

    def test_custom_app_image(self):
        raise NotImplementedError

    def test_pull_failure(self):
        """
        Failure while transferring image
        """
        raise NotImplementedError

    def test_login_failure(self):
        """
        Failure to authenticate
        """
        raise NotImplementedError


class ___TestPushAppImage(TaskTests):
    """
    Tests the BuildApp virtual task
    """

    task = "push"

    def test_execute(self):
        raise NotImplementedError

    def test_custom_app_image(self):
        raise NotImplementedError

    def test_push_failure(self):
        """
        Failure transferring image.
        """
        raise NotImplementedError

    def test_login_failure(self):
        """
        Failure to authenticate
        """
        raise NotImplementedError

    def test_image_does_not_exist(self):
        """
        Failure to authenticate
        """
        raise NotImplementedError


class ___TestCompose(TaskTests):
    task = "compose"

    def test_execute(self):
        raise NotImplementedError

    def test_execute_image_not_available(self):
        """
        Image should be built if not present.
        """
        raise NotImplementedError


class ___TestBash(TaskTests):
    task = "bash"

    def test_execute(self):
        raise NotImplementedError

    def test_execute_with_args(self):
        """
        args and kwargs are passed to /bin/bash
        :return:
        """
        raise NotImplementedError

    def test_execute_image_not_available(self):
        raise NotImplementedError


class ___TestUp(TaskTests):
    task = "up"

    def test_execute(self):
        raise NotImplementedError

    def test_execute_image_not_available(self):
        raise NotImplementedError


class ___TestDown(TaskTests):
    task = "down"

    def test_execute(self):
        raise NotImplementedError

    def test_execute_image_not_available(self):
        raise NotImplementedError
