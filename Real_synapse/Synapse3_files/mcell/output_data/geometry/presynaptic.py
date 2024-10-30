import mcell as m

# ---- presynaptic ----
presynaptic_vertex_list = [
    [2.15521693229675, -2.56104135513306, -0.857018768787384], 
    [2.14599776268005, -2.52445387840271, -0.8470618724823], 
    [2.16130328178406, -2.58718371391296, -0.872766613960266], 
    [2.1735475063324, -2.56270408630371, -0.884056866168976], 
    [2.16467213630676, -2.53539037704468, -0.873603343963623], 
    [2.15873789787292, -2.50516986846924, -0.876377463340759], 
    [2.17083811759949, -2.51809000968933, -0.894416689872742], 
    [2.17901301383972, -2.53936982154846, -0.900067448616028], 
    [2.18706560134888, -2.54116630554199, -0.928635478019714], 
    [2.18376207351685, -2.56079077720642, -0.909809648990631], 
    [2.18084979057312, -2.51723337173462, -0.918260216712952], 
    [2.17307233810425, -2.49464082717896, -0.903875112533569], 
    [2.1834409236908, -2.49436283111572, -0.932371199131012], 
    [2.18870759010315, -2.51921987533569, -0.947211742401123], 
    [2.19625353813171, -2.54528832435608, -0.95561957359314], 
    [2.19480037689209, -2.49465489387512, -0.959863066673279], 
    [2.20618939399719, -2.52238607406616, -0.977632820606232], 
    [2.22607398033142, -2.5404736995697, -0.998647689819336], 
    [2.20677161216736, -2.49011635780334, -0.984718680381775], 
    [2.22587323188782, -2.50601434707642, -1.00234258174896], 
    [2.21194815635681, -2.55716228485107, -0.978396475315094], 
    [2.2117395401001, -2.59124135971069, -0.973457098007202], 
    [2.20162534713745, -2.57095384597778, -0.956568598747253], 
    [2.22722196578979, -2.57434225082397, -1.001011967659], 
    [2.24632430076599, -2.55516934394836, -1.02070510387421], 
    [2.2274329662323, -2.606285572052, -1.00192999839783], 
    [2.21968579292297, -2.61741471290588, -0.976932406425476], 
    [2.22278475761414, -2.63814973831177, -0.9615678191185], 
    [2.20985770225525, -2.61736917495728, -0.946690201759338], 
    [2.19718432426453, -2.59341859817505, -0.937544226646423], 
    [2.21100974082947, -2.6435010433197, -0.924450397491455], 
    [2.19331979751587, -2.61699986457825, -0.916317462921143], 
    [2.17138743400574, -2.61327791213989, -0.88322639465332], 
    [2.18212962150574, -2.58880829811096, -0.904928505420685], 
    [2.18757081031799, -2.63947486877441, -0.892687261104584], 
    [2.19979810714722, -2.66847777366638, -0.89720344543457], 
    [2.21804642677307, -2.67420840263367, -0.923901319503784], 
    [2.22681927680969, -2.66245007514954, -0.949416697025299], 
    [2.1887378692627, -2.56740117073059, -0.93422931432724], 
    [2.26937675476074, -2.54606652259827, -1.04687368869781], 
    [2.25893545150757, -2.52746772766113, -1.0318341255188], 
    [2.2416615486145, -2.52582120895386, -1.01474213600159], 
    [2.25148844718933, -2.4992892742157, -1.0307332277298], 
    [2.24639058113098, -2.45918154716492, -1.03481638431549], 
    [2.23550200462341, -2.48007321357727, -1.01770615577698], 
    [2.2675883769989, -2.51334476470947, -1.05096709728241], 
    [2.26068305969238, -2.4820122718811, -1.05420708656311], 
    [2.25498676300049, -2.44716906547546, -1.05657160282135], 
    [2.24725317955017, -2.42456340789795, -1.04107809066772], 
    [2.24807024002075, -2.39255332946777, -1.05077791213989], 
    [2.23710632324219, -2.4033989906311, -1.02336668968201], 
    [2.2353892326355, -2.43028163909912, -1.01641058921814], 
    [2.21706008911133, -2.43212151527405, -0.995218575000763], 
    [2.21987724304199, -2.40491104125977, -1.00050580501556], 
    [2.22845458984375, -2.4558413028717, -1.00973641872406], 
    [2.21982288360596, -2.47843170166016, -1.00209307670593], 
    [2.21224975585938, -2.45897102355957, -0.988979399204254], 
    [2.20191764831543, -2.43733763694763, -0.974098324775696], 
    [2.19817614555359, -2.46771121025085, -0.968842208385468], 
    [2.19009566307068, -2.44774222373962, -0.955448746681213], 
    [2.18677091598511, -2.47048664093018, -0.944383263587952], 
    [2.17907071113586, -2.44549798965454, -0.932713508605957], 
    [2.1734573841095, -2.47028851509094, -0.91851806640625], 
    [2.1563606262207, -2.47520709037781, -0.890612483024597], 
    [2.16184258460999, -2.44458508491516, -0.909450352191925], 
    [2.17319774627686, -2.41990494728088, -0.927010893821716], 
    [2.14370608329773, -2.44940042495728, -0.8857421875], 
    [2.14710021018982, -2.42749428749084, -0.895444869995117], 
    [2.15757012367249, -2.41474318504333, -0.909743666648865], 
    [2.1600866317749, -2.39300727844238, -0.919360399246216], 
    [2.17786383628845, -2.39743041992188, -0.937912583351135], 
    [2.14753365516663, -2.36958360671997, -0.916360676288605], 
    [2.16902494430542, -2.37331080436707, -0.933281123638153], 
    [2.15612387657166, -2.34508228302002, -0.932724356651306], 
    [2.17706108093262, -2.35703897476196, -0.950407862663269], 
    [2.19163870811462, -2.38333463668823, -0.957876801490784], 
    [2.20621776580811, -2.37816476821899, -0.98353785276413], 
    [2.18844032287598, -2.41909313201904, -0.952980816364288], 
    [2.20332455635071, -2.40801668167114, -0.977161288261414], 
    [2.19412922859192, -2.35310316085815, -0.97010350227356], 
    [2.18835878372192, -2.32483077049255, -0.980182290077209], 
    [2.20871567726135, -2.3472855091095, -0.995700240135193], 
    [2.2281129360199, -2.35553479194641, -1.01956355571747], 
    [2.22227740287781, -2.3776535987854, -1.00620949268341], 
    [2.22101163864136, -2.3311026096344, -1.01426124572754], 
    [2.20039796829224, -2.31170988082886, -1.00774013996124], 
    [2.22934508323669, -2.30793976783752, -1.02392959594727], 
    [2.23860645294189, -2.33544564247131, -1.03235924243927], 
    [2.24391007423401, -2.36120057106018, -1.04307377338409], 
    [2.23731565475464, -2.37892985343933, -1.02760171890259], 
    [2.17295479774475, -2.33224487304688, -0.955793857574463], 
    [2.15203666687012, -2.31655502319336, -0.941056609153748], 
    [2.16552972793579, -2.30787873268127, -0.965470492839813], 
    [2.14531326293945, -2.29488110542297, -0.954452991485596], 
    [2.1292712688446, -2.29864573478699, -0.935267686843872], 
    [2.12908387184143, -2.32166075706482, -0.920360803604126], 
    [2.13376307487488, -2.34713792800903, -0.914026618003845], 
    [2.13214683532715, -2.42772626876831, -0.879911065101624], 
    [2.12419676780701, -2.44563388824463, -0.862302422523499], 
    [2.13710641860962, -2.46690678596497, -0.867426753044128], 
    [2.13977813720703, -2.49231457710266, -0.857128739356995]
] # presynaptic_vertex_list

