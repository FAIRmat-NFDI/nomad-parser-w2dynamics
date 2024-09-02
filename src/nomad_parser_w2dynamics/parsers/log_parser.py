#
# Copyright The NOMAD Authors.
#
# This file is part of NOMAD.
# See https://nomad-lab.eu for further info.
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
#

import os
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from structlog.stdlib import (
        BoundLogger,
    )

from nomad.parsing.file_parser import Quantity, TextParser

from nomad_parser_w2dynamics.parsers.utils import get_files

re_n = r'[\n\r]'


class LogParser(TextParser):
    def __init__(self):
        super().__init__(None)

    def init_quantities(self):
        self._quantities = [
            Quantity(
                'program_version', r'Version\s*([0-9.]+)', dtype=str, flatten=False
            )
        ]


class W2DynamicsLogParser:
    def parse(self, mainfile: str = '', logger: 'BoundLogger' = None) -> str:
        """
        If the log file is found, the program version is extracted from it.

        Args:
            mainfile (str, optional): The w2dynamics HDF5 mainfile. Defaults to ''.
            logger (BoundLogger, optional): The logger to log messages. Defaults to None.

        Returns:
            str: The program version.
        """
        program_version = ''

        basename = os.path.basename(mainfile)
        log_files = get_files(pattern='*.log', filepath=mainfile, stripname=basename)
        if log_files is not None and len(log_files) > 0:
            if len(log_files) > 1:
                logger.warning(
                    'Multiple logging files found, the last one will be parsed.',
                    data={'files': log_files},
                )
            log_parser = LogParser()
            log_parser.mainfile = log_files[-1]
            program_version = log_parser.get('program_version', '')
        return program_version
