import mcell as m

# ---- presynaptic ----
presynaptic_vertex_list = [
    [0.0158307552337646, -0.150431156158447, -0.109250426292419], 
    [0.0314400196075439, -0.115808010101318, -0.111905694007874], 
    [-0.00341463088989258, -0.163303852081299, -0.0956102609634399], 
    [0.0073699951171875, -0.134719371795654, -0.0919606685638428], 
    [-0.0150948762893677, -0.14335298538208, -0.0752432346343994], 
    [0.00699543952941895, -0.109336376190186, -0.0749118328094482], 
    [0.0174758434295654, -0.0759310722351074, -0.0658535957336426], 
    [-0.0229315757751465, -0.124299049377441, -0.0519484281539917], 
    [0.0280835628509521, -0.0862984657287598, -0.0926779508590698], 
    [-0.00678205490112305, -0.0954556465148926, -0.0487546920776367], 
    [0.00268399715423584, -0.0702457427978516, -0.0400645732879639], 
    [-0.0307261943817139, -0.104970932006836, -0.032623291015625], 
    [-0.0208911895751953, -0.0798311233520508, -0.024491548538208], 
    [-0.00735235214233398, -0.0508503913879395, -0.0174754858016968], 
    [-0.0401252508163452, -0.0650649070739746, -0.00528311729431152], 
    [-0.04975426197052, -0.094548225402832, -0.0134708881378174], 
    [-0.0711681842803955, -0.0767979621887207, 0.00411403179168701], 
    [-0.0542867183685303, -0.126823425292969, -0.0295339822769165], 
    [-0.0779016017913818, -0.109196662902832, -0.00597786903381348], 
    [-0.102556943893433, -0.0879988670349121, 0.011772632598877], 
    [-0.0934524536132812, -0.051398754119873, 0.0182182788848877], 
    [-0.0778307914733887, -0.0230050086975098, 0.0195740461349487], 
    [-0.107128620147705, -0.0199317932128906, 0.0301835536956787], 
    [-0.0615037679672241, -0.0467972755432129, 0.00845587253570557], 
    [-0.0311377048492432, -0.0362467765808105, 0.00075232982635498], 
    [-0.0513839721679688, -0.0203523635864258, 0.0118628740310669], 
    [-0.0569758415222168, 0.00975513458251953, 0.0212377309799194], 
    [-0.0292209386825562, -0.00573539733886719, 0.00708699226379395], 
    [-0.00557756423950195, 0.011357307434082, -0.000339627265930176], 
    [-0.00704777240753174, -0.0193819999694824, -0.00649917125701904], 
    [-0.0267987251281738, 0.021052360534668, 0.0127471685409546], 
    [-0.0336571931838989, 0.0441584587097168, 0.0247857570648193], 
    [-0.00578200817108154, 0.0467591285705566, 0.0104067325592041], 
    [0.0125987529754639, 0.0778722763061523, 0.0102090835571289], 
    [0.0187914371490479, 0.0554733276367188, -0.00365185737609863], 
    [0.0154529809951782, 0.0288558006286621, -0.00865983963012695], 
    [-0.0190533399581909, 0.076502799987793, 0.0315433740615845], 
    [-0.0147727727890015, 0.108504772186279, 0.0373160839080811], 
    [-0.0490114688873291, 0.0598278045654297, 0.0376206636428833], 
    [-0.0558823347091675, 0.0827827453613281, 0.0476251840591431], 
    [-0.0391991138458252, 0.105583667755127, 0.0474371910095215], 
    [0.00780630111694336, 0.104270458221436, 0.023045539855957], 
    [-2.72989273071289e-05, 0.130558967590332, 0.0361870527267456], 
    [0.0204137563705444, 0.129302978515625, 0.0216667652130127], 
    [0.0361911058425903, 0.112108707427979, 0.000433087348937988], 
    [0.0380159616470337, 0.147945880889893, 0.0151726007461548], 
    [0.0570098161697388, 0.14661979675293, -0.00265657901763916], 
    [0.0380558967590332, 0.0764980316162109, -0.0112454891204834], 
    [0.062839150428772, 0.127285480499268, -0.0212479829788208], 
    [0.0564452409744263, 0.0974330902099609, -0.0244419574737549], 
    [0.0567202568054199, 0.0640487670898438, -0.0380711555480957], 
    [0.0693506002426147, 0.0898528099060059, -0.0486336946487427], 
    [0.0768190622329712, 0.0690441131591797, -0.0733665227890015], 
    [0.0586986541748047, 0.0389270782470703, -0.0603243112564087], 
    [0.0449610948562622, 0.0355253219604492, -0.0402292013168335], 
    [0.0450443029403687, 0.0100321769714355, -0.0532891750335693], 
    [0.0573303699493408, 0.00924110412597656, -0.0794581174850464], 
    [0.0423970222473145, -0.0193314552307129, -0.0704149007797241], 
    [0.0377802848815918, -0.0508418083190918, -0.0895853042602539], 
    [0.022769570350647, -0.0442829132080078, -0.0522761344909668], 
    [0.0296634435653687, -0.0119857788085938, -0.041562557220459], 
    [0.0122840404510498, -0.0268144607543945, -0.0244965553283691], 
    [0.0309658050537109, 0.0169076919555664, -0.0293282270431519], 
    [0.0139758586883545, -0.000646591186523438, -0.0167243480682373], 
    [0.0351376533508301, 0.0471978187561035, -0.0206643342971802], 
    [0.0184612274169922, 0.156816005706787, 0.0370099544525146], 
    [-0.00702071189880371, 0.153290748596191, 0.0511436462402344], 
    [0.00840401649475098, 0.174017429351807, 0.0629246234893799], 
    [-0.0183882713317871, 0.173233509063721, 0.0750400424003601], 
    [-0.0336973667144775, 0.155116081237793, 0.0615741014480591], 
    [-0.0506629943847656, 0.12968921661377, 0.0591369867324829], 
    [-0.0245704650878906, 0.130851745605469, 0.0484724044799805], 
    [-0.067180871963501, 0.105856895446777, 0.0589016079902649], 
    [-0.0820791721343994, 0.0835151672363281, 0.0574472546577454], 
    [-0.0790822505950928, 0.0577750205993652, 0.0452274084091187], 
    [-0.0859463214874268, 0.0279378890991211, 0.0349239110946655], 
    [-0.061518669128418, 0.0388875007629395, 0.0327408313751221], 
    [-0.0882244110107422, 0.0013422966003418, 0.0289123058319092], 
    [-0.0422617197036743, -0.15408992767334, -0.0570160150527954], 
    [-0.0251966714859009, -0.17349910736084, -0.0816836357116699]
] # presynaptic_vertex_list

