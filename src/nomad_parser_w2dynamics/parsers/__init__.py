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

from nomad.config.models.plugins import ParserEntryPoint


class W2DynamicsParserEntryPoint(ParserEntryPoint):

    def load(self):
        from nomad_parser_w2dynamics.parsers.parser import W2DynamicsParser

        return W2DynamicsParser(**self.dict())


parser_entry_point = W2DynamicsParserEntryPoint(
    name='W2DynamicsParserEntryPoint',
    description='Entry point for the W2Dynamics parser.',
    mainfile_binary_header_re=b'^\\x89HDF',
    mainfile_contents_dict={'__has_all_keys': ['.axes', '.config', '.quantities']},
    mainfile_mime_re='(application/x-hdf)',
    mainfile_name_re=r'^.*\.(h5|hdf5)$',
)
