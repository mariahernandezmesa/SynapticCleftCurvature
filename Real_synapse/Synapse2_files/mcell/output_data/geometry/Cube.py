import mcell as m

# ---- Cube ----
Cube_vertex_list = [
    [-2.1217999458313, -6.51475381851196, -4.85059356689453], 
    [-2.1217999458313, -6.51475381851196, 3.14940619468689], 
    [-2.1217999458313, 1.48524618148804, -4.85059356689453], 
    [-2.1217999458313, 1.48524618148804, 3.14940619468689], 
    [5.8782000541687, -6.51475381851196, -4.85059356689453], 
    [5.8782000541687, -6.51475381851196, 3.14940619468689], 
    [5.8782000541687, 1.48524618148804, -4.85059356689453], 
    [5.8782000541687, 1.48524618148804, 3.14940619468689]
] # Cube_vertex_list

Cube_wall_list = [
    [1, 2, 0], 
    [3, 6, 2], 
    [7, 4, 6], 
    [5, 0, 4], 
    [6, 0, 2], 
    [3, 5, 7], 
    [1, 3, 2], 
    [3, 7, 6], 
    [7, 5, 4], 
    [5, 1, 0], 
    [6, 4, 0], 
    [3, 1, 5]
] # Cube_wall_list

Cube = m.GeometryObject(
    name = 'Cube',
    vertex_list = Cube_vertex_list,
    wall_list = Cube_wall_list,
    surface_regions = []
)
# ^^^^ Cube ^^^^


