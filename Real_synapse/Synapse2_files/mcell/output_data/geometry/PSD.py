import mcell as m

# ---- PSD ----
PSD_vertex_list = [
    [2.02977013587952, -2.43879818916321, -0.775315880775452], 
    [2.01476311683655, -2.41109466552734, -0.788568258285522], 
    [2.04465198516846, -2.41338586807251, -0.788279712200165], 
    [2.00291419029236, -2.4571578502655, -0.775581479072571], 
    [1.96714782714844, -2.46248340606689, -0.786699950695038], 
    [1.98083806037903, -2.42236232757568, -0.792327165603638], 
    [1.99304187297821, -2.38755297660828, -0.795799434185028], 
    [1.94459986686707, -2.41496324539185, -0.809365272521973], 
    [1.96538519859314, -2.38524413108826, -0.80843198299408], 
    [1.95961225032806, -2.35498356819153, -0.819554567337036], 
    [1.93896484375, -2.37181854248047, -0.823925316333771], 
    [1.91437768936157, -2.35133004188538, -0.83839875459671], 
    [1.93943905830383, -2.3347442150116, -0.833154141902924], 
    [1.91253793239594, -2.38840913772583, -0.830444574356079], 
    [1.88643443584442, -2.36603999137878, -0.84177827835083], 
    [1.912921667099, -2.42213153839111, -0.820281803607941], 
    [1.88644909858704, -2.40463256835938, -0.838281393051147], 
    [1.86044657230377, -2.38180422782898, -0.851139605045319], 
    [1.89201688766479, -2.44894003868103, -0.825963199138641], 
    [1.8604484796524, -2.42075848579407, -0.855323314666748], 
    [1.86277866363525, -2.45719289779663, -0.849628686904907], 
    [1.829185962677, -2.4089503288269, -0.881669163703918], 
    [1.83854365348816, -2.39246916770935, -0.86152720451355], 
    [1.84013783931732, -2.43567609786987, -0.879150629043579], 
    [1.84250545501709, -2.46328258514404, -0.872471809387207], 
    [1.82554876804352, -2.44100332260132, -0.909753382205963], 
    [1.81896436214447, -2.4160053730011, -0.908013105392456], 
    [1.83220160007477, -2.46325850486755, -0.902853012084961], 
    [1.83475470542908, -2.47959136962891, -0.887884020805359], 
    [1.8253276348114, -2.45778965950012, -0.929163753986359], 
    [1.82125544548035, -2.49139285087585, -0.915519833564758], 
    [1.83078706264496, -2.5002281665802, -0.881762444972992], 
    [1.81967127323151, -2.51585102081299, -0.895931780338287], 
    [1.80578517913818, -2.52833104133606, -0.920120418071747], 
    [1.82081413269043, -2.47849059104919, -0.943801999092102], 
    [1.81156051158905, -2.50347232818604, -0.945913672447205], 
    [1.79875290393829, -2.52683734893799, -0.953834474086761], 
    [1.78548896312714, -2.54478454589844, -0.965954661369324], 
    [1.79341268539429, -2.55555772781372, -0.936567187309265], 
    [1.80597102642059, -2.55794358253479, -0.898802399635315], 
    [1.77750444412231, -2.58893537521362, -0.939632892608643], 
    [1.77815198898315, -2.56717276573181, -0.962236106395721], 
    [1.7940149307251, -2.57821702957153, -0.913945198059082], 
    [1.81611156463623, -2.59005284309387, -0.884168267250061], 
    [1.79422080516815, -2.60571455955505, -0.911920249462128], 
    [1.79718291759491, -2.63341379165649, -0.910418450832367], 
    [1.81428480148315, -2.61827158927917, -0.891791880130768], 
    [1.7774475812912, -2.6210081577301, -0.932750403881073], 
    [1.77829110622406, -2.65185379981995, -0.927596390247345], 
    [1.76375317573547, -2.61060547828674, -0.95832896232605], 
    [1.76320683956146, -2.58539342880249, -0.979740619659424], 
    [1.79087340831757, -2.67980575561523, -0.91553521156311], 
    [1.80948781967163, -2.66049289703369, -0.901480853557587], 
    [1.7706732749939, -2.67727136611938, -0.935428559780121], 
    [1.77180016040802, -2.7014045715332, -0.931302309036255], 
    [1.79853880405426, -2.70507121086121, -0.906970620155334], 
    [1.82038140296936, -2.68815851211548, -0.893519580364227], 
    [1.84643566608429, -2.69870710372925, -0.869143903255463], 
    [1.84054613113403, -2.66947650909424, -0.875773429870605], 
    [1.87033569812775, -2.67969822883606, -0.85052365064621], 
    [1.82742214202881, -2.64287185668945, -0.882954597473145], 
    [1.85881888866425, -2.64750003814697, -0.85736870765686], 
    [1.84084284305573, -2.61908793449402, -0.868914186954498], 
    [1.89864182472229, -2.65462398529053, -0.83119535446167], 
    [1.87493121623993, -2.6200122833252, -0.845241129398346], 
    [1.88603842258453, -2.59124135971069, -0.834014356136322], 
    [1.85314512252808, -2.59106802940369, -0.856847047805786], 
    [1.90675532817841, -2.61959075927734, -0.824333786964417], 
    [1.93311154842377, -2.59018230438232, -0.805569529533386], 
    [1.94108235836029, -2.54235935211182, -0.797924637794495], 
    [1.8904219865799, -2.55764555931091, -0.828927278518677], 
    [1.9048810005188, -2.52584147453308, -0.815878629684448], 
    [1.88216376304626, -2.49005198478699, -0.829504013061523], 
    [1.8682576417923, -2.52469611167908, -0.840651512145996], 
    [1.91921019554138, -2.49363327026367, -0.807513892650604], 
    [1.93060350418091, -2.45459628105164, -0.805233001708984], 
    [1.95768046379089, -2.5057201385498, -0.785870671272278], 
    [1.83711457252502, -2.51735997200012, -0.865227580070496], 
    [1.86437928676605, -2.56215763092041, -0.848142743110657], 
    [1.85193932056427, -2.49016571044922, -0.855852842330933], 
    [1.84357035160065, -2.54255342483521, -0.858881711959839], 
    [1.81961381435394, -2.53857278823853, -0.880667090415955], 
    [1.8310683965683, -2.5654296875, -0.869601368904114], 
    [1.89973509311676, -2.69322347640991, -0.834665358066559], 
    [1.91122794151306, -2.72761297225952, -0.834347367286682], 
    [1.874342918396, -2.71413564682007, -0.850353956222534], 
    [1.86695218086243, -2.75447273254395, -0.857551395893097], 
    [1.8468873500824, -2.72764992713928, -0.86647617816925], 
    [1.82076454162598, -2.4288592338562, -0.939572632312775], 
    [1.80232131481171, -2.38868379592896, -0.90258377790451], 
    [1.81879138946533, -2.38422894477844, -0.876248419284821], 
    [1.82720863819122, -2.36470174789429, -0.856371521949768], 
    [1.85573410987854, -2.34309601783752, -0.84926426410675], 
    [1.89023518562317, -2.33009338378906, -0.847774505615234], 
    [1.91937506198883, -2.31217384338379, -0.844304382801056], 
    [1.95140588283539, -2.29767394065857, -0.838792979717255], 
    [1.96407866477966, -2.32886004447937, -0.826237440109253], 
    [2.01735019683838, -2.36990642547607, -0.803490459918976], 
    [2.04024767875671, -2.38737678527832, -0.797763586044312]
] # PSD_vertex_list

