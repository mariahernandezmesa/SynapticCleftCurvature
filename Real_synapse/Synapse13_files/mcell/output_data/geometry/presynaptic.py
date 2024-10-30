import mcell as m

# ---- presynaptic ----
presynaptic_vertex_list = [
    [-1.62300884723663, -2.21427226066589, 0.0882623568177223], 
    [-1.62893581390381, -2.24367117881775, 0.0929066017270088], 
    [-1.59377861022949, -2.22108197212219, 0.0818718448281288], 
    [-1.63445782661438, -2.18700242042542, 0.0914026573300362], 
    [-1.65465044975281, -2.22615790367126, 0.101982839405537], 
    [-1.67335474491119, -2.25074529647827, 0.126356914639473], 
    [-1.66212522983551, -2.19179725646973, 0.105173863470554], 
    [-1.6816611289978, -2.22054696083069, 0.124298878014088], 
    [-1.64871060848236, -2.26201391220093, 0.108879067003727], 
    [-1.63774275779724, -2.29268598556519, 0.116924084722996], 
    [-1.66022527217865, -2.28039526939392, 0.133029744029045], 
    [-1.62235760688782, -2.27458453178406, 0.0984214618802071], 
    [-1.60357093811035, -2.25483322143555, 0.0875115767121315], 
    [-1.59328079223633, -2.28168416023254, 0.0898254886269569], 
    [-1.61025214195251, -2.30288577079773, 0.105395831167698], 
    [-1.57531571388245, -2.31326341629028, 0.100721277296543], 
    [-1.59942138195038, -2.32575917243958, 0.11884943395853], 
    [-1.62515485286713, -2.31945490837097, 0.127029225230217], 
    [-1.609290599823, -2.34574365615845, 0.135399803519249], 
    [-1.64860355854034, -2.30886435508728, 0.140506342053413], 
    [-1.57878446578979, -2.34392070770264, 0.125538811087608], 
    [-1.58710384368896, -2.36534070968628, 0.144533410668373], 
    [-1.55743336677551, -2.36226797103882, 0.139751061797142], 
    [-1.53762328624725, -2.37741827964783, 0.154106095433235], 
    [-1.54897916316986, -2.34088754653931, 0.120888896286488], 
    [-1.52734005451202, -2.3559422492981, 0.136108383536339], 
    [-1.51813590526581, -2.33368039131165, 0.117617346346378], 
    [-1.50984299182892, -2.37176012992859, 0.15134696662426], 
    [-1.49288487434387, -2.34913969039917, 0.135801956057549], 
    [-1.46751594543457, -2.34847784042358, 0.157532051205635], 
    [-1.46713852882385, -2.32596969604492, 0.133984044194221], 
    [-1.49000513553619, -2.32256197929382, 0.113502897322178], 
    [-1.48496472835541, -2.36984586715698, 0.161893352866173], 
    [-1.48416042327881, -2.3919575214386, 0.18591471016407], 
    [-1.4658762216568, -2.36865091323853, 0.183270290493965], 
    [-1.49903833866119, -2.38798904418945, 0.168372496962547], 
    [-1.50332450866699, -2.41322207450867, 0.177048817276955], 
    [-1.47837483882904, -2.41250729560852, 0.197153106331825], 
    [-1.46861207485199, -2.3888738155365, 0.204483225941658], 
    [-1.47555828094482, -2.41538643836975, 0.223142847418785], 
    [-1.45768260955811, -2.38392806053162, 0.228132084012032], 
    [-1.44862329959869, -2.36216378211975, 0.206500872969627], 
    [-1.42859101295471, -2.3369574546814, 0.200637951493263], 
    [-1.4465399980545, -2.34560465812683, 0.179622396826744], 
    [-1.43250751495361, -2.35157680511475, 0.233627960085869], 
    [-1.41076552867889, -2.32424974441528, 0.248113468289375], 
    [-1.45167422294617, -2.37618184089661, 0.251009583473206], 
    [-1.42295384407043, -2.34383392333984, 0.262814193964005], 
    [-1.43878853321075, -2.36151599884033, 0.264078795909882], 
    [-1.41344261169434, -2.32502174377441, 0.220908388495445], 
    [-1.40740239620209, -2.30861210823059, 0.194996163249016], 
    [-1.39515161514282, -2.3013026714325, 0.227839693427086], 
    [-1.38779425621033, -2.27866387367249, 0.190209463238716], 
    [-1.38147330284119, -2.27519035339355, 0.251104861497879], 
    [-1.39986097812653, -2.30033159255981, 0.262506902217865], 
    [-1.3799741268158, -2.27532196044922, 0.22093178331852], 
    [-1.37199330329895, -2.25631284713745, 0.232613191008568], 
    [-1.36853957176208, -2.25421190261841, 0.205712422728539], 
    [-1.35560500621796, -2.2268807888031, 0.19798181951046], 
    [-1.36271059513092, -2.2337019443512, 0.226811751723289], 
    [-1.37156307697296, -2.24646854400635, 0.176008000969887], 
    [-1.38250386714935, -2.23021531105042, 0.148039922118187], 
    [-1.36300182342529, -2.21410822868347, 0.169443890452385], 
    [-1.39444375038147, -2.26209616661072, 0.156137004494667], 
    [-1.40647649765015, -2.24125123023987, 0.128275796771049], 
    [-1.4212943315506, -2.27110505104065, 0.134884312748909], 
    [-1.41099882125854, -2.29121541976929, 0.163620010018349], 
    [-1.43892848491669, -2.30181241035461, 0.138807937502861], 
    [-1.42698562145233, -2.31918239593506, 0.172197237610817], 
    [-1.44827079772949, -2.32873606681824, 0.155648037791252], 
    [-1.46530270576477, -2.30058169364929, 0.112780459225178], 
    [-1.4454517364502, -2.27514791488647, 0.107967652380466], 
    [-1.45769190788269, -2.24633121490479, 0.0883723869919777], 
    [-1.42940592765808, -2.24880409240723, 0.105562396347523], 
    [-1.47982537746429, -2.26758575439453, 0.0859457328915596], 
    [-1.50680994987488, -2.27913737297058, 0.0849667266011238], 
    [-1.48851919174194, -2.22232508659363, 0.0734488740563393], 
    [-1.51411783695221, -2.24785208702087, 0.0752708688378334], 
    [-1.49031376838684, -2.29825115203857, 0.095841147005558], 
    [-1.51679408550262, -2.30781960487366, 0.0956863239407539], 
    [-1.54077863693237, -2.31889176368713, 0.105889983475208], 
    [-1.53403031826019, -2.27382254600525, 0.0791325345635414], 
    [-1.54669785499573, -2.2976598739624, 0.0923972502350807], 
    [-1.56386637687683, -2.27600240707397, 0.0832675769925117], 
    [-1.57722771167755, -2.24792051315308, 0.0793640092015266], 
    [-1.47473847866058, -2.18413662910461, 0.0801087394356728], 
    [-1.45246386528015, -2.21564030647278, 0.0842595472931862], 
    [-1.42285406589508, -2.2179868221283, 0.103183068335056], 
    [-1.44403111934662, -2.1873881816864, 0.0891599133610725], 
    [-1.47184824943542, -2.147794008255, 0.086093582212925], 
    [-1.41831207275391, -2.18908429145813, 0.104025550186634], 
    [-1.43674159049988, -2.15836668014526, 0.0954901054501534], 
    [-1.46230244636536, -2.10428190231323, 0.0949795916676521], 
    [-1.41481256484985, -2.13718819618225, 0.107927538454533], 
    [-1.39839339256287, -2.16997599601746, 0.117862530052662], 
    [-1.37764120101929, -2.1975212097168, 0.143752321600914], 
    [-1.37686204910278, -2.16759562492371, 0.143038019537926], 
    [-1.3994402885437, -2.20857834815979, 0.122999854385853], 
    [-1.38575601577759, -2.14022040367126, 0.128819361329079], 
    [-1.36554288864136, -2.11436057090759, 0.142879709601402], 
    [-1.36094522476196, -2.14825034141541, 0.155816867947578], 
    [-1.40980553627014, -2.10742425918579, 0.115508325397968], 
    [-1.42895865440369, -2.0720751285553, 0.108745224773884], 
    [-1.38717234134674, -2.08504033088684, 0.122602947056293], 
    [-1.39535653591156, -2.04952025413513, 0.116677887737751], 
    [-1.3712911605835, -2.06671762466431, 0.134353086352348], 
    [-1.35751330852509, -2.0842719078064, 0.149212881922722], 
    [-1.34860181808472, -2.0576057434082, 0.148941919207573], 
    [-1.33722746372223, -2.06746935844421, 0.168994888663292], 
    [-1.34288907051086, -2.09681463241577, 0.172668114304543], 
    [-1.34996736049652, -2.12812185287476, 0.17702428996563], 
    [-1.35090148448944, -2.16012954711914, 0.191266372799873], 
    [-1.35388684272766, -2.19490170478821, 0.194639071822166], 
    [-1.3622123003006, -2.18063759803772, 0.167071625590324], 
    [-1.35643970966339, -2.20782351493835, 0.221134498715401], 
    [-1.36526107788086, -2.21579742431641, 0.248962715268135], 
    [-1.37263238430023, -2.24190139770508, 0.252980291843414], 
    [-1.36553740501404, -2.04662775993347, 0.136845007538795], 
    [-1.41377997398376, -2.32371759414673, 0.279466062784195], 
    [-1.39118456840515, -2.27813816070557, 0.277731567621231], 
    [-1.45407128334045, -2.3799614906311, 0.275906682014465], 
    [-1.46814119815826, -2.40237760543823, 0.251563787460327], 
    [-1.63214778900146, -2.15592217445374, 0.0943257585167885], 
    [-1.67249357700348, -2.15984535217285, 0.110741086304188], 
    [-1.67904090881348, -2.12872195243835, 0.111725963652134], 
    [-1.64837300777435, -2.129958152771, 0.10267449170351]
] # presynaptic_vertex_list

