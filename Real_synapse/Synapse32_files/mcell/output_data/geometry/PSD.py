import mcell as m

# ---- PSD ----
PSD_vertex_list = [
    [-0.11620169878006, 0.120989322662354, 0.123479306697845], 
    [-0.112866520881653, 0.0896072387695312, 0.130037784576416], 
    [-0.106405556201935, 0.100253582000732, 0.108003854751587], 
    [-0.106805115938187, 0.125246524810791, 0.0981556177139282], 
    [-0.0945029854774475, 0.126319885253906, 0.0730736255645752], 
    [-0.107104122638702, 0.151471614837646, 0.0873832106590271], 
    [-0.0950409770011902, 0.0970292091369629, 0.0851204991340637], 
    [-0.0823087692260742, 0.102316856384277, 0.0605700612068176], 
    [-0.0771077275276184, 0.0699353218078613, 0.0764822363853455], 
    [-0.0938166379928589, 0.0726618766784668, 0.108076393604279], 
    [-0.0725292265415192, 0.0475645065307617, 0.101372241973877], 
    [-0.0854832231998444, 0.0477943420410156, 0.125157058238983], 
    [-0.102855890989304, 0.062464714050293, 0.140849590301514], 
    [-0.0668182671070099, 0.0265846252441406, 0.123521268367767], 
    [-0.0536415278911591, 0.0189995765686035, 0.0992921590805054], 
    [-0.0505341589450836, -0.00337362289428711, 0.121738791465759], 
    [-0.0410593748092651, -0.00919580459594727, 0.0933248996734619], 
    [-0.0398787558078766, -0.0323085784912109, 0.108525574207306], 
    [-0.0310833156108856, -0.0342378616333008, 0.0863568782806396], 
    [-0.0335967540740967, -0.0574078559875488, 0.119204580783844], 
    [-0.0272112190723419, -0.0581526756286621, 0.0959951281547546], 
    [-0.0225940346717834, -0.0827093124389648, 0.110226988792419], 
    [-0.0138983726501465, -0.0801420211791992, 0.08515864610672], 
    [-0.0177815556526184, -0.053767204284668, 0.0739207863807678], 
    [-0.00340235233306885, -0.0762100219726562, 0.0597317218780518], 
    [-0.0110869407653809, -0.0428609848022461, 0.0513359308242798], 
    [-0.0274551808834076, -0.0185742378234863, 0.0642430186271667], 
    [-0.0135680437088013, -0.0152740478515625, 0.0371384620666504], 
    [-0.0425125062465668, 0.0103311538696289, 0.0743386745452881], 
    [-0.0312539637088776, 0.00760459899902344, 0.0496016144752502], 
    [-0.0366569459438324, 0.0369462966918945, 0.0363723039627075], 
    [-0.0207552909851074, 0.0142216682434082, 0.0264238119125366], 
    [-0.0452251434326172, 0.0299248695373535, 0.0586448907852173], 
    [-0.0557426512241364, 0.0549249649047852, 0.0541806221008301], 
    [-0.057812362909317, 0.0396628379821777, 0.0786563158035278], 
    [-0.0671706199645996, 0.0808773040771484, 0.0478318333625793], 
    [-0.0459226369857788, 0.065392017364502, 0.0281721949577332], 
    [-0.0319634079933167, 0.069209098815918, 0.00454282760620117], 
    [-0.0590330362319946, 0.0918240547180176, 0.0256658792495728], 
    [-0.0437696278095245, 0.0917568206787109, 0.00676822662353516], 
    [-0.0236244201660156, 0.0427670478820801, 0.0112360715866089], 
    [-0.00896179676055908, 0.0184001922607422, 0.00638556480407715], 
    [-0.00560969114303589, 0.0337357521057129, -0.0109731554985046], 
    [-0.0163682699203491, 0.0611429214477539, -0.0121869444847107], 
    [-0.00128710269927979, 0.0502762794494629, -0.0290011167526245], 
    [-0.02717325091362, 0.0881080627441406, -0.0129422545433044], 
    [-0.0109867453575134, 0.080317497253418, -0.0350914597511292], 
    [-0.0105546116828918, 0.10465669631958, -0.0537156462669373], 
    [0.00350916385650635, 0.0615348815917969, -0.0492077469825745], 
    [0.00107496976852417, 0.0815014839172363, -0.0622037649154663], 
    [-0.0253453254699707, 0.108510494232178, -0.0310800075531006], 
    [-0.0238834619522095, 0.128593444824219, -0.0495635271072388], 
    [-0.0376120209693909, 0.13521671295166, -0.0268017053604126], 
    [-0.0411359369754791, 0.114419460296631, -0.00877058506011963], 
    [-0.0581967234611511, 0.115988731384277, 0.0121574997901917], 
    [-0.0554168224334717, 0.143585681915283, -0.00331312417984009], 
    [-0.0710579454898834, 0.168614864349365, 0.012701153755188], 
    [-0.0450781881809235, 0.162362575531006, -0.0260223150253296], 
    [-0.0562424659729004, 0.174174785614014, -0.00746774673461914], 
    [-0.0723405182361603, 0.138479709625244, 0.0219008922576904], 
    [-0.0860176384449005, 0.159544944763184, 0.0349524617195129], 
    [-0.0736579895019531, 0.11028528213501, 0.0349071025848389], 
    [-0.0845709145069122, 0.13200569152832, 0.0474219918251038], 
    [-0.0974413752555847, 0.153011798858643, 0.0602944493293762], 
    [-0.106801778078079, 0.176566600799561, 0.0735331177711487], 
    [-0.0961256623268127, 0.177772998809814, 0.0501903891563416], 
    [-0.0850693583488464, 0.195818424224854, 0.0279351472854614], 
    [0.0118443965911865, 0.079594612121582, -0.0847129225730896], 
    [-0.000627100467681885, 0.100377082824707, -0.0780265331268311], 
    [0.0190343260765076, 0.0504012107849121, -0.0738928914070129], 
    [0.021073043346405, 0.0669369697570801, -0.10351151227951], 
    [0.0197489857673645, 0.0208454132080078, -0.053466260433197], 
    [0.0261697769165039, 0.0187239646911621, -0.0740804076194763], 
    [0.0257223844528198, 0.0435037612915039, -0.102263808250427], 
    [0.0280025005340576, 0.0259275436401367, -0.0922365784645081], 
    [0.0109334588050842, 0.0407476425170898, -0.0467731952667236], 
    [0.0103438496589661, 0.0199689865112305, -0.0302004218101501], 
    [0.00545006990432739, 0.0053558349609375, -0.00894796848297119], 
    [0.0195080637931824, -0.0114455223083496, -0.0244296193122864], 
    [0.022860050201416, -0.000890254974365234, -0.0453567504882812], 
    [0.0297769904136658, -0.00288009643554688, -0.0667517781257629], 
    [0.0394350290298462, -0.0348343849182129, -0.0527569055557251], 
    [0.0409632325172424, -0.01934814453125, -0.0772967338562012], 
    [0.0574114322662354, -0.0378637313842773, -0.084104061126709], 
    [0.0628560781478882, -0.0618743896484375, -0.0718289613723755], 
    [0.0283134579658508, -0.0366554260253906, -0.0228258371353149], 
    [0.040018618106842, -0.0604596138000488, -0.0268405675888062], 
    [0.0529469847679138, -0.0683951377868652, -0.0482795238494873], 
    [0.0682883262634277, -0.0885467529296875, -0.0589086413383484], 
    [0.0570827722549438, -0.09356689453125, -0.0307576656341553], 
    [0.0516833066940308, -0.111651420593262, 0.00441473722457886], 
    [0.0810099244117737, -0.118207931518555, -0.0492529273033142], 
    [0.0409504175186157, -0.0809297561645508, -0.00833064317703247], 
    [0.0703124403953552, -0.119524955749512, -0.022888720035553], 
    [0.0712907910346985, -0.137928009033203, -0.00638192892074585], 
    [0.0886816382408142, -0.147320747375488, -0.0299809575080872], 
    [0.0822280049324036, -0.162012100219727, -0.00300323963165283], 
    [0.100715219974518, -0.145583152770996, -0.0590688586235046], 
    [0.108587145805359, -0.139925003051758, -0.0881200432777405], 
    [0.0957888960838318, -0.123671531677246, -0.0729770660400391], 
    [0.100310742855072, -0.107941627502441, -0.0959645509719849], 
    [0.0842983722686768, -0.103768348693848, -0.0724635720252991], 
    [0.0800890922546387, -0.0823183059692383, -0.0846179723739624], 
    [0.0931223630905151, -0.0807743072509766, -0.108574748039246], 
    [0.0752438902854919, -0.0581293106079102, -0.0966575741767883], 
    [0.0885469913482666, -0.0550532341003418, -0.120968580245972], 
    [0.06903076171875, -0.0332574844360352, -0.109368920326233], 
    [0.0505465269088745, -0.0145153999328613, -0.0960960984230042], 
    [0.0687244534492493, -0.0160317420959473, -0.127640724182129], 
    [0.0836882591247559, -0.0331697463989258, -0.135468721389771], 
    [0.055157482624054, -0.00406503677368164, -0.117419838905334], 
    [0.0380303859710693, 0.0190467834472656, -0.115348815917969], 
    [0.0550165176391602, 0.00878429412841797, -0.139432787895203], 
    [0.0744643807411194, -0.0113468170166016, -0.14581698179245], 
    [0.0337696671485901, 0.0292339324951172, -0.141581892967224], 
    [0.0251941680908203, 0.0468463897705078, -0.124465465545654], 
    [0.0101926922798157, 0.0711965560913086, -0.123787641525269], 
    [0.00874096155166626, 0.0940651893615723, -0.104132473468781], 
    [0.0345830321311951, 0.0036015510559082, -0.0876942873001099], 
    [0.106011569499969, -0.0729885101318359, -0.129967033863068], 
    [0.113180041313171, -0.0995769500732422, -0.121854543685913], 
    [0.116781055927277, -0.128937721252441, -0.112526535987854], 
    [0.0716546177864075, -0.171501159667969, 0.0196662545204163], 
    [0.0632362961769104, -0.145692825317383, 0.0177159309387207], 
    [0.0543274879455566, -0.163539886474609, 0.0449205040931702], 
    [0.044042706489563, -0.133871078491211, 0.0346924662590027], 
    [0.0308921933174133, -0.106049537658691, 0.0304856300354004], 
    [0.0316043496131897, -0.145562171936035, 0.0654319524765015], 
    [0.0273074507713318, -0.122373580932617, 0.0488693714141846], 
    [0.0130192637443542, -0.102289199829102, 0.0537139773368835], 
    [0.015663206577301, -0.120364189147949, 0.0668007731437683], 
    [0.000185370445251465, -0.101724624633789, 0.0755130052566528], 
    [0.00741004943847656, -0.129477500915527, 0.0876421928405762], 
    [-0.00273466110229492, -0.130294799804688, 0.114719331264496], 
    [0.0212033987045288, -0.156526565551758, 0.0963912606239319], 
    [-0.00876754522323608, -0.105877876281738, 0.10034316778183], 
    [0.0407758951187134, -0.175041198730469, 0.0741480588912964], 
    [0.014549732208252, -0.0855693817138672, 0.0384181141853333], 
    [0.00423985719680786, -0.0639214515686035, 0.0372334718704224], 
    [0.0252346396446228, -0.0805273056030273, 0.0151814818382263], 
    [0.0238203406333923, -0.0531249046325684, -0.00365477800369263], 
    [0.0123806595802307, -0.0544142723083496, 0.0183143019676208], 
    [0.00514626502990723, -0.0298571586608887, 0.0149651765823364], 
    [-0.00104296207427979, -0.0414652824401855, 0.0317662954330444], 
    [0.0154747366905212, -0.0209388732910156, -0.00476545095443726], 
    [-0.00231993198394775, -0.00485515594482422, 0.0132246017456055]
] # PSD_vertex_list

