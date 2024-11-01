import mcell as m

# ---- Cube ----
Cube_vertex_list = [
    [-5.03990268707275, -6.21513652801514, -3.74906206130981], 
    [-5.03990268707275, -6.21513652801514, 4.25093793869019], 
    [-5.03990268707275, 1.78486371040344, -3.74906206130981], 
    [-5.03990268707275, 1.78486371040344, 4.25093793869019], 
    [2.96009731292725, -6.21513652801514, -3.74906206130981], 
    [2.96009731292725, -6.21513652801514, 4.25093793869019], 
    [2.96009731292725, 1.78486371040344, -3.74906206130981], 
    [2.96009731292725, 1.78486371040344, 4.25093793869019]
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


