import mcell as m

# ---- presynaptic ----
presynaptic_vertex_list = [
    [-0.811677873134613, 1.11891460418701, 0.513201415538788], 
    [-0.806410670280457, 1.14814114570618, 0.517241477966309], 
    [-0.821106970310211, 1.13889050483704, 0.538263022899628], 
    [-0.824249982833862, 1.10889077186584, 0.54136323928833], 
    [-0.793253898620605, 1.13979423046112, 0.493851482868195], 
    [-0.792897462844849, 1.11167788505554, 0.484441459178925], 
    [-0.772015035152435, 1.13264906406403, 0.469107061624527], 
    [-0.774076163768768, 1.15945398807526, 0.485854506492615], 
    [-0.753427028656006, 1.16821134090424, 0.46808522939682], 
    [-0.761336386203766, 1.18946206569672, 0.493990361690521], 
    [-0.732021450996399, 1.1959342956543, 0.472480684518814], 
    [-0.740751504898071, 1.21541285514832, 0.497496426105499], 
    [-0.713800609111786, 1.23309648036957, 0.483981192111969], 
    [-0.703938663005829, 1.26373112201691, 0.503423035144806], 
    [-0.730187475681305, 1.24111247062683, 0.510407388210297], 
    [-0.762206077575684, 1.2194607257843, 0.525653779506683], 
    [-0.725305676460266, 1.26731896400452, 0.526797592639923], 
    [-0.745830893516541, 1.24829518795013, 0.532804012298584], 
    [-0.74590677022934, 1.27062690258026, 0.548215687274933], 
    [-0.766387522220612, 1.24827992916107, 0.551789700984955], 
    [-0.788382053375244, 1.24955308437347, 0.572745203971863], 
    [-0.766602098941803, 1.27726328372955, 0.572132349014282], 
    [-0.786179065704346, 1.22555363178253, 0.555492877960205], 
    [-0.807452142238617, 1.20352923870087, 0.560348987579346], 
    [-0.809465825557709, 1.22729420661926, 0.579131364822388], 
    [-0.790724992752075, 1.20422065258026, 0.538841068744659], 
    [-0.78206342458725, 1.1919641494751, 0.517988622188568], 
    [-0.809400856494904, 1.17492783069611, 0.535890102386475], 
    [-0.831928193569183, 1.15695416927338, 0.559968113899231], 
    [-0.825008034706116, 1.18342232704163, 0.563659071922302], 
    [-0.790608882904053, 1.16798949241638, 0.506475687026978], 
    [-0.828732252120972, 1.20338952541351, 0.584627091884613], 
    [-0.840426206588745, 1.17441713809967, 0.586085498332977], 
    [-0.841643571853638, 1.19311928749084, 0.610669672489166], 
    [-0.843556523323059, 1.16165280342102, 0.610935211181641], 
    [-0.842188596725464, 1.14510333538055, 0.585763454437256], 
    [-0.839487612247467, 1.13491022586823, 0.607335388660431], 
    [-0.84121435880661, 1.11474967002869, 0.589972317218781], 
    [-0.833033978939056, 1.12708139419556, 0.563119351863861], 
    [-0.829279839992523, 1.0971747636795, 0.569714903831482], 
    [-0.827837228775024, 1.14094460010529, 0.632058143615723], 
    [-0.833741188049316, 1.17568695545197, 0.634943664073944], 
    [-0.829792559146881, 1.20559108257294, 0.636133253574371], 
    [-0.830426633358002, 1.22663044929504, 0.61009556055069], 
    [-0.818708300590515, 1.22934794425964, 0.637082993984222], 
    [-0.801929116249084, 1.24457669258118, 0.650965452194214], 
    [-0.814215123653412, 1.2538868188858, 0.626821041107178], 
    [-0.79902982711792, 1.2761607170105, 0.614862143993378], 
    [-0.808870851993561, 1.25168812274933, 0.597412168979645], 
    [-0.797163844108582, 1.27188158035278, 0.644583284854889], 
    [-0.781876564025879, 1.2939168214798, 0.630111217498779], 
    [-0.773928642272949, 1.29384624958038, 0.601212084293365], 
    [-0.755956411361694, 1.31464767456055, 0.619854390621185], 
    [-0.730343401432037, 1.33248221874237, 0.60925555229187], 
    [-0.746624767780304, 1.30794250965118, 0.588837444782257], 
    [-0.742337942123413, 1.29215025901794, 0.563564538955688], 
    [-0.720321953296661, 1.32541477680206, 0.585891902446747], 
    [-0.723092138767242, 1.31129741668701, 0.564582347869873], 
    [-0.699324369430542, 1.31030678749084, 0.548152804374695], 
    [-0.699019134044647, 1.33040904998779, 0.571041941642761], 
    [-0.723084568977356, 1.28980255126953, 0.545920729637146], 
    [-0.703565835952759, 1.28879570960999, 0.527317821979523], 
    [-0.787924945354462, 1.27052652835846, 0.590108335018158]
] # presynaptic_vertex_list

