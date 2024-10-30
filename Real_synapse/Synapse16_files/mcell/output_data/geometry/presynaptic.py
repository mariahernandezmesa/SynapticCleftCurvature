import mcell as m

# ---- presynaptic ----
presynaptic_vertex_list = [
    [1.58421111106873, 3.02127599716187, -0.238843455910683], 
    [1.61994194984436, 3.00549578666687, -0.24125649034977], 
    [1.58848428726196, 3.00203609466553, -0.231237635016441], 
    [1.59683847427368, 3.0377368927002, -0.246993377804756], 
    [1.62216663360596, 3.03519821166992, -0.248009517788887], 
    [1.64734399318695, 3.02575922012329, -0.257911115884781], 
    [1.6039103269577, 3.05806517601013, -0.25496917963028], 
    [1.62937808036804, 3.05735087394714, -0.253356039524078], 
    [1.65312528610229, 3.05807447433472, -0.264088362455368], 
    [1.61076176166534, 3.08223223686218, -0.257382690906525], 
    [1.63778853416443, 3.07873034477234, -0.260088354349136], 
    [1.66595649719238, 3.08674740791321, -0.277981877326965], 
    [1.62459456920624, 3.10304689407349, -0.264089077711105], 
    [1.61434459686279, 3.12431979179382, -0.277590692043304], 
    [1.64215433597565, 3.11613368988037, -0.279687196016312], 
    [1.66494715213776, 3.12186241149902, -0.293309539556503], 
    [1.63618814945221, 3.13960838317871, -0.289105862379074], 
    [1.65646171569824, 3.15320587158203, -0.303946435451508], 
    [1.67933690547943, 3.15973448753357, -0.316937237977982], 
    [1.68545281887054, 3.13437128067017, -0.308461338281631], 
    [1.70941603183746, 3.15949773788452, -0.323693543672562], 
    [1.6890527009964, 3.1015887260437, -0.298215508460999], 
    [1.71138978004456, 3.11991953849792, -0.313659638166428], 
    [1.73507678508759, 3.13556861877441, -0.324254810810089], 
    [1.71333909034729, 3.08833050727844, -0.310252249240875], 
    [1.73734545707703, 3.10389113426208, -0.320487260818481], 
    [1.7377450466156, 3.07358717918396, -0.317975699901581], 
    [1.76097345352173, 3.08228492736816, -0.325025945901871], 
    [1.76383280754089, 3.12008047103882, -0.330208122730255], 
    [1.75469493865967, 3.14721202850342, -0.336323261260986], 
    [1.78086638450623, 3.09701037406921, -0.332894295454025], 
    [1.79790842533112, 3.1207287311554, -0.343560814857483], 
    [1.77678442001343, 3.14584422111511, -0.346766918897629], 
    [1.79842090606689, 3.15204811096191, -0.360725671052933], 
    [1.75520443916321, 3.16658091545105, -0.355211168527603], 
    [1.77635622024536, 3.16646909713745, -0.367751330137253], 
    [1.79564225673676, 3.16658854484558, -0.38117703795433], 
    [1.82303893566132, 3.15701150894165, -0.385097622871399], 
    [1.81706142425537, 3.1357536315918, -0.362377762794495], 
    [1.83574652671814, 3.13016748428345, -0.374245017766953], 
    [1.8287764787674, 3.11344385147095, -0.35785585641861], 
    [1.85195899009705, 3.10640382766724, -0.374662965536118], 
    [1.83505070209503, 3.08607816696167, -0.356516063213348], 
    [1.85042774677277, 3.07685923576355, -0.371647119522095], 
    [1.83638656139374, 3.05556893348694, -0.358310639858246], 
    [1.85772979259491, 3.05370283126831, -0.377781808376312], 
    [1.86502182483673, 3.02971792221069, -0.386945515871048], 
    [1.8416314125061, 3.02370452880859, -0.36325392127037], 
    [1.86316812038422, 3.00085520744324, -0.388410717248917], 
    [1.81472897529602, 3.0379626750946, -0.343028843402863], 
    [1.81253528594971, 3.0045645236969, -0.347126454114914], 
    [1.84301781654358, 2.99042081832886, -0.370153784751892], 
    [1.84283983707428, 2.95607376098633, -0.373734533786774], 
    [1.86260581016541, 2.96853923797607, -0.391735404729843], 
    [1.82539248466492, 2.97493386268616, -0.358026385307312], 
    [1.82063114643097, 2.95066690444946, -0.357341140508652], 
    [1.8038147687912, 2.97343683242798, -0.346214294433594], 
    [1.79420459270477, 2.94354867935181, -0.342881083488464], 
    [1.7743833065033, 2.98733854293823, -0.330802112817764], 
    [1.78408944606781, 3.02491068840027, -0.332552790641785], 
    [1.74964392185211, 3.01925158500671, -0.320086300373077], 
    [1.75065171718597, 2.96587443351746, -0.317044585943222], 
    [1.74142694473267, 2.98982644081116, -0.316322088241577], 
    [1.76893484592438, 2.95016479492188, -0.32636347413063], 
    [1.74861168861389, 2.93858599662781, -0.310514450073242], 
    [1.77504503726959, 2.92141079902649, -0.325864046812057], 
    [1.8021742105484, 2.9113883972168, -0.345211029052734], 
    [1.75248599052429, 2.90771055221558, -0.30103525519371], 
    [1.7749445438385, 2.8952431678772, -0.317546159029007], 
    [1.79024231433868, 2.89315867424011, -0.334404349327087], 
    [1.79117941856384, 2.87052822113037, -0.326274245977402], 
    [1.81128454208374, 2.87402367591858, -0.348299145698547], 
    [1.83731198310852, 2.86971759796143, -0.367870837450027], 
    [1.82559907436371, 2.89909791946411, -0.362639486789703], 
    [1.80653655529022, 2.84165740013123, -0.332015633583069], 
    [1.827183842659, 2.84561038017273, -0.353472709655762], 
    [1.78672659397125, 2.85066628456116, -0.312574148178101], 
    [1.77090525627136, 2.87397003173828, -0.305151700973511], 
    [1.76797533035278, 2.84953618049622, -0.295597106218338], 
    [1.74985468387604, 2.87800860404968, -0.286807417869568], 
    [1.72905957698822, 2.90023994445801, -0.280457258224487], 
    [1.72981512546539, 2.8706316947937, -0.269940078258514], 
    [1.70715367794037, 2.88911032676697, -0.263683408498764], 
    [1.70896434783936, 2.85698986053467, -0.257848262786865], 
    [1.68699836730957, 2.87140107154846, -0.252807646989822], 
    [1.67906022071838, 2.90540862083435, -0.255817353725433], 
    [1.68151533603668, 2.93491959571838, -0.265433132648468], 
    [1.70404708385468, 2.9183976650238, -0.273420810699463], 
    [1.6530396938324, 2.94162344932556, -0.244860932230949], 
    [1.67516028881073, 2.96185326576233, -0.266520589590073], 
    [1.62908279895782, 2.97082018852234, -0.236362710595131], 
    [1.65416431427002, 2.98784685134888, -0.25517925620079], 
    [1.69103384017944, 2.98563861846924, -0.285112172365189], 
    [1.67185509204865, 3.01249313354492, -0.272938221693039], 
    [1.69367527961731, 3.02262878417969, -0.290900677442551], 
    [1.67429041862488, 3.04422116279602, -0.277195811271667], 
    [1.69411909580231, 3.06356120109558, -0.294787734746933], 
    [1.7174654006958, 3.03324127197266, -0.306102335453033], 
    [1.71961975097656, 3.06157422065735, -0.308063149452209], 
    [1.73766851425171, 3.04679274559021, -0.316279351711273], 
    [1.76204800605774, 3.05037331581116, -0.325522571802139], 
    [1.78893911838531, 3.06105971336365, -0.332739949226379], 
    [1.80019438266754, 3.08616185188293, -0.339264035224915], 
    [1.817134141922, 3.0682520866394, -0.343604356050491], 
    [1.81731390953064, 3.09603667259216, -0.347204506397247], 
    [1.71624791622162, 3.00164914131165, -0.30451363325119], 
    [1.72174465656281, 2.96562457084656, -0.302464008331299], 
    [1.70050585269928, 2.95055532455444, -0.282045483589172], 
    [1.72530090808868, 2.93079972267151, -0.291940033435822], 
    [1.60095942020416, 2.9833505153656, -0.227150872349739], 
    [1.81680119037628, 2.92608904838562, -0.356596887111664], 
    [1.84875118732452, 2.89825463294983, -0.381021350622177], 
    [1.83893775939941, 2.92631316184998, -0.371360927820206], 
    [1.86179792881012, 2.93170690536499, -0.393134742975235], 
    [1.88158166408539, 2.92152285575867, -0.418245762586594], 
    [1.88097333908081, 2.95247721672058, -0.414183497428894], 
    [1.87007761001587, 2.89744424819946, -0.402565747499466], 
    [1.87995779514313, 2.98345017433167, -0.408719003200531], 
    [1.73652446269989, 3.16441559791565, -0.337067395448685], 
    [1.67767119407654, 3.17703723907471, -0.337453752756119]
] # presynaptic_vertex_list