presynaptic_wall_list = [
    [3, 1, 0], 
    [0, 2, 3], 
    [4, 3, 2], 
    [3, 4, 5], 
    [1, 3, 5], 
    [5, 6, 8], 
    [9, 6, 5], 
    [7, 5, 4], 
    [9, 5, 7], 
    [5, 8, 1], 
    [9, 7, 11], 
    [10, 6, 9], 
    [12, 10, 9], 
    [9, 11, 12], 
    [12, 11, 15], 
    [13, 12, 14], 
    [12, 13, 10], 
    [14, 12, 15], 
    [15, 16, 14], 
    [18, 16, 15], 
    [15, 17, 18], 
    [15, 11, 17], 
    [16, 18, 19], 
    [19, 20, 16], 
    [23, 20, 21], 
    [22, 21, 20], 
    [20, 23, 16], 
    [16, 23, 14], 
    [23, 24, 14], 
    [25, 24, 23], 
    [21, 25, 23], 
    [25, 21, 26], 
    [27, 25, 26], 
    [25, 27, 24], 
    [24, 27, 29], 
    [28, 29, 27], 
    [30, 28, 27], 
    [26, 30, 27], 
    [32, 28, 30], 
    [32, 30, 31], 
    [30, 26, 31], 
    [32, 35, 28], 
    [36, 33, 32], 
    [33, 34, 32], 
    [34, 35, 32], 
    [31, 36, 32], 
    [41, 33, 36], 
    [41, 36, 37], 
    [40, 37, 36], 
    [36, 38, 39], 
    [36, 31, 38], 
    [39, 40, 36], 
    [37, 42, 41], 
    [41, 42, 43], 
    [41, 43, 44], 
    [41, 44, 33], 
    [45, 44, 43], 
    [46, 44, 45], 
    [44, 46, 48], 
    [33, 44, 47], 
    [49, 47, 44], 
    [44, 48, 49], 
    [47, 49, 50], 
    [50, 49, 51], 
    [52, 50, 51], 
    [53, 50, 52], 
    [54, 53, 55], 
    [50, 53, 54], 
    [56, 55, 53], 
    [57, 55, 56], 
    [60, 55, 57], 
    [58, 59, 57], 
    [59, 60, 57], 
    [61, 60, 59], 
    [60, 61, 63], 
    [62, 55, 60], 
    [63, 62, 60], 
    [28, 35, 63], 
    [62, 63, 35], 
    [63, 29, 28], 
    [29, 63, 61], 
    [62, 54, 55], 
    [64, 54, 62], 
    [64, 62, 35], 
    [64, 50, 54], 
    [47, 50, 64], 
    [34, 47, 64], 
    [64, 35, 34], 
    [61, 13, 29], 
    [13, 61, 59], 
    [6, 59, 58], 
    [59, 6, 10], 
    [59, 10, 13], 
    [6, 58, 8], 
    [47, 34, 33], 
    [65, 45, 43], 
    [67, 65, 66], 
    [66, 65, 42], 
    [65, 43, 42], 
    [67, 66, 68], 
    [68, 66, 69], 
    [70, 69, 71], 
    [66, 71, 69], 
    [42, 71, 66], 
    [71, 40, 70], 
    [37, 40, 71], 
    [42, 37, 71], 
    [72, 70, 40], 
    [73, 72, 39], 
    [72, 40, 39], 
    [74, 73, 39], 
    [75, 74, 76], 
    [39, 38, 74], 
    [38, 76, 74], 
    [31, 76, 38], 
    [76, 26, 75], 
    [76, 31, 26], 
    [75, 26, 77], 
    [21, 22, 77], 
    [77, 26, 21], 
    [29, 13, 24], 
    [24, 13, 14], 
    [17, 11, 7], 
    [17, 7, 78], 
    [7, 4, 78], 
    [4, 79, 78], 
    [2, 79, 4]
] # presynaptic_wall_list

presynaptic = m.GeometryObject(
    name = 'presynaptic',
    vertex_list = presynaptic_vertex_list,
    wall_list = presynaptic_wall_list,
    surface_regions = []
)
# ^^^^ presynaptic ^^^^


