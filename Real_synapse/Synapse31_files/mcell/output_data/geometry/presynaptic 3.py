import mcell as m

# ---- presynaptic ----
presynaptic_vertex_list = [
    [1.45674574375153, -7.88873720169067, -0.563683450222015], 
    [1.45224177837372, -7.90494060516357, -0.591618955135345], 
    [1.47756600379944, -7.88884735107422, -0.588503122329712], 
    [1.43143439292908, -7.89833450317383, -0.544504344463348], 
    [1.42916619777679, -7.90741968154907, -0.571698248386383], 
    [1.41015839576721, -7.92775917053223, -0.5813148021698], 
    [1.40646541118622, -7.92241621017456, -0.555425941944122], 
    [1.42967879772186, -7.91949939727783, -0.5944864153862], 
    [1.4181113243103, -7.93548202514648, -0.608620941638947], 
    [1.4479033946991, -7.92948722839355, -0.615167498588562], 
    [1.42801761627197, -7.95037364959717, -0.625491142272949], 
    [1.47386038303375, -7.91451549530029, -0.609472930431366], 
    [1.45042502880096, -7.95043277740479, -0.638739287853241], 
    [1.47712743282318, -7.93596649169922, -0.629397749900818], 
    [1.50484323501587, -7.92655467987061, -0.619929850101471], 
    [1.50956010818481, -7.94620752334595, -0.64193457365036], 
    [1.4749002456665, -7.95416355133057, -0.651805520057678], 
    [1.44565331935883, -7.96661567687988, -0.663058936595917], 
    [1.44916760921478, -7.98115730285645, -0.68726646900177], 
    [1.41645681858063, -7.96845626831055, -0.645302295684814], 
    [1.4204158782959, -7.98424196243286, -0.671098947525024], 
    [1.42390501499176, -7.99185657501221, -0.699478387832642], 
    [1.39423251152039, -7.9915337562561, -0.654438495635986], 
    [1.3945187330246, -8.0067195892334, -0.680982172489166], 
    [1.40546715259552, -8.00918674468994, -0.708148956298828], 
    [1.38123822212219, -8.030686378479, -0.707171320915222], 
    [1.36941802501678, -8.0135498046875, -0.659710645675659], 
    [1.36770462989807, -8.02732372283936, -0.681411147117615], 
    [1.34991550445557, -8.0457592010498, -0.693738102912903], 
    [1.33794212341309, -8.03396320343018, -0.66581004858017], 
    [1.32459223270416, -8.03043651580811, -0.642300963401794], 
    [1.348273396492, -8.02042770385742, -0.63821679353714], 
    [1.29933500289917, -8.02103328704834, -0.661251902580261], 
    [1.30979931354523, -8.02402877807617, -0.684473752975464], 
    [1.32818841934204, -8.04286670684814, -0.692820131778717], 
    [1.30879938602448, -8.03973007202148, -0.716263771057129], 
    [1.33416676521301, -8.0504846572876, -0.71363639831543], 
    [1.35690665245056, -8.04947280883789, -0.722267925739288], 
    [1.33025455474854, -8.05801582336426, -0.740718722343445], 
    [1.38062715530396, -8.04115676879883, -0.734982550144196], 
    [1.40189683437347, -8.01849269866943, -0.730741500854492], 
    [1.42753660678864, -8.00289726257324, -0.727684915065765], 
    [1.45635414123535, -8.00904178619385, -0.739337146282196], 
    [1.45319151878357, -7.99296379089355, -0.713810563087463], 
    [1.4785270690918, -7.98470544815063, -0.698703646659851], 
    [1.48342907428741, -8.00091743469238, -0.722784340381622], 
    [1.33107304573059, -8.03023242950439, -0.615130245685577], 
    [1.36244380474091, -8.00045394897461, -0.612839341163635], 
    [1.37149548530579, -7.99948406219482, -0.638508379459381], 
    [1.38600480556488, -7.97869777679443, -0.627960205078125], 
    [1.37891018390656, -7.96677207946777, -0.598258316516876], 
    [1.40177190303802, -7.95637845993042, -0.619544088840485], 
    [1.39860320091248, -7.94442272186279, -0.596814215183258], 
    [1.38979637622833, -7.9460563659668, -0.571811556816101], 
    [1.3697966337204, -7.96870708465576, -0.565557718276978], 
    [1.38238632678986, -7.94436693191528, -0.54145485162735], 
    [1.35769259929657, -7.97962522506714, -0.538554072380066], 
    [1.34354341030121, -7.99996423721313, -0.560015559196472], 
    [1.36123037338257, -7.98973226547241, -0.584625482559204], 
    [1.34401619434357, -8.01167869567871, -0.59023505449295], 
    [1.49832355976105, -7.90617990493774, -0.605036020278931]
] # presynaptic_vertex_list