presynaptic_wall_list = [
    [2, 1, 0], 
    [0, 1, 3], 
    [4, 3, 1], 
    [4, 5, 7], 
    [1, 5, 4], 
    [7, 6, 4], 
    [8, 7, 5], 
    [10, 7, 8], 
    [9, 7, 10], 
    [6, 7, 9], 
    [8, 11, 10], 
    [11, 12, 10], 
    [10, 12, 9], 
    [12, 11, 14], 
    [12, 14, 13], 
    [13, 14, 16], 
    [16, 14, 15], 
    [15, 14, 11], 
    [15, 17, 16], 
    [19, 18, 17], 
    [15, 19, 17], 
    [21, 19, 15], 
    [18, 19, 20], 
    [20, 19, 22], 
    [21, 22, 19], 
    [25, 23, 22], 
    [22, 23, 20], 
    [25, 22, 24], 
    [21, 24, 22], 
    [25, 26, 27], 
    [24, 26, 25], 
    [27, 28, 25], 
    [25, 28, 23], 
    [23, 28, 29], 
    [32, 29, 28], 
    [30, 28, 27], 
    [28, 30, 31], 
    [28, 31, 32], 
    [33, 35, 32], 
    [32, 31, 33], 
    [32, 35, 34], 
    [32, 34, 29], 
    [36, 35, 33], 
    [37, 36, 33], 
    [33, 38, 37], 
    [38, 39, 37], 
    [40, 41, 39], 
    [39, 38, 40], 
    [42, 43, 41], 
    [41, 40, 42], 
    [43, 42, 44], 
    [45, 43, 44], 
    [47, 45, 44], 
    [46, 45, 47], 
    [48, 46, 47], 
    [47, 51, 48], 
    [47, 44, 49], 
    [47, 49, 50], 
    [50, 51, 47], 
    [51, 53, 48], 
    [51, 54, 52], 
    [52, 53, 51], 
    [50, 54, 51], 
    [55, 52, 54], 
    [56, 55, 54], 
    [54, 50, 56], 
    [57, 55, 56], 
    [56, 50, 58], 
    [58, 57, 56], 
    [58, 50, 59], 
    [58, 59, 60], 
    [58, 60, 62], 
    [62, 61, 58], 
    [61, 63, 58], 
    [63, 57, 58], 
    [65, 63, 64], 
    [64, 63, 61], 
    [57, 63, 65], 
    [69, 66, 65], 
    [65, 66, 57], 
    [67, 68, 65], 
    [67, 65, 64], 
    [69, 65, 68], 
    [69, 71, 66], 
    [69, 68, 70], 
    [70, 71, 69], 
    [71, 72, 73], 
    [71, 75, 72], 
    [71, 73, 66], 
    [74, 75, 71], 
    [70, 74, 71], 
    [76, 74, 70], 
    [77, 76, 70], 
    [78, 76, 77], 
    [79, 78, 77], 
    [79, 67, 80], 
    [77, 67, 79], 
    [80, 81, 79], 
    [83, 81, 82], 
    [81, 80, 82], 
    [83, 82, 84], 
    [84, 82, 85], 
    [87, 86, 85], 
    [85, 86, 88], 
    [82, 87, 85], 
    [88, 89, 91], 
    [86, 89, 88], 
    [90, 88, 91], 
    [89, 92, 91], 
    [91, 92, 93], 
    [93, 5, 91], 
    [91, 5, 1], 
    [1, 90, 91], 
    [92, 94, 93], 
    [93, 94, 95], 
    [93, 95, 5], 
    [95, 11, 8], 
    [96, 11, 95], 
    [95, 94, 96], 
    [5, 95, 8], 
    [96, 97, 98], 
    [94, 97, 96], 
    [98, 24, 96], 
    [96, 24, 21], 
    [96, 21, 11], 
    [26, 24, 98], 
    [97, 99, 98], 
    [98, 99, 26], 
    [60, 99, 97], 
    [100, 99, 60], 
    [99, 100, 26], 
    [26, 100, 27], 
    [60, 59, 100], 
    [100, 101, 27], 
    [59, 101, 100], 
    [49, 101, 59], 
    [101, 49, 103], 
    [102, 30, 101], 
    [27, 101, 30], 
    [101, 103, 102], 
    [49, 44, 103], 
    [44, 42, 103], 
    [104, 103, 42], 
    [104, 102, 103], 
    [42, 40, 104], 
    [31, 104, 40], 
    [102, 104, 31], 
    [30, 102, 31], 
    [60, 97, 105], 
    [105, 97, 94], 
    [105, 106, 62], 
    [92, 106, 105], 
    [105, 94, 92], 
    [62, 60, 105], 
    [108, 106, 107], 
    [107, 106, 92], 
    [106, 64, 61], 
    [108, 64, 106], 
    [106, 61, 62], 
    [80, 67, 108], 
    [108, 67, 64], 
    [87, 80, 108], 
    [107, 87, 108], 
    [86, 107, 89], 
    [89, 107, 92], 
    [86, 87, 107], 
    [109, 90, 1], 
    [1, 2, 109], 
    [80, 87, 82], 
    [77, 68, 67], 
    [70, 68, 77], 
    [110, 73, 112], 
    [73, 110, 66], 
    [73, 72, 111], 
    [73, 111, 112], 
    [111, 113, 112], 
    [112, 52, 55], 
    [112, 55, 110], 
    [112, 113, 52], 
    [113, 114, 115], 
    [116, 114, 113], 
    [116, 113, 111], 
    [53, 113, 115], 
    [113, 53, 52], 
    [115, 117, 53], 
    [48, 53, 117], 
    [110, 55, 57], 
    [66, 110, 57], 
    [59, 50, 49], 
    [40, 38, 31], 
    [31, 38, 33], 
    [118, 29, 34], 
    [29, 118, 23], 
    [23, 118, 20], 
    [11, 21, 15], 
    [20, 119, 18]
] # presynaptic_wall_list

presynaptic = m.GeometryObject(
    name = 'presynaptic',
    vertex_list = presynaptic_vertex_list,
    wall_list = presynaptic_wall_list,
    surface_regions = []
)
# ^^^^ presynaptic ^^^^

