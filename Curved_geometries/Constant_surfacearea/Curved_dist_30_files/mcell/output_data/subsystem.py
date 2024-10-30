# WARNING: This is an automatically generated file and will be overwritten
#          by CellBlender on the next model export.

import os
import shared
import mcell as m

from parameters import *

# ---- subsystem ----

MODEL_PATH = os.path.dirname(os.path.abspath(__file__))

Surface_cube = m.SurfaceClass(
    name = 'Surface_cube',
    type = m.SurfacePropertyType.ABSORPTIVE,
    affected_complex_pattern = m.AllMolecules
)

Synapse = m.SurfaceClass(
    name = 'Synapse',
    type = m.SurfacePropertyType.TRANSPARENT,
    affected_complex_pattern = m.AllMolecules
)

unnamed_reaction_rule_8 = m.ReactionRule(
    name = 'unnamed_reaction_rule_8',
    reactants = [ m.Complex('NMDAR') ],
    products = [ m.Complex('NMDAR_B') ],
    variable_rate = k_B_rate
)

unnamed_reaction_rule_9 = m.ReactionRule(
    name = 'unnamed_reaction_rule_9',
    reactants = [ m.Complex('NMDAR') ],
    products = [ m.Complex('NMDAR'), m.Complex('Ca2@IN', compartment_name = 'IN') ],
    variable_rate = nmdar_rate_scaled
)

unnamed_reaction_rule_10 = m.ReactionRule(
    name = 'unnamed_reaction_rule_10',
    reactants = [ m.Complex('NMDAR_B') ],
    products = [ m.Complex('NMDAR') ],
    variable_rate = k_U_rate
)

# ---- create subsystem object and add components ----

subsystem = m.Subsystem()
subsystem.add_surface_class(Surface_cube)
subsystem.add_surface_class(Synapse)
subsystem.add_reaction_rule(unnamed_reaction_rule_8)
subsystem.add_reaction_rule(unnamed_reaction_rule_9)
subsystem.add_reaction_rule(unnamed_reaction_rule_10)

# load subsystem information from bngl file
subsystem.load_bngl_molecule_types_and_reaction_rules(os.path.join(MODEL_PATH, 'model.bngl'), shared.parameter_overrides)

# set additional information about species and molecule types that cannot be stored in BNGL,
# elementary molecule types are already in the subsystem after they were loaded from BNGL
def set_bngl_molecule_types_info(subsystem):
    glu = subsystem.find_elementary_molecule_type('glu')
    assert glu, "Elementary molecule type 'glu' was not found"
    glu.diffusion_constant_3d = 2.2e-6

    NMDAR_0 = subsystem.find_elementary_molecule_type('NMDAR_0')
    assert NMDAR_0, "Elementary molecule type 'NMDAR_0' was not found"
    NMDAR_0.diffusion_constant_2d = 0

    NMDAR_1 = subsystem.find_elementary_molecule_type('NMDAR_1')
    assert NMDAR_1, "Elementary molecule type 'NMDAR_1' was not found"
    NMDAR_1.diffusion_constant_2d = 0

    NMDAR_2 = subsystem.find_elementary_molecule_type('NMDAR_2')
    assert NMDAR_2, "Elementary molecule type 'NMDAR_2' was not found"
    NMDAR_2.diffusion_constant_2d = 0

    NMDAR_D = subsystem.find_elementary_molecule_type('NMDAR_D')
    assert NMDAR_D, "Elementary molecule type 'NMDAR_D' was not found"
    NMDAR_D.diffusion_constant_2d = 0

    NMDAR_0B = subsystem.find_elementary_molecule_type('NMDAR_0B')
    assert NMDAR_0B, "Elementary molecule type 'NMDAR_0B' was not found"
    NMDAR_0B.diffusion_constant_2d = 0

    NMDAR_1B = subsystem.find_elementary_molecule_type('NMDAR_1B')
    assert NMDAR_1B, "Elementary molecule type 'NMDAR_1B' was not found"
    NMDAR_1B.diffusion_constant_2d = 0

    NMDAR_2B = subsystem.find_elementary_molecule_type('NMDAR_2B')
    assert NMDAR_2B, "Elementary molecule type 'NMDAR_2B' was not found"
    NMDAR_2B.diffusion_constant_2d = 0

    NMDAR_DB = subsystem.find_elementary_molecule_type('NMDAR_DB')
    assert NMDAR_DB, "Elementary molecule type 'NMDAR_DB' was not found"
    NMDAR_DB.diffusion_constant_2d = 0

    NMDAR = subsystem.find_elementary_molecule_type('NMDAR')
    assert NMDAR, "Elementary molecule type 'NMDAR' was not found"
    NMDAR.diffusion_constant_2d = 0

    NMDAR_B = subsystem.find_elementary_molecule_type('NMDAR_B')
    assert NMDAR_B, "Elementary molecule type 'NMDAR_B' was not found"
    NMDAR_B.diffusion_constant_2d = 0

    Ca2 = subsystem.find_elementary_molecule_type('Ca2')
    assert Ca2, "Elementary molecule type 'Ca2' was not found"
    Ca2.diffusion_constant_3d = 2.2e-6

set_bngl_molecule_types_info(subsystem)
