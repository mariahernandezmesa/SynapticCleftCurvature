import mcell as m

# ---- presynaptic ----
presynaptic_vertex_list = [
    [-1.00230252742767, -2.59941959381104, 0.570417165756226], 
    [-1.02970051765442, -2.61275124549866, 0.571463584899902], 
    [-0.987291216850281, -2.57498335838318, 0.580354273319244], 
    [-1.03626728057861, -2.59522891044617, 0.585689067840576], 
    [-1.01484429836273, -2.58077549934387, 0.587209284305573], 
    [-1.00740814208984, -2.55753684043884, 0.597640037536621], 
    [-1.04552173614502, -2.57393836975098, 0.604160666465759], 
    [-1.0642763376236, -2.60099339485168, 0.59264063835144], 
    [-1.02639865875244, -2.54594278335571, 0.614987730979919], 
    [-1.05751752853394, -2.58187127113342, 0.627968013286591], 
    [-1.07798457145691, -2.59380102157593, 0.614473879337311], 
    [-1.04390454292297, -2.56161046028137, 0.624933779239655], 
    [-1.09074914455414, -2.61349773406982, 0.599289059638977], 
    [-1.10094773769379, -2.60920357704163, 0.62252801656723], 
    [-1.13093650341034, -2.6174647808075, 0.62526947259903], 
    [-1.11415064334869, -2.62218356132507, 0.606590986251831], 
    [-1.13998746871948, -2.63582181930542, 0.598256945610046], 
    [-1.1085159778595, -2.63221836090088, 0.584125518798828], 
    [-1.1315803527832, -2.64759826660156, 0.571682691574097], 
    [-1.09799826145172, -2.64467096328735, 0.561969518661499], 
    [-1.07641804218292, -2.62740397453308, 0.575336933135986], 
    [-1.05107593536377, -2.61368179321289, 0.576296627521515], 
    [-1.068244099617, -2.64575600624084, 0.551375567913055], 
    [-1.04310178756714, -2.63125109672546, 0.558457612991333], 
    [-1.08997595310211, -2.65701079368591, 0.539130210876465], 
    [-1.11967170238495, -2.65718674659729, 0.548450350761414], 
    [-1.1510933637619, -2.65890431404114, 0.551624476909637], 
    [-1.18394947052002, -2.65856719017029, 0.548571109771729], 
    [-1.16762971878052, -2.65129399299622, 0.577571213245392], 
    [-1.2024552822113, -2.65017414093018, 0.571158409118652], 
    [-1.16989386081696, -2.63969326019287, 0.604740858078003], 
    [-1.19761490821838, -2.64112138748169, 0.600231170654297], 
    [-1.15475165843964, -2.62816143035889, 0.62074863910675], 
    [-0.999056041240692, -2.53316855430603, 0.611377775669098], 
    [-1.01726961135864, -2.52661514282227, 0.632420301437378], 
    [-0.99489152431488, -2.51117396354675, 0.631593227386475], 
    [-0.969012796878815, -2.52295112609863, 0.6092129945755], 
    [-0.978185594081879, -2.54888296127319, 0.593189835548401], 
    [-0.948372483253479, -2.54191994667053, 0.588049650192261], 
    [-0.958519518375397, -2.56608819961548, 0.574396967887878]
] # presynaptic_vertex_list

presynaptic_wall_list = [
    [0, 1, 3], 
    [0, 4, 2], 
    [3, 4, 0], 
    [4, 5, 2], 
    [4, 6, 5], 
    [3, 6, 4], 
    [8, 5, 6], 
    [7, 6, 3], 
    [10, 6, 7], 
    [11, 8, 6], 
    [6, 10, 9], 
    [10, 12, 13], 
    [7, 12, 10], 
    [14, 13, 15], 
    [13, 12, 15], 
    [17, 16, 15], 
    [15, 16, 14], 
    [15, 12, 17], 
    [16, 17, 18], 
    [18, 17, 19], 
    [20, 19, 17], 
    [12, 20, 17], 
    [7, 20, 12], 
    [21, 20, 7], 
    [23, 20, 21], 
    [22, 19, 20], 
    [20, 23, 22], 
    [21, 1, 23], 
    [19, 22, 24], 
    [19, 24, 25], 
    [19, 25, 18], 
    [18, 25, 26], 
    [28, 26, 27], 
    [18, 26, 28], 
    [18, 28, 16], 
    [16, 28, 30], 
    [27, 29, 28], 
    [28, 29, 31], 
    [31, 30, 28], 
    [32, 16, 30], 
    [14, 16, 32], 
    [3, 21, 7], 
    [1, 21, 3], 
    [8, 33, 5], 
    [8, 34, 33], 
    [33, 34, 35], 
    [35, 36, 33], 
    [33, 36, 37], 
    [36, 38, 37], 
    [37, 38, 39], 
    [39, 2, 37], 
    [37, 2, 5], 
    [5, 33, 37]
] # presynaptic_wall_list

presynaptic = m.GeometryObject(
    name = 'presynaptic',
    vertex_list = presynaptic_vertex_list,
    wall_list = presynaptic_wall_list,
    surface_regions = []
)
# ^^^^ presynaptic ^^^^

