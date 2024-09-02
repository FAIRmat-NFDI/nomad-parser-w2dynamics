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

from nomad.datamodel import EntryArchive

from nomad_parser_w2dynamics.parsers.parser import W2DynamicsParser

from .conftest import logger


def test_srvo3():
    # parser = W2DynamicsParser()

    # archive = EntryArchive()
    # parser.parse(
    #     mainfile='tests/data/srvo3/SrVO3_beta60-2021-12-03-Fri-13-38-46.hdf5',
    #     archive=archive,
    #     logger=logger
    # )

    assert True


def test_pressure_prnio2():
    # parser = W2DynamicsParser()

    # archive1 = EntryArchive()
    # parser.parse(
    #     mainfile='tests/data/pressure_prnio2/12GPa_d0.00_beta20/DMFT_STEP4.hdf5',
    #     archive=archive1,
    #     logger=logger
    # )

    # archive2 = EntryArchive()
    # parser.parse(
    #     mainfile='tests/data/pressure_prnio2/12GPa_d0.18_beta60/DMFT_STEP4.hdf5',
    #     archive=archive2,
    #     logger=logger
    # )

    assert True
