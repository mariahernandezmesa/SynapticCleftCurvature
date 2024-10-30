# WARNING: This is an automatically generated file and will be overwritten
#          by CellBlender on the next model export.

import os
import shared
import mcell as m

from parameters import *
from subsystem import *
from geometry import *
MODEL_PATH = os.path.dirname(os.path.abspath(__file__))


# ---- observables ----

viz_output = m.VizOutput(
    mode = m.VizMode.CELLBLENDER,
    output_files_prefix = './viz_data/seed_' + str(SEED).zfill(5) + '/Scene',
    every_n_timesteps = 1
)

# ---- declaration of rxn rules defined in BNGL and used in counts ----

cterm_count_glu_species_synapse = m.CountTerm(
    species_pattern = m.Complex('glu'),
    region = synapse
)

count_glu_synapse = m.Count(
    name = 'glu_synapse',
    expression = cterm_count_glu_species_synapse,
    file_name = './react_data/seed_' + str(SEED).zfill(5) + '/glu_synapse.dat'
)

# ---- create observables object and add components ----

observables = m.Observables()
observables.add_viz_output(viz_output)
observables.add_count(count_glu_synapse)

# load observables information from bngl file
observables.load_bngl_observables(os.path.join(MODEL_PATH, 'model.bngl'), './react_data/seed_' + str(SEED).zfill(5) + '/', shared.parameter_overrides)
