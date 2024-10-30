# WARNING: This is an automatically generated file and will be overwritten
#          by CellBlender on the next model export.

import os
import shared
import mcell as m

from parameters import *
from subsystem import *
from geometry import *
MODEL_PATH = os.path.dirname(os.path.abspath(__file__))


# ---- instantiation ----

# ---- release sites ----

# ---- surface classes assignment ----

# OuterCube
Cube.surface_class = Surface_cube
# Synapse
synapse.surface_class = Surface_synapse
# ---- compartments assignment ----

Release_Site_1 = m.ReleaseSite(
    name = 'Release_Site_1',
    complex = m.Complex('glu'),
    shape = m.Shape.SPHERICAL,
    location = (-0.786121330677427, 1.225495896755611, 0.555550612987124),
    site_diameter = 0,
    number_to_release = n_glu
)

Release_Site_2 = m.ReleaseSite(
    name = 'Release_Site_2',
    complex = m.Complex('NMDAR_0', orientation = m.Orientation.UP),
    region = PSD,
    number_to_release = n_NMDAR
)

# ---- create instantiation object and add components ----

instantiation = m.Instantiation()
instantiation.add_geometry_object(Cube)
instantiation.add_geometry_object(presynaptic)
instantiation.add_geometry_object(PSD)
instantiation.add_geometry_object(synapse)
instantiation.add_release_site(Release_Site_1)
instantiation.add_release_site(Release_Site_2)

# load seed species information from bngl file
instantiation.load_bngl_compartments_and_seed_species(os.path.join(MODEL_PATH, 'model.bngl'), None, shared.parameter_overrides)

