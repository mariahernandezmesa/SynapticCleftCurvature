import mcell as m

# ---- PSD ----
PSD_vertex_list = [
    [1.81183886528015, 0.0866881906986237, 1.02742612361908], 
    [1.82131576538086, 0.0925753489136696, 1.00519800186157], 
    [1.80636739730835, 0.0609497874975204, 1.0440765619278], 
    [1.79841792583466, 0.0679218173027039, 1.01134312152863], 
    [1.77782428264618, 0.0354189276695251, 0.996250092983246], 
    [1.79080498218536, 0.0595334470272064, 0.984336972236633], 
    [1.81067848205566, 0.0802130699157715, 0.980488896369934], 
    [1.78980326652527, 0.0403208881616592, 1.02188897132874], 
    [1.77458834648132, 0.011818952858448, 1.01736676692963], 
    [1.78969395160675, 0.0178389325737953, 1.04008913040161], 
    [1.80526232719421, 0.0308353304862976, 1.06227076053619], 
    [1.77041685581207, -0.0124455019831657, 1.03525531291962], 
    [1.79026198387146, -0.00516518205404282, 1.06056392192841], 
    [1.76975405216217, -0.0344790518283844, 1.0550502538681], 
    [1.7491614818573, -0.0378269031643867, 1.03355383872986], 
    [1.73952078819275, -0.0657137334346771, 1.05165755748749], 
    [1.70077168941498, -0.0799311846494675, 1.03049182891846], 
    [1.72262001037598, -0.0524976924061775, 1.01850187778473], 
    [1.71267402172089, -0.0899219587445259, 1.06201708316803], 
    [1.68804001808167, -0.0929819270968437, 1.05227506160736], 
    [1.67778611183167, -0.10307864844799, 1.03713750839233], 
    [1.67536222934723, -0.1165626719594, 1.00730109214783], 
    [1.65642917156219, -0.1170609369874, 1.04052329063416], 
    [1.64492380619049, -0.136378258466721, 1.02811253070831], 
    [1.61493599414825, -0.149613857269287, 1.02614283561707], 
    [1.64323008060455, -0.158025711774826, 1.01096498966217], 
    [1.61492812633514, -0.175674170255661, 1.01105117797852], 
    [1.63534665107727, -0.176670581102371, 0.992598712444305], 
    [1.65386462211609, -0.15569880604744, 0.981696486473083], 
    [1.64432525634766, -0.159238561987877, 0.952099621295929], 
    [1.66479301452637, -0.12805849313736, 0.969567120075226], 
    [1.63141477108002, -0.184366077184677, 0.965298295021057], 
    [1.6127690076828, -0.192885920405388, 0.988977789878845], 
    [1.6081063747406, -0.204492390155792, 0.967992544174194], 
    [1.66640603542328, -0.112511202692986, 0.948948204517365], 
    [1.6783127784729, -0.0991668552160263, 0.974642157554626], 
    [1.65315532684326, -0.135279551148415, 0.941328823566437], 
    [1.63629710674286, -0.152759611606598, 0.920418560504913], 
    [1.65331518650055, -0.12174978107214, 0.918768703937531], 
    [1.65272188186646, -0.110804848372936, 0.885789930820465], 
    [1.66120672225952, -0.0995483696460724, 0.910772442817688], 
    [1.66533184051514, -0.0981999635696411, 0.931133031845093], 
    [1.64255809783936, -0.136305540800095, 0.898636221885681], 
    [1.67220449447632, -0.0769951120018959, 0.924160897731781], 
    [1.67582809925079, -0.0849194154143333, 0.948895335197449], 
    [1.68765223026276, -0.0728036090731621, 0.96750408411026], 
    [1.69142758846283, -0.0544373691082001, 0.941436290740967], 
    [1.68260598182678, -0.0580438524484634, 0.910982131958008], 
    [1.7107766866684, -0.017328716814518, 0.931603312492371], 
    [1.70134389400482, -0.0527699887752533, 0.970966339111328], 
    [1.70907700061798, -0.0319594219326973, 0.957872867584229], 
    [1.69834434986115, -0.0391277968883514, 0.91514128446579], 
    [1.69470143318176, -0.0446225553750992, 0.88818770647049], 
    [1.71141993999481, -0.0232144072651863, 0.900429964065552], 
    [1.71133506298065, -0.0255009233951569, 0.873552441596985], 
    [1.72920310497284, -0.00775859504938126, 0.885964870452881], 
    [1.72461187839508, -0.00322326272726059, 0.910545885562897], 
    [1.73715782165527, 0.0106673240661621, 0.931513845920563], 
    [1.74729013442993, 0.00818216800689697, 0.901232004165649], 
    [1.77033793926239, 0.0157922431826591, 0.888542890548706], 
    [1.76733541488647, 0.0265337377786636, 0.913707494735718], 
    [1.75354409217834, 0.000728406012058258, 0.875567018985748], 
    [1.79262840747833, 0.0507150068879128, 0.909285128116608], 
    [1.778404712677, 0.0443699285387993, 0.92837256193161], 
    [1.7612988948822, 0.0293453112244606, 0.945961594581604], 
    [1.79135644435883, 0.0329405143857002, 0.887439012527466], 
    [1.78183567523956, 0.0498523563146591, 0.948080539703369], 
    [1.77639555931091, 0.0431833863258362, 0.969971597194672], 
    [1.75857126712799, 0.0235414579510689, 0.975027441978455], 
    [1.74255466461182, 0.0114227309823036, 0.958735048770905], 
    [1.72364294528961, -0.00813835114240646, 0.958563089370728], 
    [1.73969113826752, -0.0046813115477562, 0.982261717319489], 
    [1.75929844379425, 0.00885997712612152, 0.995977282524109], 
    [1.72121667861938, -0.0338615328073502, 0.988320887088776], 
    [1.74741780757904, -0.0194233655929565, 1.008953332901], 
    [1.69623970985413, -0.0726800039410591, 0.997559249401093], 
    [1.79516518115997, 0.0665522366762161, 0.959658801555634], 
    [1.79649615287781, 0.064117819070816, 0.932265877723694], 
    [1.68209421634674, -0.0634639412164688, 0.869081497192383], 
    [1.67925906181335, -0.0662372559309006, 0.889122486114502], 
    [1.66689884662628, -0.087309829890728, 0.871361553668976], 
    [1.66813373565674, -0.0832691863179207, 0.89778333902359]
] # PSD_vertex_list