PSD_wall_list = [
    [1, 2, 0], 
    [0, 3, 1], 
    [4, 5, 3], 
    [5, 1, 3], 
    [6, 1, 5], 
    [7, 5, 4], 
    [5, 8, 6], 
    [5, 7, 8], 
    [10, 8, 7], 
    [8, 10, 9], 
    [7, 13, 10], 
    [11, 12, 10], 
    [10, 13, 11], 
    [9, 10, 12], 
    [7, 15, 13], 
    [14, 11, 13], 
    [13, 16, 14], 
    [13, 15, 16], 
    [16, 19, 17], 
    [16, 17, 14], 
    [18, 19, 16], 
    [18, 16, 15], 
    [18, 20, 19], 
    [20, 23, 19], 
    [17, 19, 22], 
    [19, 23, 21], 
    [22, 19, 21], 
    [20, 24, 23], 
    [24, 27, 23], 
    [23, 26, 21], 
    [23, 27, 25], 
    [25, 26, 23], 
    [24, 28, 27], 
    [28, 30, 27], 
    [27, 29, 25], 
    [27, 30, 29], 
    [30, 28, 31], 
    [31, 32, 30], 
    [32, 33, 30], 
    [30, 34, 29], 
    [33, 35, 30], 
    [30, 35, 34], 
    [33, 36, 35], 
    [38, 36, 33], 
    [38, 37, 36], 
    [38, 33, 39], 
    [39, 42, 38], 
    [40, 41, 38], 
    [38, 42, 40], 
    [38, 41, 37], 
    [43, 44, 42], 
    [42, 39, 43], 
    [44, 40, 42], 
    [47, 40, 44], 
    [46, 44, 43], 
    [47, 44, 45], 
    [45, 44, 46], 
    [45, 48, 47], 
    [47, 49, 40], 
    [40, 49, 50], 
    [40, 50, 41], 
    [48, 52, 51], 
    [53, 48, 51], 
    [48, 45, 52], 
    [51, 54, 53], 
    [55, 54, 51], 
    [56, 55, 51], 
    [51, 52, 56], 
    [52, 58, 56], 
    [56, 58, 57], 
    [58, 52, 60], 
    [59, 57, 58], 
    [59, 58, 61], 
    [61, 58, 60], 
    [64, 61, 62], 
    [60, 62, 61], 
    [63, 59, 61], 
    [63, 61, 64], 
    [64, 62, 66], 
    [64, 66, 65], 
    [67, 64, 65], 
    [63, 64, 67], 
    [68, 67, 65], 
    [68, 71, 69], 
    [65, 70, 68], 
    [70, 71, 68], 
    [74, 71, 72], 
    [71, 73, 72], 
    [70, 73, 71], 
    [69, 71, 74], 
    [74, 72, 18], 
    [74, 75, 76], 
    [74, 18, 75], 
    [74, 76, 69], 
    [75, 4, 76], 
    [4, 75, 7], 
    [15, 7, 75], 
    [75, 18, 15], 
    [70, 78, 73], 
    [73, 80, 77], 
    [79, 73, 77], 
    [78, 80, 73], 
    [72, 73, 79], 
    [80, 81, 77], 
    [80, 82, 81], 
    [78, 82, 80], 
    [66, 43, 82], 
    [82, 78, 66], 
    [43, 39, 82], 
    [82, 39, 81], 
    [81, 39, 33], 
    [33, 32, 81], 
    [77, 81, 32], 
    [79, 28, 24], 
    [31, 28, 79], 
    [77, 31, 79], 
    [79, 24, 20], 
    [79, 20, 72], 
    [65, 66, 78], 
    [78, 70, 65], 
    [32, 31, 77], 
    [18, 72, 20], 
    [66, 62, 43], 
    [83, 59, 63], 
    [85, 59, 83], 
    [84, 85, 83], 
    [84, 86, 85], 
    [87, 85, 86], 
    [85, 87, 57], 
    [57, 59, 85], 
    [46, 62, 60], 
    [46, 43, 62], 
    [60, 52, 45], 
    [60, 45, 46], 
    [25, 29, 88], 
    [88, 26, 25], 
    [21, 26, 89], 
    [90, 21, 89], 
    [22, 21, 90], 
    [91, 22, 90], 
    [17, 91, 92], 
    [17, 22, 91], 
    [92, 93, 14], 
    [14, 17, 92], 
    [11, 93, 94], 
    [93, 11, 14], 
    [12, 94, 95], 
    [94, 12, 11], 
    [95, 96, 12], 
    [12, 96, 9], 
    [1, 6, 97], 
    [1, 97, 98], 
    [98, 2, 1]
] # PSD_wall_list

PSD = m.GeometryObject(
    name = 'PSD',
    vertex_list = PSD_vertex_list,
    wall_list = PSD_wall_list,
    surface_regions = []
)
# ^^^^ PSD ^^^^

