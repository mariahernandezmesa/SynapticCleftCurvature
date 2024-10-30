import mcell as m

# ---- presynaptic ----
presynaptic_vertex_list = [
    [0.0645657777786255, 0.0809612274169922, 0.0888698101043701], 
    [0.0600618124008179, 0.0647578239440918, 0.06093430519104], 
    [0.0853860378265381, 0.0808510780334473, 0.0640501379966736], 
    [0.0392544269561768, 0.0713639259338379, 0.108048915863037], 
    [0.036986231803894, 0.0622787475585938, 0.0808550119400024], 
    [0.0179784297943115, 0.0419392585754395, 0.0712384581565857], 
    [0.0142854452133179, 0.0472822189331055, 0.0971273183822632], 
    [0.0374988317489624, 0.050199031829834, 0.0580668449401855], 
    [0.0259313583374023, 0.0342164039611816, 0.043932318687439], 
    [0.0557234287261963, 0.0402112007141113, 0.0373857617378235], 
    [0.0358376502990723, 0.019324779510498, 0.0270621180534363], 
    [0.0816804170608521, 0.055182933807373, 0.0430803298950195], 
    [0.058245062828064, 0.0192656517028809, 0.0138139724731445], 
    [0.0849474668502808, 0.0337319374084473, 0.0231555104255676], 
    [0.112663269042969, 0.0431437492370605, 0.0326234102249146], 
    [0.117380142211914, 0.0234909057617188, 0.0106186866760254], 
    [0.0827202796936035, 0.0155348777770996, 0.000747740268707275], 
    [0.0534733533859253, 0.0030827522277832, -0.0105056762695312], 
    [0.0569876432418823, -0.0114588737487793, -0.0347132086753845], 
    [0.0242768526077271, 0.00124216079711914, 0.00725096464157104], 
    [0.028235912322998, -0.0145435333251953, -0.0185456871986389], 
    [0.0317250490188599, -0.022158145904541, -0.0469251275062561], 
    [0.00205254554748535, -0.0218353271484375, -0.00188523530960083], 
    [0.00233876705169678, -0.0370216369628906, -0.0284289121627808], 
    [0.0132871866226196, -0.0394887924194336, -0.0555956959724426], 
    [-0.010941743850708, -0.0609879493713379, -0.0546180605888367], 
    [-0.0227619409561157, -0.043851375579834, -0.00715738534927368], 
    [-0.0244753360748291, -0.0576252937316895, -0.0288578867912292], 
    [-0.042264461517334, -0.0760607719421387, -0.0411848425865173], 
    [-0.0542378425598145, -0.0642647743225098, -0.0132567882537842], 
    [-0.0675877332687378, -0.0607380867004395, 0.0102522969245911], 
    [-0.043906569480896, -0.0507292747497559, 0.0143364667892456], 
    [-0.0928449630737305, -0.0513348579406738, -0.00869864225387573], 
    [-0.0823806524276733, -0.0543303489685059, -0.0319204926490784], 
    [-0.0639915466308594, -0.0731682777404785, -0.0402668714523315], 
    [-0.0833805799484253, -0.0700316429138184, -0.0637105107307434], 
    [-0.0580132007598877, -0.0807862281799316, -0.0610831379890442], 
    [-0.0352733135223389, -0.0797743797302246, -0.0697146654129028], 
    [-0.0619254112243652, -0.0883173942565918, -0.0881654620170593], 
    [-0.0115528106689453, -0.0714583396911621, -0.0824292898178101], 
    [0.00971686840057373, -0.0487942695617676, -0.0781882405281067], 
    [0.0353566408157349, -0.0331988334655762, -0.0751316547393799], 
    [0.0641741752624512, -0.0393433570861816, -0.0867838859558105], 
    [0.0610115528106689, -0.0232653617858887, -0.0612573027610779], 
    [0.0863471031188965, -0.0150070190429688, -0.0461503863334656], 
    [0.0912491083145142, -0.031219482421875, -0.0702310800552368], 
    [-0.0611069202423096, -0.0605340003967285, 0.0374230146408081], 
    [-0.0297361612319946, -0.0307555198669434, 0.0397139191627502], 
    [-0.0206844806671143, -0.0297856330871582, 0.0140448808670044], 
    [-0.00617516040802002, -0.00899934768676758, 0.0245930552482605], 
    [-0.0132697820663452, 0.00292634963989258, 0.0542949438095093], 
    [0.00959193706512451, 0.0133199691772461, 0.0330091714859009], 
    [0.0064232349395752, 0.025275707244873, 0.0557390451431274], 
    [-0.00238358974456787, 0.0236420631408691, 0.0807417035102844], 
    [-0.0223833322525024, 0.000991344451904297, 0.086995542049408], 
    [-0.00979363918304443, 0.0253314971923828, 0.111098408699036], 
    [-0.0344873666763306, -0.00992679595947266, 0.11399918794632], 
    [-0.0486365556716919, -0.0302658081054688, 0.0925377011299133], 
    [-0.030949592590332, -0.0200338363647461, 0.0679277777671814], 
    [-0.0481637716293335, -0.0419802665710449, 0.0623182058334351], 
    [0.106143593788147, 0.0635185241699219, 0.0475172400474548]
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

