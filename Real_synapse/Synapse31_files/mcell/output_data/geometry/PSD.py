import mcell as m

# ---- PSD ----
PSD_vertex_list = [
    [0.0545657873153687, 0.0909614562988281, 0.0788698196411133], 
    [0.050061821937561, 0.0747580528259277, 0.0509343147277832], 
    [0.0753860473632812, 0.0908513069152832, 0.0540501475334167], 
    [0.0292544364929199, 0.0813641548156738, 0.0980489253997803], 
    [0.0269862413406372, 0.0722789764404297, 0.0708550214767456], 
    [0.00797843933105469, 0.0519394874572754, 0.0612384676933289], 
    [0.00428545475006104, 0.0572824478149414, 0.0871273279190063], 
    [0.0274988412857056, 0.0601992607116699, 0.0480668544769287], 
    [0.0159313678741455, 0.0442166328430176, 0.0339323282241821], 
    [0.0457234382629395, 0.0502114295959473, 0.0273857712745667], 
    [0.0258376598358154, 0.029325008392334, 0.0170621275901794], 
    [0.0716804265975952, 0.065183162689209, 0.0330803394317627], 
    [0.0482450723648071, 0.0292658805847168, 0.0038139820098877], 
    [0.0749474763870239, 0.0437321662902832, 0.0131555199623108], 
    [0.102663278579712, 0.0531439781188965, 0.0226234197616577], 
    [0.107380151748657, 0.0334911346435547, 0.000618696212768555], 
    [0.0727202892303467, 0.0255351066589355, -0.00925225019454956], 
    [0.0434733629226685, 0.0130829811096191, -0.0205056667327881], 
    [0.0469876527786255, -0.00145864486694336, -0.0447131991386414], 
    [0.0142768621444702, 0.0112423896789551, -0.00274902582168579], 
    [0.0182359218597412, -0.00454330444335938, -0.0285456776618958], 
    [0.021725058555603, -0.0121579170227051, -0.0569251179695129], 
    [-0.00794744491577148, -0.0118350982666016, -0.0118852257728577], 
    [-0.00766122341156006, -0.0270214080810547, -0.0384289026260376], 
    [0.00328719615936279, -0.0294885635375977, -0.0655956864356995], 
    [-0.0209417343139648, -0.050987720489502, -0.0646180510520935], 
    [-0.0327619314193726, -0.033851146697998, -0.0171573758125305], 
    [-0.0344753265380859, -0.0476250648498535, -0.0388578772544861], 
    [-0.0522644519805908, -0.0660605430603027, -0.0511848330497742], 
    [-0.0642378330230713, -0.0542645454406738, -0.023256778717041], 
    [-0.0775877237319946, -0.0507378578186035, 0.000252306461334229], 
    [-0.0539065599441528, -0.0407290458679199, 0.00433647632598877], 
    [-0.102844953536987, -0.0413346290588379, -0.0186986327171326], 
    [-0.0923806428909302, -0.0443301200866699, -0.0419204831123352], 
    [-0.0739915370941162, -0.0631680488586426, -0.0502668619155884], 
    [-0.0933805704116821, -0.0600314140319824, -0.0737105011940002], 
    [-0.0680131912231445, -0.0707859992980957, -0.071083128452301], 
    [-0.0452733039855957, -0.0697741508483887, -0.0797146558761597], 
    [-0.0719254016876221, -0.0783171653747559, -0.0981654524803162], 
    [-0.0215528011322021, -0.0614581108093262, -0.0924292802810669], 
    [-0.000283122062683105, -0.0387940406799316, -0.0881882309913635], 
    [0.025356650352478, -0.0231986045837402, -0.0851316452026367], 
    [0.0541741847991943, -0.0293431282043457, -0.0967838764190674], 
    [0.0510115623474121, -0.0132651329040527, -0.0712572932243347], 
    [0.0763471126556396, -0.00500679016113281, -0.0561503767967224], 
    [0.0812491178512573, -0.0212192535400391, -0.0802310705184937], 
    [-0.0711069107055664, -0.0505337715148926, 0.0274230241775513], 
    [-0.0397361516952515, -0.0207552909851074, 0.0297139286994934], 
    [-0.0306844711303711, -0.0197854042053223, 0.00404489040374756], 
    [-0.0161751508712769, 0.00100088119506836, 0.0145930647850037], 
    [-0.0232697725296021, 0.0129265785217285, 0.0442949533462524], 
    [-0.000408053398132324, 0.023320198059082, 0.023009181022644], 
    [-0.00357675552368164, 0.035275936126709, 0.0457390546798706], 
    [-0.0123835802078247, 0.0336422920227051, 0.0707417130470276], 
    [-0.0323833227157593, 0.0109915733337402, 0.0769955515861511], 
    [-0.0197936296463013, 0.0353317260742188, 0.101098418235779], 
    [-0.0444873571395874, 7.34329223632812e-05, 0.103999197483063], 
    [-0.0586365461349487, -0.0202655792236328, 0.0825377106666565], 
    [-0.0409495830535889, -0.0100336074829102, 0.0579277873039246], 
    [-0.0581637620925903, -0.031980037689209, 0.0523182153701782], 
    [0.0961436033248901, 0.0735187530517578, 0.037517249584198]
] # PSD_vertex_list

PSD_wall_list = [
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
] # PSD_wall_list

PSD = m.GeometryObject(
    name = 'PSD',
    vertex_list = PSD_vertex_list,
    wall_list = PSD_wall_list,
    surface_regions = []
)
# ^^^^ PSD ^^^^