presynaptic_wall_list = [
    [1, 4, 0], 
    [0, 3, 2], 
    [0, 4, 3], 
    [1, 5, 4], 
    [5, 6, 4], 
    [4, 7, 3], 
    [6, 7, 4], 
    [8, 9, 7], 
    [10, 8, 7], 
    [3, 7, 9], 
    [10, 7, 6], 
    [6, 11, 10], 
    [11, 12, 10], 
    [12, 13, 10], 
    [10, 13, 8], 
    [13, 16, 14], 
    [8, 13, 14], 
    [15, 13, 12], 
    [15, 16, 13], 
    [14, 16, 20], 
    [15, 18, 16], 
    [16, 19, 17], 
    [20, 16, 17], 
    [18, 19, 16], 
    [20, 23, 21], 
    [21, 22, 20], 
    [22, 14, 20], 
    [17, 23, 20], 
    [21, 23, 25], 
    [17, 24, 23], 
    [21, 25, 26], 
    [21, 26, 28], 
    [27, 28, 26], 
    [21, 28, 29], 
    [29, 28, 31], 
    [30, 28, 27], 
    [30, 31, 28], 
    [31, 34, 32], 
    [32, 33, 31], 
    [33, 29, 31], 
    [34, 31, 30], 
    [30, 35, 34], 
    [30, 36, 35], 
    [30, 37, 36], 
    [30, 27, 37], 
    [38, 29, 33], 
    [38, 33, 9], 
    [3, 9, 33], 
    [2, 3, 33], 
    [33, 32, 2], 
    [8, 14, 38], 
    [9, 8, 38], 
    [38, 22, 29], 
    [14, 22, 38], 
    [29, 22, 21], 
    [17, 41, 24], 
    [40, 39, 24], 
    [24, 41, 40], 
    [40, 41, 42], 
    [19, 42, 41], 
    [19, 41, 17], 
    [42, 43, 46], 
    [44, 43, 42], 
    [40, 42, 45], 
    [19, 44, 42], 
    [46, 45, 42], 
    [47, 46, 43], 
    [43, 48, 47], 
    [49, 48, 50], 
    [51, 50, 48], 
    [48, 43, 51], 
    [51, 43, 54], 
    [53, 50, 51], 
    [51, 52, 53], 
    [51, 54, 52], 
    [56, 54, 55], 
    [54, 44, 55], 
    [43, 44, 54], 
    [56, 52, 54], 
    [56, 55, 18], 
    [58, 56, 18], 
    [52, 56, 57], 
    [58, 57, 56], 
    [58, 60, 59], 
    [59, 57, 58], 
    [58, 18, 15], 
    [15, 60, 58], 
    [59, 60, 61], 
    [12, 60, 15], 
    [62, 61, 60], 
    [60, 12, 62], 
    [64, 61, 62], 
    [12, 11, 62], 
    [63, 62, 11], 
    [64, 62, 63], 
    [65, 61, 64], 
    [65, 64, 68], 
    [64, 63, 66], 
    [64, 66, 67], 
    [68, 64, 67], 
    [68, 69, 65], 
    [69, 72, 70], 
    [65, 69, 70], 
    [72, 69, 71], 
    [73, 72, 71], 
    [74, 72, 73], 
    [72, 75, 70], 
    [75, 72, 74], 
    [70, 75, 77], 
    [75, 79, 76], 
    [76, 78, 75], 
    [77, 75, 78], 
    [80, 81, 79], 
    [79, 81, 76], 
    [81, 83, 76], 
    [80, 85, 81], 
    [81, 84, 82], 
    [82, 83, 81], 
    [81, 85, 84], 
    [86, 84, 85], 
    [84, 86, 87], 
    [82, 87, 88], 
    [84, 87, 82], 
    [89, 88, 49], 
    [89, 82, 88], 
    [83, 82, 89], 
    [49, 50, 89], 
    [89, 50, 83], 
    [83, 53, 76], 
    [50, 53, 83], 
    [76, 53, 78], 
    [57, 78, 52], 
    [78, 53, 52], 
    [78, 57, 77], 
    [61, 77, 59], 
    [77, 57, 59], 
    [70, 77, 65], 
    [77, 61, 65], 
    [73, 90, 74], 
    [73, 91, 90], 
    [91, 92, 90], 
    [93, 92, 91], 
    [91, 94, 93], 
    [95, 94, 91], 
    [95, 91, 73], 
    [96, 95, 73], 
    [73, 71, 96], 
    [97, 67, 66], 
    [97, 66, 98], 
    [98, 66, 99], 
    [99, 66, 63], 
    [99, 63, 100], 
    [100, 5, 1], 
    [100, 63, 5], 
    [5, 63, 11], 
    [18, 55, 19], 
    [55, 44, 19], 
    [45, 39, 40], 
    [11, 6, 5]
] # presynaptic_wall_list

presynaptic = m.GeometryObject(
    name = 'presynaptic',
    vertex_list = presynaptic_vertex_list,
    wall_list = presynaptic_wall_list,
    surface_regions = []
)
# ^^^^ presynaptic ^^^^


