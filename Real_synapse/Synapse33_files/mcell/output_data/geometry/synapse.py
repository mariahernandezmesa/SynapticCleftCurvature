import mcell as m

# ---- synapse ----
synapse_vertex_list = [
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
    [-0.0251966714859009, -0.17349910736084, -0.0816836357116699], 
    [0.0258307456970215, -0.160431385040283, -0.0992504358291626], 
    [0.0414400100708008, -0.125808238983154, -0.101905703544617], 
    [0.00658535957336426, -0.173304080963135, -0.0856102705001831], 
    [0.0173699855804443, -0.14471960067749, -0.0819606781005859], 
    [-0.00509488582611084, -0.153353214263916, -0.0652432441711426], 
    [0.0169954299926758, -0.119336605072021, -0.0649118423461914], 
    [0.0274758338928223, -0.0859313011169434, -0.0558536052703857], 
    [-0.0129315853118896, -0.134299278259277, -0.0419484376907349], 
    [0.038083553314209, -0.0962986946105957, -0.082677960395813], 
    [0.00321793556213379, -0.105455875396729, -0.0387547016143799], 
    [0.0126839876174927, -0.0802459716796875, -0.030064582824707], 
    [-0.020726203918457, -0.114971160888672, -0.0226233005523682], 
    [-0.0108911991119385, -0.0898313522338867, -0.0144915580749512], 
    [0.00264763832092285, -0.0608506202697754, -0.00747549533843994], 
    [-0.0301252603530884, -0.0750651359558105, 0.00471687316894531], 
    [-0.0397542715072632, -0.104548454284668, -0.00347089767456055], 
    [-0.0611681938171387, -0.0867981910705566, 0.0141140222549438], 
    [-0.0442867279052734, -0.136823654174805, -0.0195339918136597], 
    [-0.067901611328125, -0.119196891784668, 0.00402212142944336], 
    [-0.0925569534301758, -0.097999095916748, 0.0217726230621338], 
    [-0.0834524631500244, -0.061398983001709, 0.0282182693481445], 
    [-0.0678308010101318, -0.0330052375793457, 0.0295740365982056], 
    [-0.0971286296844482, -0.0299320220947266, 0.0401835441589355], 
    [-0.0515037775039673, -0.0567975044250488, 0.0184558629989624], 
    [-0.0211377143859863, -0.0462470054626465, 0.0107523202896118], 
    [-0.0413839817047119, -0.0303525924682617, 0.0218628644943237], 
    [-0.04697585105896, -0.000245094299316406, 0.0312377214431763], 
    [-0.0192209482192993, -0.0157356262207031, 0.0170869827270508], 
    [0.00442242622375488, 0.00135707855224609, 0.00966036319732666], 
    [0.0029522180557251, -0.0293822288513184, 0.00350081920623779], 
    [-0.016798734664917, 0.011052131652832, 0.0227471590042114], 
    [-0.0236572027206421, 0.0341582298278809, 0.0347857475280762], 
    [0.00421798229217529, 0.0367588996887207, 0.0204067230224609], 
    [0.0225987434387207, 0.0678720474243164, 0.0202090740203857], 
    [0.0287914276123047, 0.0454730987548828, 0.0063481330871582], 
    [0.0254529714584351, 0.0188555717468262, 0.00134015083312988], 
    [-0.00905334949493408, 0.066502571105957, 0.0415433645248413], 
    [-0.00477278232574463, 0.0985045433044434, 0.0473160743713379], 
    [-0.0390114784240723, 0.0498275756835938, 0.0476206541061401], 
    [-0.0458823442459106, 0.0727825164794922, 0.0576251745223999], 
    [-0.0291991233825684, 0.095583438873291, 0.0574371814727783], 
    [0.0178062915802002, 0.0942702293395996, 0.0330455303192139], 
    [0.00997269153594971, 0.120558738708496, 0.0461870431900024], 
    [0.0304137468338013, 0.119302749633789, 0.0316667556762695], 
    [0.0461910963058472, 0.102108478546143, 0.0104330778121948], 
    [0.0480159521102905, 0.137945652008057, 0.0251725912094116], 
    [0.0670098066329956, 0.136619567871094, 0.00734341144561768], 
    [0.04805588722229, 0.066497802734375, -0.00124549865722656], 
    [0.0728391408920288, 0.117285251617432, -0.011247992515564], 
    [0.0664452314376831, 0.087432861328125, -0.014441967010498], 
    [0.0667202472686768, 0.0540485382080078, -0.0280711650848389], 
    [0.0793505907058716, 0.0798525810241699, -0.0386337041854858], 
    [0.086819052696228, 0.0590438842773438, -0.0633665323257446], 
    [0.0686986446380615, 0.0289268493652344, -0.0503243207931519], 
    [0.054961085319519, 0.0255250930786133, -0.0302292108535767], 
    [0.0550442934036255, 3.19480895996094e-05, -0.0432891845703125], 
    [0.0673303604125977, -0.000759124755859375, -0.0694581270217896], 
    [0.0523970127105713, -0.0293316841125488, -0.0604149103164673], 
    [0.0477802753448486, -0.0608420372009277, -0.0795853137969971], 
    [0.0327695608139038, -0.0542831420898438, -0.04227614402771], 
    [0.0396634340286255, -0.0219860076904297, -0.0315625667572021], 
    [0.0222840309143066, -0.0368146896362305, -0.0144965648651123], 
    [0.0409657955169678, 0.00690746307373047, -0.019328236579895], 
    [0.0239758491516113, -0.0106468200683594, -0.00672435760498047], 
    [0.0451376438140869, 0.0371975898742676, -0.0106643438339233], 
    [0.028461217880249, 0.146815776824951, 0.0470099449157715], 
    [0.00297927856445312, 0.143290519714355, 0.0611436367034912], 
    [0.0184040069580078, 0.164017200469971, 0.0729246139526367], 
    [-0.00838828086853027, 0.163233280181885, 0.0850400328636169], 
    [-0.0236973762512207, 0.145115852355957, 0.0715740919113159], 
    [-0.0406630039215088, 0.119688987731934, 0.0691369771957397], 
    [-0.0145704746246338, 0.120851516723633, 0.0584723949432373], 
    [-0.0571808815002441, 0.0958566665649414, 0.0689015984535217], 
    [-0.0720791816711426, 0.0735149383544922, 0.0674472451210022], 
    [-0.0690822601318359, 0.0477747917175293, 0.0552273988723755], 
    [-0.0759463310241699, 0.0179376602172852, 0.0449239015579224], 
    [-0.0515186786651611, 0.0288872718811035, 0.0427408218383789], 
    [-0.0782244205474854, -0.00865793228149414, 0.038912296295166], 
    [-0.0322617292404175, -0.164090156555176, -0.0470160245895386], 
    [-0.015196681022644, -0.183499336242676, -0.0716836452484131]
] # synapse_vertex_list