PSD_wall_list = [
    [0, 3, 1], 
    [2, 3, 0], 
    [3, 7, 4], 
    [4, 5, 3], 
    [3, 6, 1], 
    [5, 6, 3], 
    [3, 2, 7], 
    [7, 8, 4], 
    [7, 9, 8], 
    [9, 7, 2], 
    [9, 11, 8], 
    [10, 9, 2], 
    [10, 12, 9], 
    [9, 12, 11], 
    [13, 11, 12], 
    [11, 13, 14], 
    [13, 15, 14], 
    [15, 18, 16], 
    [16, 17, 15], 
    [17, 14, 15], 
    [18, 19, 16], 
    [16, 19, 20], 
    [16, 20, 21], 
    [21, 20, 22], 
    [21, 22, 23], 
    [23, 24, 25], 
    [23, 25, 21], 
    [25, 24, 26], 
    [27, 25, 26], 
    [25, 27, 28], 
    [25, 28, 21], 
    [29, 30, 28], 
    [28, 31, 29], 
    [21, 28, 30], 
    [28, 27, 31], 
    [27, 32, 31], 
    [33, 31, 32], 
    [26, 32, 27], 
    [30, 35, 21], 
    [30, 36, 34], 
    [34, 35, 30], 
    [36, 30, 29], 
    [38, 36, 37], 
    [34, 36, 38], 
    [38, 42, 39], 
    [38, 39, 40], 
    [40, 41, 38], 
    [37, 42, 38], 
    [41, 34, 38], 
    [40, 43, 41], 
    [44, 34, 41], 
    [44, 41, 43], 
    [35, 44, 45], 
    [34, 44, 35], 
    [45, 44, 46], 
    [46, 44, 43], 
    [46, 43, 47], 
    [47, 51, 46], 
    [50, 46, 48], 
    [46, 51, 48], 
    [49, 46, 50], 
    [46, 49, 45], 
    [47, 52, 51], 
    [51, 52, 53], 
    [53, 48, 51], 
    [53, 52, 54], 
    [54, 55, 53], 
    [56, 53, 55], 
    [48, 53, 56], 
    [56, 58, 57], 
    [57, 48, 56], 
    [56, 55, 58], 
    [61, 58, 55], 
    [60, 58, 59], 
    [59, 58, 61], 
    [58, 60, 57], 
    [59, 65, 60], 
    [60, 62, 63], 
    [60, 65, 62], 
    [63, 64, 60], 
    [57, 60, 64], 
    [63, 66, 64], 
    [66, 67, 64], 
    [68, 64, 67], 
    [68, 69, 64], 
    [69, 57, 64], 
    [70, 57, 69], 
    [70, 69, 71], 
    [69, 68, 71], 
    [72, 74, 71], 
    [71, 68, 72], 
    [73, 70, 71], 
    [71, 74, 73], 
    [73, 74, 17], 
    [74, 14, 17], 
    [8, 74, 72], 
    [8, 11, 74], 
    [74, 11, 14], 
    [17, 75, 73], 
    [75, 49, 73], 
    [50, 70, 73], 
    [73, 49, 50], 
    [21, 75, 16], 
    [21, 35, 75], 
    [45, 49, 75], 
    [75, 35, 45], 
    [75, 17, 16], 
    [4, 8, 72], 
    [72, 68, 4], 
    [57, 70, 48], 
    [48, 70, 50], 
    [4, 68, 67], 
    [5, 67, 76], 
    [67, 66, 76], 
    [67, 5, 4], 
    [77, 76, 66], 
    [76, 6, 5], 
    [77, 63, 62], 
    [66, 63, 77], 
    [52, 79, 78], 
    [79, 52, 47], 
    [79, 80, 78], 
    [81, 80, 79], 
    [81, 79, 47], 
    [39, 80, 81], 
    [40, 39, 81], 
    [81, 43, 40], 
    [47, 43, 81]
] # PSD_wall_list

PSD = m.GeometryObject(
    name = 'PSD',
    vertex_list = PSD_vertex_list,
    wall_list = PSD_wall_list,
    surface_regions = []
)
# ^^^^ PSD ^^^^

