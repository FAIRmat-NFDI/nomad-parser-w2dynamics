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

from typing import (
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import (
        EntryArchive,
    )
    from structlog.stdlib import (
        BoundLogger,
    )

import h5py
from nomad.config import config
from nomad.parsing.parser import MatchingParser
from nomad_simulations.schema_packages.general import Program, Simulation

from nomad_parser_w2dynamics.parsers.log_parser import W2DynamicsLogParser

configuration = config.get_plugin_entry_point(
    'nomad_parser_w2dynamics.parsers:parser_entry_point'
)


class W2DynamicsParser(MatchingParser):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self._hubbard_kanamori_map = {'u': 'u', 'j': 'jh', 'v': 'up'}

        self._dmft_qmc_map = {'ntau': 'n_tau', 'niw': 'n_matsubara_freq'}

        # self._dataset_run_mapping = {
        #     '.axes': x_w2dynamics_axes,
        #     '.quantities': x_w2dynamics_quantities,
        # }

        self._inequivalent_atom_map = {
            'self_energy_iw': 'siw',
            'greens_function_iw': 'giw',
            'greens_function_tau': 'gtau',
        }

    def parse(
        self,
        mainfile: str,
        archive: 'EntryArchive',
        logger: 'BoundLogger',
        child_archives: dict[str, 'EntryArchive'] = None,
    ) -> None:
        self.mainfile = mainfile
        self.archive = archive

        # Read hdf5 file
        try:
            self.data = h5py.File(self.mainfile)
        except Exception:
            logger.error('Error opening hdf5 file.')
            return

        # Add Simulation to data
        simulation = Simulation()
        archive.data = simulation

        # Add Program information
        program_version = W2DynamicsLogParser().parse(
            mainfile=self.mainfile, logger=logger
        )
        simulation.program = Program(
            name='w2dynamics',
            version=program_version,
        )