presynaptic_wall_list = [
    [0, 1, 4], 
    [2, 1, 0], 
    [3, 2, 0], 
    [4, 5, 0], 
    [6, 5, 4], 
    [4, 7, 6], 
    [7, 8, 6], 
    [10, 8, 9], 
    [8, 7, 9], 
    [9, 11, 10], 
    [11, 12, 10], 
    [14, 12, 11], 
    [13, 12, 14], 
    [15, 14, 11], 
    [17, 14, 15], 
    [16, 13, 14], 
    [14, 17, 16], 
    [18, 16, 17], 
    [17, 19, 18], 
    [19, 17, 15], 
    [20, 21, 19], 
    [20, 19, 22], 
    [21, 18, 19], 
    [15, 22, 19], 
    [24, 22, 23], 
    [23, 22, 25], 
    [25, 22, 15], 
    [24, 20, 22], 
    [15, 26, 25], 
    [27, 25, 26], 
    [23, 25, 27], 
    [27, 28, 29], 
    [28, 27, 2], 
    [23, 27, 29], 
    [27, 26, 30], 
    [27, 30, 1], 
    [1, 2, 27], 
    [1, 30, 4], 
    [26, 9, 30], 
    [9, 7, 30], 
    [30, 7, 4], 
    [29, 28, 32], 
    [31, 29, 32], 
    [23, 29, 31], 
    [32, 33, 31], 
    [34, 33, 32], 
    [32, 35, 34], 
    [32, 28, 35], 
    [35, 36, 34], 
    [36, 35, 37], 
    [38, 37, 35], 
    [35, 28, 38], 
    [2, 38, 28], 
    [39, 38, 3], 
    [38, 39, 37], 
    [2, 3, 38], 
    [40, 34, 36], 
    [34, 40, 41], 
    [33, 34, 41], 
    [41, 42, 33], 
    [44, 43, 42], 
    [42, 43, 33], 
    [43, 44, 46], 
    [46, 44, 45], 
    [46, 48, 43], 
    [47, 48, 46], 
    [46, 49, 47], 
    [45, 49, 46], 
    [50, 47, 49], 
    [51, 47, 50], 
    [50, 52, 51], 
    [52, 53, 54], 
    [54, 51, 52], 
    [55, 54, 57], 
    [21, 54, 55], 
    [54, 21, 51], 
    [53, 56, 54], 
    [56, 57, 54], 
    [58, 57, 59], 
    [58, 60, 57], 
    [56, 59, 57], 
    [57, 60, 55], 
    [60, 58, 61], 
    [61, 16, 60], 
    [18, 60, 16], 
    [55, 60, 18], 
    [61, 13, 16], 
    [55, 18, 21], 
    [47, 51, 62], 
    [51, 21, 62], 
    [62, 20, 48], 
    [62, 21, 20], 
    [62, 48, 47], 
    [43, 48, 24], 
    [20, 24, 48], 
    [43, 31, 33], 
    [24, 31, 43], 
    [31, 24, 23], 
    [15, 9, 26], 
    [15, 11, 9]
] # presynaptic_wall_list

presynaptic = m.GeometryObject(
    name = 'presynaptic',
    vertex_list = presynaptic_vertex_list,
    wall_list = presynaptic_wall_list,
    surface_regions = []
)
# ^^^^ presynaptic ^^^^