PSD_wall_list = [
    [0, 1, 2], 
    [2, 3, 0], 
    [4, 5, 3], 
    [6, 4, 3], 
    [6, 3, 2], 
    [6, 7, 4], 
    [8, 7, 6], 
    [9, 8, 6], 
    [2, 9, 6], 
    [8, 9, 10], 
    [1, 9, 2], 
    [10, 9, 11], 
    [12, 11, 9], 
    [1, 12, 9], 
    [13, 10, 11], 
    [15, 14, 13], 
    [14, 10, 13], 
    [15, 17, 16], 
    [15, 16, 14], 
    [20, 18, 17], 
    [18, 16, 17], 
    [19, 20, 17], 
    [19, 21, 20], 
    [22, 20, 21], 
    [20, 22, 23], 
    [20, 23, 18], 
    [18, 23, 26], 
    [22, 24, 23], 
    [23, 24, 25], 
    [23, 25, 26], 
    [26, 25, 27], 
    [26, 27, 29], 
    [28, 26, 29], 
    [16, 26, 28], 
    [16, 18, 26], 
    [27, 31, 29], 
    [29, 31, 30], 
    [29, 30, 32], 
    [29, 32, 28], 
    [32, 33, 34], 
    [30, 33, 32], 
    [28, 32, 34], 
    [34, 33, 8], 
    [34, 8, 10], 
    [14, 28, 34], 
    [10, 14, 34], 
    [8, 33, 35], 
    [36, 35, 33], 
    [33, 30, 36], 
    [35, 36, 38], 
    [36, 37, 39], 
    [40, 37, 36], 
    [39, 38, 36], 
    [40, 36, 30], 
    [31, 41, 40], 
    [40, 41, 42], 
    [40, 42, 43], 
    [40, 43, 37], 
    [30, 31, 40], 
    [37, 43, 45], 
    [43, 42, 44], 
    [43, 44, 46], 
    [43, 46, 45], 
    [49, 47, 46], 
    [46, 47, 50], 
    [45, 46, 50], 
    [48, 49, 46], 
    [44, 48, 46], 
    [51, 52, 50], 
    [47, 51, 50], 
    [50, 52, 53], 
    [53, 45, 50], 
    [39, 45, 53], 
    [54, 39, 53], 
    [53, 55, 54], 
    [53, 52, 55], 
    [56, 55, 58], 
    [59, 55, 56], 
    [54, 55, 59], 
    [55, 57, 58], 
    [52, 57, 55], 
    [62, 59, 60], 
    [60, 59, 56], 
    [61, 54, 59], 
    [62, 61, 59], 
    [7, 62, 4], 
    [4, 62, 63], 
    [7, 61, 62], 
    [62, 60, 63], 
    [5, 63, 64], 
    [64, 63, 65], 
    [63, 60, 65], 
    [5, 4, 63], 
    [65, 60, 66], 
    [66, 60, 56], 
    [38, 61, 35], 
    [35, 61, 7], 
    [61, 38, 54], 
    [39, 54, 38], 
    [67, 68, 49], 
    [69, 67, 49], 
    [69, 49, 48], 
    [69, 70, 67], 
    [73, 70, 69], 
    [75, 71, 69], 
    [69, 71, 72], 
    [72, 74, 69], 
    [69, 48, 75], 
    [74, 73, 69], 
    [44, 75, 48], 
    [76, 75, 44], 
    [76, 71, 75], 
    [79, 71, 76], 
    [77, 78, 76], 
    [76, 42, 77], 
    [78, 79, 76], 
    [76, 44, 42], 
    [79, 80, 71], 
    [81, 80, 79], 
    [81, 79, 78], 
    [81, 82, 80], 
    [83, 82, 81], 
    [84, 83, 81], 
    [87, 84, 81], 
    [81, 78, 85], 
    [85, 86, 81], 
    [86, 87, 81], 
    [87, 88, 84], 
    [89, 88, 87], 
    [89, 87, 86], 
    [90, 89, 92], 
    [93, 89, 90], 
    [89, 91, 88], 
    [93, 91, 89], 
    [89, 86, 92], 
    [95, 93, 94], 
    [94, 93, 90], 
    [93, 95, 91], 
    [91, 95, 97], 
    [94, 96, 95], 
    [98, 99, 97], 
    [97, 99, 91], 
    [99, 98, 100], 
    [99, 100, 101], 
    [99, 101, 91], 
    [91, 101, 88], 
    [101, 102, 88], 
    [101, 100, 102], 
    [103, 104, 102], 
    [102, 100, 103], 
    [102, 84, 88], 
    [84, 102, 104], 
    [104, 103, 105], 
    [105, 106, 104], 
    [104, 106, 83], 
    [84, 104, 83], 
    [107, 106, 110], 
    [83, 106, 107], 
    [109, 108, 106], 
    [106, 108, 110], 
    [106, 105, 109], 
    [111, 110, 112], 
    [107, 110, 111], 
    [108, 112, 110], 
    [108, 113, 112], 
    [112, 114, 111], 
    [114, 115, 111], 
    [111, 115, 73], 
    [70, 115, 116], 
    [73, 115, 70], 
    [117, 70, 116], 
    [67, 70, 117], 
    [68, 67, 117], 
    [108, 109, 113], 
    [111, 73, 74], 
    [111, 74, 118], 
    [111, 118, 107], 
    [118, 72, 80], 
    [82, 118, 80], 
    [72, 118, 74], 
    [107, 118, 82], 
    [82, 83, 107], 
    [119, 105, 103], 
    [120, 119, 103], 
    [100, 121, 120], 
    [120, 103, 100], 
    [121, 100, 98], 
    [123, 96, 94], 
    [122, 96, 123], 
    [125, 123, 90], 
    [90, 123, 94], 
    [124, 123, 125], 
    [122, 123, 124], 
    [90, 126, 125], 
    [125, 126, 128], 
    [127, 124, 125], 
    [128, 127, 125], 
    [130, 127, 128], 
    [130, 128, 129], 
    [129, 128, 126], 
    [132, 130, 131], 
    [131, 130, 129], 
    [132, 127, 130], 
    [134, 127, 132], 
    [133, 134, 132], 
    [132, 135, 133], 
    [132, 131, 135], 
    [131, 22, 135], 
    [21, 135, 22], 
    [134, 136, 127], 
    [136, 124, 127], 
    [22, 131, 24], 
    [131, 129, 24], 
    [24, 129, 137], 
    [129, 126, 137], 
    [137, 138, 24], 
    [139, 138, 137], 
    [137, 126, 139], 
    [139, 92, 140], 
    [139, 140, 141], 
    [90, 92, 139], 
    [138, 139, 141], 
    [90, 139, 126], 
    [141, 140, 142], 
    [141, 142, 143], 
    [141, 143, 138], 
    [25, 143, 27], 
    [142, 27, 143], 
    [25, 138, 143], 
    [142, 140, 144], 
    [27, 142, 145], 
    [144, 145, 142], 
    [77, 145, 144], 
    [41, 145, 77], 
    [31, 145, 41], 
    [145, 31, 27], 
    [85, 78, 144], 
    [144, 78, 77], 
    [140, 85, 144], 
    [86, 85, 140], 
    [86, 140, 92], 
    [24, 138, 25], 
    [80, 72, 71], 
    [77, 42, 41], 
    [45, 39, 37], 
    [8, 35, 7], 
    [16, 28, 14]
] # PSD_wall_list

PSD = m.GeometryObject(
    name = 'PSD',
    vertex_list = PSD_vertex_list,
    wall_list = PSD_wall_list,
    surface_regions = []
)
# ^^^^ PSD ^^^^


