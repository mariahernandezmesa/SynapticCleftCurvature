import mcell as m

# ---- presynaptic ----
presynaptic_vertex_list = [
    [0, 0.0324149988591671, 1.04999995231628], 
    [0.0063238525763154, 0.0317921526730061, 1.04999995231628], 
    [0.0124046839773655, 0.0299475528299809, 1.04999995231628], 
    [0.0180088095366955, 0.0269520860165358, 1.04999995231628], 
    [0.0229208655655384, 0.0229208655655384, 1.04999995231628], 
    [0.0269520860165358, 0.0180088095366955, 1.04999995231628], 
    [0.0299475528299809, 0.0124046830460429, 1.04999995231628], 
    [0.0317921526730061, 0.00632385350763798, 1.04999995231628], 
    [0.0324149988591671, -1.41690459365407e-09, 1.04999995231628], 
    [0.0317921526730061, -0.0063238525763154, 1.04999995231628], 
    [0.029947554692626, -0.0124046821147203, 1.04999995231628], 
    [0.0269520878791809, -0.0180088076740503, 1.04999995231628], 
    [0.0229208655655384, -0.0229208655655384, 1.04999995231628], 
    [0.0180088076740503, -0.0269520878791809, 1.04999995231628], 
    [0.0124046849086881, -0.0299475528299809, 1.04999995231628], 
    [0.00632385211065412, -0.0317921563982964, 1.04999995231628], 
    [-2.83380918730813e-09, -0.0324149988591671, 1.04999995231628], 
    [-0.00632385024800897, -0.0317921563982964, 1.04999995231628], 
    [-0.0124046830460429, -0.0299475528299809, 1.04999995231628], 
    [-0.0180088113993406, -0.0269520841538906, 1.04999995231628], 
    [-0.0229208637028933, -0.0229208674281836, 1.04999995231628], 
    [-0.0269520822912455, -0.0180088151246309, 1.04999995231628], 
    [-0.0299475528299809, -0.0124046877026558, 1.04999995231628], 
    [-0.0317921526730061, -0.00632385443896055, 1.04999995231628], 
    [-0.0324149988591671, 3.86544990460536e-10, 1.04999995231628], 
    [-0.0317921526730061, 0.00632385537028313, 1.04999995231628], 
    [-0.0299475509673357, 0.0124046886339784, 1.04999995231628], 
    [-0.0269520897418261, 0.01800880394876, 1.04999995231628], 
    [-0.0229208692908287, 0.0229208618402481, 1.04999995231628], 
    [-0.0180088113993406, 0.0269520860165358, 1.04999995231628], 
    [-0.0124046830460429, 0.029947554692626, 1.04999995231628], 
    [-0.00632384978234768, 0.0317921563982964, 1.04999995231628]
] # presynaptic_vertex_list

presynaptic_wall_list = [
    [26, 18, 10], 
    [2, 1, 30], 
    [1, 0, 30], 
    [0, 31, 30], 
    [30, 29, 28], 
    [28, 27, 30], 
    [27, 26, 30], 
    [26, 25, 24], 
    [24, 23, 22], 
    [22, 21, 20], 
    [20, 19, 18], 
    [18, 17, 16], 
    [16, 15, 14], 
    [14, 13, 12], 
    [12, 11, 10], 
    [10, 9, 8], 
    [8, 7, 6], 
    [6, 5, 4], 
    [4, 3, 2], 
    [26, 24, 18], 
    [24, 22, 18], 
    [22, 20, 18], 
    [18, 16, 14], 
    [14, 12, 18], 
    [12, 10, 18], 
    [10, 8, 2], 
    [8, 6, 2], 
    [6, 4, 2], 
    [2, 30, 26], 
    [2, 26, 10]
] # presynaptic_wall_list

presynaptic = m.GeometryObject(
    name = 'presynaptic',
    vertex_list = presynaptic_vertex_list,
    wall_list = presynaptic_wall_list,
    surface_regions = []
)
# ^^^^ presynaptic ^^^^


