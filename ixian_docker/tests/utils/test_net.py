import pytest

from ixian_docker.utils.net import is_valid_hostname


@pytest.mark.parametrize(
    "hostname,is_valid",
    [
        ["www.foo.com", True],
        ["www.foo-bar.com", True],
        ["www.foo2.com", True],
        ["www.foo2two.com", True],
        ["foo.com", True],
        ["c.foo.com", True],
        ["foo.net", True],
        ["foo.co", True],
        ["www..foo.com", False],
        ["foo..com", False],
        ["c", False],
        ["foo", False],
        [".www.foo", False],
        [".foo", False],
        ["www.foo.com.", True],
        # max 63 characters per segment
        [
            "BiiiiiiiiiAiiiiiiiiiAiiiiiiiiiAiiiiiiiiiAiiiiiiiiiAiiiiiiiiiAii."
            "AiiiiiiiiiAiiiiiiiiiAiiiiiiiiiAiiiiiiiiiAiiiiiiiiiAiiiiiiiiiAii."
            "AiiiiiiiiiAiiiiiiiiiAiiiiiiiiiAiiiiiiiiiAiiiiiiiiiAiiiiiiiiiAiii."
            ".com",
            False,
        ],
        # max 255 characters
        [
            "CiiiiiiiiiAiiiiiiiiiAiiiiiiiiiAiiiiiiiiiAiiiiiiiiiAiiiiiiiiiAii."
            "CiiiiiiiiiAiiiiiiiiiAiiiiiiiiiAiiiiiiiiiAiiiiiiiiiAiiiiiiiiiAii."
            "CiiiiiiiiiAiiiiiiiiiAiiiiiiiiiAiiiiiiiiiAiiiiiiiiiAiiiiiiiiiAii."
            "CiiiiiiiiiAiiiiiiiiiAiiiiiiiiiAiiiiiiiiiAiiiiiiiiiAiiiiiiiiiAii."
            "CiiiiiiiiiAiiiiiiiiiAiiiiiiiiiAiiiiiiiiiAiiiiiiiiiAiiiiiiiiiAii."
            "CiiiiiiiiiAiiiiiiiiiAiiiiiiiiiAiiiiiiiiiAiiiiiiiiiAiiiiiiiiiAii."
            "AiiiiiiiiiAi.com",
            False,
        ],
    ],
)
def test_is_valid_hostnames(hostname, is_valid):
    assert is_valid == is_valid_hostname(hostname)