presynaptic_wall_list = [
    [1, 2, 0], 
    [0, 4, 1], 
    [3, 4, 0], 
    [5, 7, 4], 
    [6, 5, 4], 
    [4, 7, 1], 
    [3, 6, 4], 
    [8, 7, 5], 
    [8, 9, 7], 
    [1, 7, 9], 
    [10, 12, 9], 
    [9, 8, 10], 
    [9, 11, 1], 
    [11, 9, 13], 
    [12, 13, 9], 
    [11, 13, 14], 
    [13, 12, 16], 
    [15, 14, 13], 
    [13, 16, 15], 
    [17, 16, 12], 
    [17, 20, 18], 
    [17, 12, 19], 
    [20, 17, 19], 
    [21, 20, 23], 
    [20, 21, 18], 
    [19, 22, 20], 
    [22, 23, 20], 
    [23, 24, 21], 
    [23, 25, 24], 
    [23, 27, 25], 
    [23, 22, 26], 
    [27, 23, 26], 
    [28, 25, 27], 
    [28, 27, 29], 
    [27, 26, 29], 
    [29, 34, 28], 
    [32, 29, 30], 
    [30, 29, 31], 
    [31, 29, 26], 
    [33, 29, 32], 
    [33, 34, 29], 
    [34, 33, 35], 
    [34, 35, 36], 
    [34, 36, 28], 
    [36, 38, 37], 
    [28, 36, 37], 
    [36, 35, 38], 
    [28, 37, 25], 
    [25, 37, 39], 
    [25, 39, 40], 
    [24, 40, 41], 
    [40, 24, 25], 
    [24, 41, 21], 
    [41, 42, 43], 
    [21, 41, 43], 
    [18, 21, 43], 
    [18, 43, 44], 
    [44, 43, 45], 
    [42, 45, 43], 
    [46, 31, 47], 
    [46, 30, 31], 
    [31, 48, 47], 
    [48, 31, 26], 
    [48, 22, 49], 
    [47, 48, 49], 
    [48, 26, 22], 
    [49, 19, 51], 
    [49, 22, 19], 
    [49, 51, 50], 
    [50, 47, 49], 
    [51, 19, 10], 
    [10, 8, 51], 
    [52, 51, 8], 
    [52, 50, 51], 
    [5, 52, 8], 
    [52, 5, 53], 
    [50, 52, 53], 
    [54, 50, 53], 
    [54, 53, 55], 
    [5, 6, 53], 
    [55, 53, 6], 
    [54, 55, 56], 
    [56, 57, 54], 
    [54, 57, 58], 
    [59, 58, 57], 
    [46, 47, 59], 
    [47, 58, 59], 
    [58, 50, 54], 
    [47, 50, 58], 
    [19, 12, 10], 
    [14, 60, 11], 
    [2, 11, 60], 
    [11, 2, 1]
] # presynaptic_wall_list

presynaptic = m.GeometryObject(
    name = 'presynaptic',
    vertex_list = presynaptic_vertex_list,
    wall_list = presynaptic_wall_list,
    surface_regions = []
)
# ^^^^ presynaptic ^^^^


