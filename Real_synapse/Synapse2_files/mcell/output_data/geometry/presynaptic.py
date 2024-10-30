import mcell as m

# ---- presynaptic ----
presynaptic_vertex_list = [
    [2.03977012634277, -2.42879819869995, -0.785315871238708], 
    [2.0247631072998, -2.40109467506409, -0.798568248748779], 
    [2.05465197563171, -2.40338587760925, -0.798279702663422], 
    [2.01291418075562, -2.44715785980225, -0.785581469535828], 
    [1.97714781761169, -2.45248341560364, -0.796699941158295], 
    [1.99083805084229, -2.41236233711243, -0.802327156066895], 
    [2.00304198265076, -2.37755298614502, -0.805799424648285], 
    [1.95459985733032, -2.40496325492859, -0.819365262985229], 
    [1.9753851890564, -2.375244140625, -0.818431973457336], 
    [1.96961224079132, -2.34498357772827, -0.829554557800293], 
    [1.94896483421326, -2.36181855201721, -0.833925306797028], 
    [1.92437767982483, -2.34133005142212, -0.848398745059967], 
    [1.94943904876709, -2.32474422454834, -0.84315413236618], 
    [1.92253792285919, -2.37840914726257, -0.840444564819336], 
    [1.89643442630768, -2.35604000091553, -0.851778268814087], 
    [1.92292165756226, -2.41213154792786, -0.830281794071198], 
    [1.89644908905029, -2.39463257789612, -0.848281383514404], 
    [1.87044656276703, -2.37180423736572, -0.861139595508575], 
    [1.90201687812805, -2.43894004821777, -0.835963189601898], 
    [1.87044847011566, -2.41075849533081, -0.865323305130005], 
    [1.87277865409851, -2.44719290733337, -0.859628677368164], 
    [1.83918595314026, -2.39895033836365, -0.891669154167175], 
    [1.84854364395142, -2.38246917724609, -0.871527194976807], 
    [1.85013782978058, -2.42567610740662, -0.889150619506836], 
    [1.85250544548035, -2.45328259468079, -0.882471799850464], 
    [1.83554875850677, -2.43100333213806, -0.91975337266922], 
    [1.82896435260773, -2.40600538253784, -0.918013095855713], 
    [1.84220159053802, -2.4532585144043, -0.912853002548218], 
    [1.84475469589233, -2.46959137916565, -0.897884011268616], 
    [1.83532762527466, -2.44778966903687, -0.939163744449615], 
    [1.8312554359436, -2.4813928604126, -0.925519824028015], 
    [1.84078705310822, -2.49022817611694, -0.891762435436249], 
    [1.82967126369476, -2.50585103034973, -0.905931770801544], 
    [1.81578516960144, -2.5183310508728, -0.930120408535004], 
    [1.83081412315369, -2.46849060058594, -0.953801989555359], 
    [1.82156050205231, -2.49347233772278, -0.955913662910461], 
    [1.80875289440155, -2.51683735847473, -0.963834464550018], 
    [1.79548895359039, -2.53478455543518, -0.975954651832581], 
    [1.80341267585754, -2.54555773735046, -0.946567177772522], 
    [1.81597101688385, -2.54794359207153, -0.908802390098572], 
    [1.78750443458557, -2.57893538475037, -0.949632883071899], 
    [1.78815197944641, -2.55717277526855, -0.972236096858978], 
    [1.80401492118835, -2.56821703910828, -0.923945188522339], 
    [1.82611155509949, -2.58005285263062, -0.894168257713318], 
    [1.80422079563141, -2.5957145690918, -0.921920239925385], 
    [1.80718290805817, -2.62341380119324, -0.920418441295624], 
    [1.82428479194641, -2.60827159881592, -0.901791870594025], 
    [1.78744757175446, -2.61100816726685, -0.94275039434433], 
    [1.78829109668732, -2.64185380935669, -0.937596380710602], 
    [1.77375316619873, -2.60060548782349, -0.968328952789307], 
    [1.77320683002472, -2.57539343833923, -0.989740610122681], 
    [1.80087339878082, -2.66980576515198, -0.925535202026367], 
    [1.81948781013489, -2.65049290657043, -0.911480844020844], 
    [1.78067326545715, -2.66727137565613, -0.945428550243378], 
    [1.78180015087128, -2.69140458106995, -0.941302299499512], 
    [1.80853879451752, -2.69507122039795, -0.916970610618591], 
    [1.83038139343262, -2.67815852165222, -0.903519570827484], 
    [1.85643565654755, -2.68870711326599, -0.879143893718719], 
    [1.85054612159729, -2.65947651863098, -0.885773420333862], 
    [1.880335688591, -2.6696982383728, -0.860523641109467], 
    [1.83742213249207, -2.6328718662262, -0.892954587936401], 
    [1.8688188791275, -2.63750004768372, -0.867368698120117], 
    [1.85084283351898, -2.60908794403076, -0.878914177417755], 
    [1.90864181518555, -2.64462399482727, -0.841195344924927], 
    [1.88493120670319, -2.61001229286194, -0.855241119861603], 
    [1.89603841304779, -2.58124136924744, -0.844014346599579], 
    [1.86314511299133, -2.58106803894043, -0.866847038269043], 
    [1.91675531864166, -2.60959076881409, -0.834333777427673], 
    [1.94311153888702, -2.58018231391907, -0.815569519996643], 
    [1.95108234882355, -2.53235936164856, -0.807924628257751], 
    [1.90042197704315, -2.54764556884766, -0.838927268981934], 
    [1.91488099098206, -2.51584148406982, -0.825878620147705], 
    [1.89216375350952, -2.48005199432373, -0.83950400352478], 
    [1.87825763225555, -2.51469612121582, -0.850651502609253], 
    [1.92921018600464, -2.48363327980042, -0.817513883113861], 
    [1.94060349464417, -2.44459629058838, -0.815232992172241], 
    [1.96768045425415, -2.49572014808655, -0.795870661735535], 
    [1.84711456298828, -2.50735998153687, -0.875227570533752], 
    [1.87437927722931, -2.55215764045715, -0.858142733573914], 
    [1.86193931102753, -2.48016571998596, -0.865852832794189], 
    [1.8535703420639, -2.53255343437195, -0.868881702423096], 
    [1.8296138048172, -2.52857279777527, -0.890667080879211], 
    [1.84106838703156, -2.55542969703674, -0.879601359367371], 
    [1.90973508358002, -2.68322348594666, -0.844665348529816], 
    [1.92122793197632, -2.71761298179626, -0.844347357749939], 
    [1.88434290885925, -2.70413565635681, -0.860353946685791], 
    [1.87695217132568, -2.74447274208069, -0.867551386356354], 
    [1.85688734054565, -2.71764993667603, -0.876476168632507], 
    [1.83076453208923, -2.41885924339294, -0.949572622776031], 
    [1.81232130527496, -2.3786838054657, -0.912583768367767], 
    [1.82879137992859, -2.37422895431519, -0.886248409748077], 
    [1.83720862865448, -2.35470175743103, -0.866371512413025], 
    [1.8657341003418, -2.33309602737427, -0.859264254570007], 
    [1.90023517608643, -2.32009339332581, -0.857774496078491], 
    [1.92937505245209, -2.30217385292053, -0.854304373264313], 
    [1.96140587329865, -2.28767395019531, -0.848792970180511], 
    [1.97407865524292, -2.31886005401611, -0.83623743057251], 
    [2.02735018730164, -2.35990643501282, -0.813490450382233], 
    [2.05024766921997, -2.37737679481506, -0.807763576507568]
] # presynaptic_vertex_list

presynaptic_wall_list = [
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
] # presynaptic_wall_list

presynaptic = m.GeometryObject(
    name = 'presynaptic',
    vertex_list = presynaptic_vertex_list,
    wall_list = presynaptic_wall_list,
    surface_regions = []
)
# ^^^^ presynaptic ^^^^

