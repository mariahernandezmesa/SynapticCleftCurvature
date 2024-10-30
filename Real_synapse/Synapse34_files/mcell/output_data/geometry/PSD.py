import mcell as m

# ---- PSD ----
PSD_vertex_list = [
    [0.0898510217666626, -0.0813131332397461, 0.0826286673545837], 
    [0.0763126611709595, -0.0645790100097656, 0.063194215297699], 
    [0.0539406538009644, -0.0746126174926758, 0.0787742733955383], 
    [0.103955745697021, -0.0664615631103516, 0.0558821558952332], 
    [0.115319967269897, -0.0456247329711914, 0.0343375205993652], 
    [0.0780222415924072, -0.0452728271484375, 0.0427796244621277], 
    [0.0515350103378296, -0.0564613342285156, 0.056867241859436], 
    [0.094391942024231, -0.02728271484375, 0.027651309967041], 
    [0.0631839036941528, -0.0128793716430664, 0.0239825248718262], 
    [0.0456914901733398, -0.0375328063964844, 0.0394467711448669], 
    [0.0322718620300293, -0.0193233489990234, 0.0271397233009338], 
    [0.0132961273193359, -0.0353212356567383, 0.0339552760124207], 
    [0.0221508741378784, -0.0543708801269531, 0.0488336682319641], 
    [-0.0065467357635498, -0.054905891418457, 0.0403651595115662], 
    [0.0298737287521362, -0.0688991546630859, 0.0656314492225647], 
    [0.00098109245300293, -0.073796272277832, 0.0607682466506958], 
    [-0.0284988880157471, -0.072941780090332, 0.0440647006034851], 
    [-0.0235062837600708, -0.0887012481689453, 0.0632414221763611], 
    [0.0189331769943237, -0.0834140777587891, 0.082368016242981], 
    [-0.00876724720001221, -0.0918130874633789, 0.0840689539909363], 
    [-0.0386505126953125, -0.101686477661133, 0.0804342031478882], 
    [-0.0706971883773804, -0.105683326721191, 0.0704468488693237], 
    [-0.0486639738082886, -0.0915765762329102, 0.0541260838508606], 
    [-0.0573631525039673, -0.106643676757812, 0.0999802350997925], 
    [-0.0813374519348145, -0.101405143737793, 0.092911958694458], 
    [-0.101069569587708, -0.102055549621582, 0.0747077465057373], 
    [-0.100231051445007, -0.104074478149414, 0.0480024218559265], 
    [-0.125987648963928, -0.0986204147338867, 0.0297815203666687], 
    [-0.0927239656448364, -0.0914134979248047, 0.0250064134597778], 
    [-0.073462963104248, -0.0958662033081055, 0.044550359249115], 
    [-0.0580391883850098, -0.0753107070922852, 0.029327929019928], 
    [-0.0634912252426147, -0.0450773239135742, 0.0148377418518066], 
    [-0.0358872413635254, -0.0522031784057617, 0.0292689204216003], 
    [-0.0832959413528442, -0.0684337615966797, 0.0135120749473572], 
    [-0.110260009765625, -0.0794649124145508, 0.00752741098403931], 
    [-0.0993502140045166, -0.0489587783813477, -0.000715017318725586], 
    [-0.130775332450867, -0.0656194686889648, -0.00957846641540527], 
    [-0.101384162902832, -0.0175504684448242, -0.0192825794219971], 
    [-0.0796476602554321, -0.0260744094848633, -0.00110983848571777], 
    [-0.120237588882446, -0.0406808853149414, -0.0189571976661682], 
    [-0.142059445381165, -0.0488071441650391, -0.0312957763671875], 
    [-0.126397490501404, -0.0269107818603516, -0.0394410490989685], 
    [-0.112373352050781, -0.00286293029785156, -0.0431926250457764], 
    [-0.136703372001648, -0.0149192810058594, -0.061201274394989], 
    [-0.119693875312805, 0.00674819946289062, -0.067430853843689], 
    [-0.100935220718384, 0.0343666076660156, -0.0732346773147583], 
    [-0.100307941436768, 0.0186967849731445, -0.0526732802391052], 
    [-0.0859920978546143, 0.0153093338012695, -0.0289115905761719], 
    [-0.0853410959243774, 0.040888786315918, -0.0486041903495789], 
    [-0.0844452381134033, 0.0630636215209961, -0.0771902203559875], 
    [-0.0595772266387939, 0.0443058013916016, -0.0267661809921265], 
    [-0.0700037479400635, 0.0622053146362305, -0.0504791140556335], 
    [-0.0545164346694946, 0.0852365493774414, -0.0635248422622681], 
    [-0.0486522912979126, 0.0684137344360352, -0.0428046584129333], 
    [-0.0319308042526245, 0.0644979476928711, -0.0282741189002991], 
    [-0.0251106023788452, 0.0848321914672852, -0.0413041710853577], 
    [-0.0274713039398193, 0.100194931030273, -0.0626716613769531], 
    [0.00100159645080566, 0.103652954101562, -0.053672194480896], 
    [-0.00736033916473389, 0.0693340301513672, -0.0226972103118896], 
    [0.00251281261444092, 0.0862817764282227, -0.0358958840370178], 
    [0.0194053649902344, 0.0743751525878906, -0.0253411531448364], 
    [0.0262967348098755, 0.0952463150024414, -0.0391429662704468], 
    [0.0349351167678833, 0.111283302307129, -0.0585276484489441], 
    [0.0542707443237305, 0.0991144180297852, -0.045439600944519], 
    [0.0468052625656128, 0.0804243087768555, -0.0300747156143188], 
    [0.065696120262146, 0.0630912780761719, -0.0167495608329773], 
    [0.0383340120315552, 0.0632028579711914, -0.0161793828010559], 
    [0.0733644962310791, 0.0817642211914062, -0.0358138680458069], 
    [0.093281626701355, 0.0642023086547852, -0.0271731615066528], 
    [0.0785077810287476, 0.0968151092529297, -0.0560811161994934], 
    [0.0998190641403198, 0.0845727920532227, -0.048348605632782], 
    [0.0992423295974731, 0.103781700134277, -0.0781749486923218], 
    [0.122779488563538, 0.083770751953125, -0.064078152179718], 
    [0.120943784713745, 0.0662403106689453, -0.0424851775169373], 
    [0.145086884498596, 0.0651750564575195, -0.0609644651412964], 
    [0.116214752197266, 0.0472383499145508, -0.0235717296600342], 
    [0.142856359481812, 0.0472221374511719, -0.0374531149864197], 
    [0.139962196350098, 0.0286808013916016, -0.0173067450523376], 
    [0.132487297058105, 0.00818347930908203, -6.33597373962402e-05], 
    [0.115493893623352, 0.0268306732177734, -0.00872385501861572], 
    [0.0842791795730591, 0.0387744903564453, -0.00550550222396851], 
    [0.104844689369202, 0.00928306579589844, 0.00421315431594849], 
    [0.121120810508728, -0.0171518325805664, 0.0168498158454895], 
    [0.0925376415252686, -0.00725746154785156, 0.01630038022995], 
    [0.0788999795913696, 0.0109577178955078, 0.00993120670318604], 
    [0.0530984401702881, 0.0184059143066406, 0.00816726684570312], 
    [0.0297503471374512, 0.00323009490966797, 0.0161653161048889], 
    [0.0223827362060547, 0.0268564224243164, 0.00398659706115723], 
    [0.047171950340271, 0.0432796478271484, -0.00381225347518921], 
    [0.0121763944625854, 0.051971435546875, -0.00858867168426514], 
    [-0.0200651884078979, 0.0492010116577148, -0.0131950378417969], 
    [-0.00818824768066406, 0.0302219390869141, -0.00121879577636719], 
    [-0.000146389007568359, 0.00873470306396484, 0.0117006897926331], 
    [-0.0308269262313843, 0.0107946395874023, 0.00408124923706055], 
    [-0.0367125272750854, 0.0299158096313477, -0.00959056615829468], 
    [-0.0593656301498413, 0.0165119171142578, -0.0090261697769165], 
    [-0.0540797710418701, -0.0103063583374023, 0.00589978694915771], 
    [-0.0773739814758301, -0.00279617309570312, -0.00907760858535767], 
    [-0.0214066505432129, -0.0100393295288086, 0.0164716839790344], 
    [-0.0389696359634399, -0.0292129516601562, 0.019785463809967], 
    [-0.0137628316879272, -0.0322656631469727, 0.0276136994361877], 
    [0.00631225109100342, -0.0136032104492188, 0.0228092074394226], 
    [0.143767595291138, 0.0897760391235352, -0.0905596017837524], 
    [0.0637977123260498, 0.112910270690918, -0.0711749792098999]
] # PSD_vertex_list