presynaptic_wall_list = [
    [4, 1, 0], 
    [1, 2, 0], 
    [0, 3, 4], 
    [4, 7, 5], 
    [5, 8, 4], 
    [1, 4, 8], 
    [7, 4, 6], 
    [3, 6, 4], 
    [11, 8, 9], 
    [10, 9, 8], 
    [8, 5, 10], 
    [8, 11, 1], 
    [11, 13, 12], 
    [12, 1, 11], 
    [13, 11, 14], 
    [11, 9, 14], 
    [14, 16, 15], 
    [14, 15, 13], 
    [17, 16, 14], 
    [14, 9, 17], 
    [18, 16, 17], 
    [19, 17, 9], 
    [19, 9, 10], 
    [18, 20, 16], 
    [20, 18, 21], 
    [22, 20, 21], 
    [22, 24, 20], 
    [23, 25, 22], 
    [22, 25, 24], 
    [25, 28, 26], 
    [26, 24, 25], 
    [25, 23, 27], 
    [27, 28, 25], 
    [26, 28, 31], 
    [32, 29, 28], 
    [29, 30, 28], 
    [28, 27, 32], 
    [31, 28, 30], 
    [33, 34, 32], 
    [35, 33, 32], 
    [34, 29, 32], 
    [33, 35, 36], 
    [37, 33, 36], 
    [37, 38, 33], 
    [38, 39, 40], 
    [38, 34, 33], 
    [38, 41, 34], 
    [40, 41, 38], 
    [41, 43, 34], 
    [41, 44, 42], 
    [41, 42, 43], 
    [40, 44, 41], 
    [44, 45, 49], 
    [44, 47, 45], 
    [44, 46, 48], 
    [46, 44, 40], 
    [48, 47, 44], 
    [42, 44, 49], 
    [51, 49, 45], 
    [49, 50, 42], 
    [50, 49, 51], 
    [54, 51, 45], 
    [51, 55, 52], 
    [52, 50, 51], 
    [53, 51, 54], 
    [53, 55, 51], 
    [55, 57, 52], 
    [53, 56, 55], 
    [56, 57, 55], 
    [57, 60, 52], 
    [58, 60, 57], 
    [58, 57, 59], 
    [59, 57, 56], 
    [60, 62, 61], 
    [61, 63, 60], 
    [58, 62, 60], 
    [60, 63, 52], 
    [63, 66, 52], 
    [63, 61, 64], 
    [63, 64, 65], 
    [65, 66, 63], 
    [52, 66, 50], 
    [68, 66, 67], 
    [66, 65, 67], 
    [66, 68, 50], 
    [67, 69, 68], 
    [68, 69, 43], 
    [43, 42, 68], 
    [50, 68, 42], 
    [69, 29, 43], 
    [67, 30, 69], 
    [30, 29, 69], 
    [67, 70, 30], 
    [67, 71, 70], 
    [67, 65, 71], 
    [72, 71, 73], 
    [71, 72, 74], 
    [73, 71, 65], 
    [70, 71, 74], 
    [76, 74, 72], 
    [78, 74, 75], 
    [77, 75, 74], 
    [74, 76, 77], 
    [74, 78, 70], 
    [79, 31, 78], 
    [75, 79, 78], 
    [70, 78, 31], 
    [79, 80, 26], 
    [80, 79, 82], 
    [79, 75, 81], 
    [81, 82, 79], 
    [26, 31, 79], 
    [80, 82, 15], 
    [82, 81, 83], 
    [83, 15, 82], 
    [15, 83, 13], 
    [83, 84, 13], 
    [12, 13, 84], 
    [84, 2, 12], 
    [77, 81, 75], 
    [15, 24, 80], 
    [26, 80, 24], 
    [72, 86, 76], 
    [85, 76, 86], 
    [85, 86, 88], 
    [86, 72, 73], 
    [73, 87, 86], 
    [87, 88, 86], 
    [88, 89, 85], 
    [88, 91, 89], 
    [88, 87, 90], 
    [91, 88, 90], 
    [91, 92, 89], 
    [92, 91, 93], 
    [91, 90, 94], 
    [94, 93, 91], 
    [90, 97, 94], 
    [95, 96, 94], 
    [97, 95, 94], 
    [98, 94, 96], 
    [93, 94, 98], 
    [100, 98, 96], 
    [99, 98, 100], 
    [98, 99, 101], 
    [101, 93, 98], 
    [101, 102, 92], 
    [93, 101, 92], 
    [102, 101, 103], 
    [99, 103, 101], 
    [103, 105, 104], 
    [103, 104, 102], 
    [103, 99, 106], 
    [105, 103, 106], 
    [106, 108, 107], 
    [106, 107, 105], 
    [99, 109, 106], 
    [109, 108, 106], 
    [99, 110, 109], 
    [100, 110, 99], 
    [110, 100, 111], 
    [111, 113, 112], 
    [111, 100, 113], 
    [112, 113, 62], 
    [113, 96, 95], 
    [62, 113, 95], 
    [96, 113, 100], 
    [58, 112, 62], 
    [114, 112, 58], 
    [59, 114, 58], 
    [115, 114, 59], 
    [59, 116, 115], 
    [56, 116, 59], 
    [116, 56, 53], 
    [117, 105, 107], 
    [105, 117, 104], 
    [97, 90, 87], 
    [87, 64, 97], 
    [61, 97, 64], 
    [97, 61, 95], 
    [62, 95, 61], 
    [73, 64, 87], 
    [65, 64, 73], 
    [30, 70, 31], 
    [118, 54, 45], 
    [53, 54, 119], 
    [118, 45, 47], 
    [120, 48, 46], 
    [120, 46, 121], 
    [40, 121, 46], 
    [39, 121, 40], 
    [34, 43, 29], 
    [20, 24, 15], 
    [15, 16, 20], 
    [12, 2, 1], 
    [6, 3, 122], 
    [123, 6, 122], 
    [125, 124, 123], 
    [123, 122, 125]
] # presynaptic_wall_list

presynaptic = m.GeometryObject(
    name = 'presynaptic',
    vertex_list = presynaptic_vertex_list,
    wall_list = presynaptic_wall_list,
    surface_regions = []
)
# ^^^^ presynaptic ^^^^

