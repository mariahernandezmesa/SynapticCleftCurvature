import mcell as m

# ---- Cube ----
Cube_vertex_list = [
    [-4.8229341506958, -9.49776077270508, -5.44043445587158], 
    [-4.8229341506958, -9.49776077270508, 2.55956554412842], 
    [-4.8229341506958, -1.49776077270508, -5.44043445587158], 
    [-4.8229341506958, -1.49776077270508, 2.55956554412842], 
    [3.1770658493042, -9.49776077270508, -5.44043445587158], 
    [3.1770658493042, -9.49776077270508, 2.55956554412842], 
    [3.1770658493042, -1.49776077270508, -5.44043445587158], 
    [3.1770658493042, -1.49776077270508, 2.55956554412842]
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