PSD_wall_list = [
    [0, 1, 3], 
    [0, 2, 1], 
    [1, 5, 3], 
    [3, 5, 4], 
    [6, 5, 1], 
    [9, 5, 6], 
    [5, 8, 7], 
    [7, 4, 5], 
    [5, 9, 8], 
    [6, 12, 9], 
    [10, 9, 11], 
    [9, 10, 8], 
    [12, 11, 9], 
    [14, 12, 6], 
    [13, 12, 15], 
    [11, 12, 13], 
    [14, 15, 12], 
    [15, 16, 13], 
    [15, 17, 16], 
    [15, 14, 18], 
    [17, 15, 19], 
    [18, 19, 15], 
    [19, 20, 17], 
    [22, 17, 20], 
    [20, 21, 22], 
    [23, 21, 20], 
    [21, 23, 24], 
    [24, 25, 21], 
    [25, 26, 21], 
    [26, 27, 28], 
    [21, 26, 29], 
    [26, 28, 29], 
    [28, 30, 29], 
    [30, 22, 29], 
    [29, 22, 21], 
    [22, 30, 16], 
    [31, 32, 30], 
    [30, 33, 31], 
    [30, 32, 16], 
    [30, 28, 33], 
    [33, 34, 35], 
    [34, 33, 28], 
    [33, 35, 31], 
    [35, 34, 36], 
    [35, 36, 39], 
    [31, 35, 38], 
    [35, 37, 38], 
    [39, 37, 35], 
    [36, 40, 39], 
    [41, 37, 39], 
    [39, 40, 41], 
    [41, 43, 42], 
    [37, 41, 42], 
    [43, 44, 42], 
    [46, 44, 45], 
    [42, 44, 46], 
    [48, 46, 45], 
    [42, 46, 47], 
    [46, 48, 47], 
    [48, 45, 49], 
    [49, 51, 48], 
    [48, 51, 50], 
    [47, 48, 50], 
    [49, 52, 51], 
    [50, 51, 53], 
    [53, 51, 52], 
    [54, 50, 53], 
    [53, 55, 54], 
    [52, 55, 53], 
    [56, 57, 55], 
    [55, 52, 56], 
    [54, 55, 58], 
    [57, 59, 55], 
    [58, 55, 59], 
    [60, 59, 61], 
    [59, 60, 58], 
    [59, 57, 61], 
    [62, 61, 57], 
    [61, 62, 63], 
    [64, 61, 63], 
    [61, 64, 60], 
    [63, 67, 64], 
    [64, 67, 65], 
    [65, 66, 64], 
    [60, 64, 66], 
    [63, 69, 67], 
    [65, 67, 68], 
    [68, 67, 70], 
    [67, 69, 70], 
    [71, 70, 69], 
    [71, 72, 70], 
    [73, 70, 72], 
    [70, 73, 68], 
    [73, 72, 74], 
    [74, 76, 73], 
    [73, 76, 75], 
    [68, 73, 75], 
    [75, 76, 77], 
    [75, 77, 79], 
    [78, 79, 77], 
    [79, 80, 75], 
    [80, 79, 81], 
    [79, 78, 81], 
    [81, 78, 82], 
    [83, 81, 82], 
    [80, 81, 84], 
    [83, 84, 81], 
    [84, 85, 80], 
    [8, 85, 84], 
    [8, 84, 83], 
    [86, 85, 8], 
    [85, 88, 80], 
    [86, 87, 85], 
    [88, 85, 87], 
    [88, 66, 65], 
    [65, 80, 88], 
    [66, 88, 89], 
    [87, 89, 88], 
    [89, 60, 66], 
    [87, 91, 89], 
    [91, 90, 89], 
    [58, 89, 90], 
    [89, 58, 60], 
    [91, 92, 93], 
    [91, 87, 92], 
    [93, 94, 91], 
    [90, 91, 94], 
    [94, 95, 50], 
    [50, 90, 94], 
    [95, 94, 93], 
    [96, 95, 93], 
    [97, 95, 96], 
    [95, 47, 50], 
    [47, 95, 97], 
    [38, 97, 96], 
    [37, 97, 38], 
    [97, 37, 47], 
    [96, 31, 38], 
    [99, 31, 96], 
    [99, 96, 98], 
    [98, 96, 93], 
    [31, 99, 32], 
    [98, 100, 99], 
    [32, 99, 100], 
    [13, 32, 100], 
    [100, 11, 13], 
    [100, 98, 101], 
    [11, 100, 101], 
    [10, 101, 86], 
    [11, 101, 10], 
    [101, 98, 92], 
    [92, 86, 101], 
    [93, 92, 98], 
    [87, 86, 92], 
    [54, 58, 90], 
    [90, 50, 54], 
    [8, 10, 86], 
    [82, 7, 83], 
    [7, 8, 83], 
    [4, 7, 82], 
    [68, 80, 65], 
    [75, 80, 68], 
    [72, 102, 74], 
    [72, 71, 102], 
    [69, 103, 71], 
    [63, 103, 69], 
    [62, 103, 63], 
    [42, 47, 37], 
    [27, 34, 28], 
    [16, 32, 13], 
    [22, 16, 17], 
    [2, 18, 14], 
    [2, 14, 6], 
    [6, 1, 2]
] # PSD_wall_list

PSD = m.GeometryObject(
    name = 'PSD',
    vertex_list = PSD_vertex_list,
    wall_list = PSD_wall_list,
    surface_regions = []
)
# ^^^^ PSD ^^^^