synapse_wall_list = [
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
    [2, 79, 4], 
    [83, 80, 81], 
    [80, 83, 82], 
    [84, 82, 83], 
    [83, 85, 84], 
    [81, 85, 83], 
    [85, 88, 86], 
    [89, 85, 86], 
    [87, 84, 85], 
    [89, 87, 85], 
    [85, 81, 88], 
    [89, 91, 87], 
    [90, 89, 86], 
    [92, 89, 90], 
    [89, 92, 91], 
    [92, 95, 91], 
    [93, 94, 92], 
    [92, 90, 93], 
    [94, 95, 92], 
    [95, 94, 96], 
    [98, 95, 96], 
    [95, 98, 97], 
    [95, 97, 91], 
    [96, 99, 98], 
    [99, 96, 100], 
    [103, 101, 100], 
    [102, 100, 101], 
    [100, 96, 103], 
    [96, 94, 103], 
    [103, 94, 104], 
    [105, 103, 104], 
    [101, 103, 105], 
    [105, 106, 101], 
    [107, 106, 105], 
    [105, 104, 107], 
    [104, 109, 107], 
    [108, 107, 109], 
    [110, 107, 108], 
    [106, 107, 110], 
    [112, 110, 108], 
    [112, 111, 110], 
    [110, 111, 106], 
    [112, 108, 115], 
    [116, 112, 113], 
    [113, 112, 114], 
    [114, 112, 115], 
    [111, 112, 116], 
    [121, 116, 113], 
    [121, 117, 116], 
    [120, 116, 117], 
    [116, 119, 118], 
    [116, 118, 111], 
    [119, 116, 120], 
    [117, 121, 122], 
    [121, 123, 122], 
    [121, 124, 123], 
    [121, 113, 124], 
    [125, 123, 124], 
    [126, 125, 124], 
    [124, 128, 126], 
    [113, 127, 124], 
    [129, 124, 127], 
    [124, 129, 128], 
    [127, 130, 129], 
    [130, 131, 129], 
    [132, 131, 130], 
    [133, 132, 130], 
    [134, 135, 133], 
    [130, 134, 133], 
    [136, 133, 135], 
    [137, 136, 135], 
    [140, 137, 135], 
    [138, 137, 139], 
    [139, 137, 140], 
    [141, 139, 140], 
    [140, 143, 141], 
    [142, 140, 135], 
    [143, 140, 142], 
    [108, 143, 115], 
    [142, 115, 143], 
    [143, 108, 109], 
    [109, 141, 143], 
    [142, 135, 134], 
    [144, 142, 134], 
    [144, 115, 142], 
    [144, 134, 130], 
    [127, 144, 130], 
    [114, 144, 127], 
    [144, 114, 115], 
    [141, 109, 93], 
    [93, 139, 141], 
    [86, 138, 139], 
    [139, 90, 86], 
    [139, 93, 90], 
    [86, 88, 138], 
    [127, 113, 114], 
    [145, 123, 125], 
    [147, 146, 145], 
    [146, 122, 145], 
    [145, 122, 123], 
    [147, 148, 146], 
    [148, 149, 146], 
    [150, 151, 149], 
    [146, 149, 151], 
    [122, 146, 151], 
    [151, 150, 120], 
    [117, 151, 120], 
    [122, 151, 117], 
    [152, 120, 150], 
    [153, 119, 152], 
    [152, 119, 120], 
    [154, 119, 153], 
    [155, 156, 154], 
    [119, 154, 118], 
    [118, 154, 156], 
    [111, 118, 156], 
    [156, 155, 106], 
    [156, 106, 111], 
    [155, 157, 106], 
    [101, 157, 102], 
    [157, 101, 106], 
    [109, 104, 93], 
    [104, 94, 93], 
    [97, 87, 91], 
    [97, 158, 87], 
    [87, 158, 84], 
    [84, 158, 159], 
    [82, 84, 159], 
    [74, 153, 73], 
    [75, 154, 74], 
    [77, 155, 75], 
    [22, 157, 77], 
    [20, 102, 22], 
    [19, 100, 20], 
    [18, 99, 19], 
    [17, 98, 18], 
    [78, 97, 17], 
    [79, 158, 78], 
    [79, 82, 159], 
    [2, 80, 82], 
    [81, 0, 1], 
    [88, 1, 8], 
    [138, 8, 58], 
    [137, 58, 57], 
    [57, 136, 137], 
    [133, 56, 53], 
    [53, 132, 133], 
    [131, 52, 51], 
    [49, 131, 51], 
    [128, 49, 48], 
    [126, 48, 46], 
    [125, 46, 45], 
    [145, 45, 65], 
    [65, 147, 145], 
    [148, 67, 68], 
    [68, 149, 148], 
    [70, 149, 69], 
    [72, 150, 70], 
    [73, 152, 72], 
    [74, 154, 153], 
    [75, 155, 154], 
    [77, 157, 155], 
    [22, 102, 157], 
    [20, 100, 102], 
    [19, 99, 100], 
    [18, 98, 99], 
    [17, 97, 98], 
    [78, 158, 97], 
    [79, 159, 158], 
    [79, 2, 82], 
    [2, 0, 80], 
    [81, 80, 0], 
    [88, 81, 1], 
    [138, 88, 8], 
    [137, 138, 58], 
    [57, 56, 136], 
    [133, 136, 56], 
    [53, 52, 132], 
    [131, 132, 52], 
    [49, 129, 131], 
    [128, 129, 49], 
    [126, 128, 48], 
    [125, 126, 46], 
    [145, 125, 45], 
    [65, 67, 147], 
    [148, 147, 67], 
    [68, 69, 149], 
    [70, 150, 149], 
    [72, 152, 150], 
    [73, 153, 152]
] # synapse_wall_list

synapse = m.GeometryObject(
    name = 'synapse',
    vertex_list = synapse_vertex_list,
    wall_list = synapse_wall_list,
    surface_regions = []
)
# ^^^^ synapse ^^^^

