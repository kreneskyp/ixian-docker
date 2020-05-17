# Copyright [2018-2020] Peter Krenesky
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from typing import List

from ixian.config import Config


class PytestConfig(Config):
    #: Python source files to test
    SRC: str = "{PYTHON.ROOT_MODULE_PATH}"

    #: Directory within container where pytest cache is stored
    CACHE_DIR: str = "{DOCKER.APP_DIR}/.pytest_cache"

    #: Pytest configuration file
    INI_FILE: str = "{DOCKER.APP_ETC}/runtime/pytest.ini"

    #: Global args passed to ``pytest``
    ARGS: List[str] = [
        "-c {PYTEST.INI_FILE}",
        "-o cache_dir={PYTEST.CACHE_DIR}",
    ]


PYTEST_CONFIG = PytestConfig()
