import mcell as m

# ---- presynaptic ----
presynaptic_vertex_list = [
    [0.0999112725257874, 0.0160531997680664, 0.0718183517456055], 
    [0.0903278589248657, -0.00198888778686523, 0.0489034652709961], 
    [0.107994049787521, 0.0151681900024414, 0.0387250185012817], 
    [0.0797344446182251, -0.0121245384216309, 0.0739346146583557], 
    [0.118552446365356, 0.0344963073730469, 0.0576627254486084], 
    [0.133431553840637, 0.0598907470703125, 0.0578619241714478], 
    [0.128662139177322, 0.0351352691650391, 0.0334256887435913], 
    [0.130638003349304, 0.0428018569946289, 0.00780677795410156], 
    [0.111348301172256, 0.021843433380127, 0.00972235202789307], 
    [0.142948359251022, 0.0597720146179199, 0.0290037393569946], 
    [0.139941394329071, 0.0672817230224609, -0.0036768913269043], 
    [0.115787982940674, 0.0428338050842285, -0.0187417268753052], 
    [0.140233665704727, 0.0915517807006836, -0.0190153121948242], 
    [0.126916527748108, 0.0705366134643555, -0.0299134254455566], 
    [0.112384021282196, 0.0863375663757324, -0.045076847076416], 
    [0.125710844993591, 0.110818386077881, -0.0332775115966797], 
    [0.105620175600052, 0.0603795051574707, -0.0439627170562744], 
    [0.0906993746757507, 0.0377693176269531, -0.0358479022979736], 
    [0.080234169960022, 0.0587615966796875, -0.0599110126495361], 
    [0.09709832072258, 0.0807266235351562, -0.0624969005584717], 
    [0.0787039995193481, 0.0800337791442871, -0.0788168907165527], 
    [0.0900079607963562, 0.102927207946777, -0.0770847797393799], 
    [0.108951449394226, 0.108709335327148, -0.0562630891799927], 
    [0.0540095567703247, 0.0647807121276855, -0.0895993709564209], 
    [0.055605411529541, 0.0464253425598145, -0.0639814138412476], 
    [0.0243327617645264, 0.0541596412658691, -0.0908071994781494], 
    [0.0327009558677673, 0.0418567657470703, -0.0705254077911377], 
    [0.0137173533439636, 0.0283122062683105, -0.0580503940582275], 
    [0.0395180583000183, 0.0278797149658203, -0.0446795225143433], 
    [0.0106064677238464, 0.039860725402832, -0.0792868137359619], 
    [-0.00881999731063843, 0.0289549827575684, -0.0725516080856323], 
    [-0.00797700881958008, 0.0451526641845703, -0.106204271316528], 
    [-0.0405056476593018, 0.0303964614868164, -0.102908611297607], 
    [-0.0281544923782349, 0.0278291702270508, -0.0852787494659424], 
    [-0.034640908241272, 0.0177021026611328, -0.0619664192199707], 
    [-0.0526028275489807, 0.0206356048583984, -0.0872644186019897], 
    [-0.0828006863594055, 0.0145382881164551, -0.0907355546951294], 
    [-0.0642418265342712, 0.0247111320495605, -0.10977029800415], 
    [-0.0640588998794556, 0.0120859146118164, -0.068372368812561], 
    [-0.0873412489891052, -0.000145435333251953, -0.0567585229873657], 
    [-0.0536794066429138, 0.00654411315917969, -0.0469825267791748], 
    [-0.0636988282203674, -0.00716352462768555, -0.0269843339920044], 
    [-0.0258935689926147, 0.00605535507202148, -0.0283807516098022], 
    [0.00451189279556274, 0.00323247909545898, -0.0132386684417725], 
    [-0.0426624417304993, -0.0130248069763184, -0.00952506065368652], 
    [0.0121777653694153, 0.0168371200561523, -0.0347529649734497], 
    [-0.00938141345977783, 0.0184588432312012, -0.050815224647522], 
    [-0.016310453414917, -0.00974559783935547, -0.00202751159667969], 
    [0.0186032056808472, -0.00842094421386719, 0.00902748107910156], 
    [-0.0401478409767151, -0.030301570892334, 0.0137882232666016], 
    [-0.00713413953781128, -0.023829460144043, 0.0171017646789551], 
    [-0.0161187052726746, -0.0462551116943359, 0.026922345161438], 
    [0.0174190402030945, -0.0295133590698242, 0.0293921232223511], 
    [0.0448413491249084, -0.0171623229980469, 0.0274485349655151], 
    [0.0403412580490112, -0.0382676124572754, 0.0480968952178955], 
    [0.0147051811218262, -0.0523324012756348, 0.041837215423584], 
    [0.00558221340179443, -0.0788173675537109, 0.0516796112060547], 
    [0.0285795331001282, -0.0665855407714844, 0.0599362850189209], 
    [-0.00596517324447632, -0.0643100738525391, 0.0394265651702881], 
    [-0.028594970703125, -0.0831522941589355, 0.0362989902496338], 
    [-0.0265550017356873, -0.116990089416504, 0.0418292284011841], 
    [-0.00288820266723633, -0.104090213775635, 0.049544095993042], 
    [-0.0642278790473938, -0.0821418762207031, 0.0190880298614502], 
    [-0.0437163114547729, -0.0579218864440918, 0.0223376750946045], 
    [-0.0481038689613342, -0.107626914978027, 0.0291056632995605], 
    [-0.0486207008361816, -0.135781288146973, 0.0371192693710327], 
    [-0.0741426348686218, -0.123996734619141, 0.0237518548965454], 
    [-0.0902199745178223, -0.100262641906738, 0.0126869678497314], 
    [-0.0713533759117126, -0.15315055847168, 0.0386321544647217], 
    [-0.103554368019104, -0.12739372253418, 0.0148358345031738], 
    [-0.0966312885284424, -0.14886474609375, 0.0273478031158447], 
    [-0.0493820905685425, -0.16105842590332, 0.0539093017578125], 
    [-0.0266451835632324, -0.143449783325195, 0.0522949695587158], 
    [-0.00656372308731079, -0.128722667694092, 0.0554660558700562], 
    [0.0145440697669983, -0.121870517730713, 0.0676525831222534], 
    [0.0206257700920105, -0.0934257507324219, 0.0647342205047607], 
    [0.0412543416023254, -0.0819149017333984, 0.0825760364532471], 
    [0.0450705885887146, -0.0506963729858398, 0.0713024139404297], 
    [0.0591095089912415, -0.0311746597290039, 0.0631729364395142], 
    [0.0604632496833801, -0.0342812538146973, 0.0847233533859253], 
    [0.0691265463829041, -0.0189213752746582, 0.0421926975250244], 
    [0.0832878351211548, -0.00055694580078125, 0.0180143117904663], 
    [0.0917379260063171, 0.0193076133728027, -0.0123085975646973], 
    [0.0657160878181458, 0.00946664810180664, -0.00690174102783203], 
    [0.0474246144294739, -5.29289245605469e-05, 0.00701463222503662], 
    [0.0352299213409424, 0.011042594909668, -0.0168637037277222], 
    [0.0640237331390381, 0.0228571891784668, -0.0280262231826782], 
    [0.0665903091430664, 0.0387873649597168, -0.0458731651306152], 
    [-0.0933045744895935, -0.0692520141601562, 0.00456047058105469], 
    [-0.069010853767395, -0.0501747131347656, 0.0103307962417603], 
    [-0.0922755002975464, -0.0427823066711426, -0.0101730823516846], 
    [-0.0892787575721741, -0.0203347206115723, -0.0290451049804688], 
    [-0.116752922534943, -0.0337128639221191, -0.0296992063522339], 
    [-0.0672547817230225, -0.026273250579834, -0.00676178932189941], 
    [-0.110539197921753, -0.0169320106506348, -0.0465229749679565], 
    [-0.124425828456879, -0.011138916015625, -0.067874550819397], 
    [-0.107315003871918, 0.00168323516845703, -0.083464503288269], 
    [-0.136098384857178, -0.00517702102661133, -0.0937305688858032], 
    [-0.110972464084625, 0.00583982467651367, -0.109346389770508], 
    [-0.0867326259613037, 0.0140261650085449, -0.121919870376587]
] # presynaptic_vertex_list

presynaptic_wall_list = [
    [1, 2, 0], 
    [3, 1, 0], 
    [2, 4, 0], 
    [4, 6, 5], 
    [2, 6, 4], 
    [6, 8, 7], 
    [6, 7, 9], 
    [8, 6, 2], 
    [5, 6, 9], 
    [7, 10, 9], 
    [11, 10, 7], 
    [10, 11, 13], 
    [13, 12, 10], 
    [12, 13, 15], 
    [11, 16, 13], 
    [14, 13, 16], 
    [14, 15, 13], 
    [17, 18, 16], 
    [11, 17, 16], 
    [18, 19, 16], 
    [14, 16, 19], 
    [18, 20, 19], 
    [19, 20, 21], 
    [19, 21, 22], 
    [14, 19, 22], 
    [22, 15, 14], 
    [18, 23, 20], 
    [26, 23, 24], 
    [24, 23, 18], 
    [26, 25, 23], 
    [29, 26, 27], 
    [27, 26, 28], 
    [29, 25, 26], 
    [24, 28, 26], 
    [30, 29, 27], 
    [31, 29, 30], 
    [29, 31, 25], 
    [33, 31, 30], 
    [33, 32, 31], 
    [34, 35, 33], 
    [30, 34, 33], 
    [35, 32, 33], 
    [35, 36, 37], 
    [38, 36, 35], 
    [38, 35, 34], 
    [37, 32, 35], 
    [38, 39, 36], 
    [40, 39, 38], 
    [38, 34, 40], 
    [41, 39, 40], 
    [41, 40, 42], 
    [42, 40, 34], 
    [44, 41, 42], 
    [47, 42, 43], 
    [42, 45, 43], 
    [44, 42, 47], 
    [42, 46, 45], 
    [42, 34, 46], 
    [47, 43, 48], 
    [50, 47, 48], 
    [47, 49, 44], 
    [49, 47, 50], 
    [51, 49, 50], 
    [50, 52, 51], 
    [50, 48, 52], 
    [48, 53, 52], 
    [52, 53, 54], 
    [51, 52, 55], 
    [54, 55, 52], 
    [55, 58, 51], 
    [55, 57, 56], 
    [56, 58, 55], 
    [57, 55, 54], 
    [58, 59, 51], 
    [56, 59, 58], 
    [59, 61, 60], 
    [60, 64, 59], 
    [59, 56, 61], 
    [59, 63, 51], 
    [59, 64, 62], 
    [62, 63, 59], 
    [60, 65, 64], 
    [66, 64, 65], 
    [62, 64, 66], 
    [67, 62, 66], 
    [66, 69, 67], 
    [66, 65, 68], 
    [68, 70, 66], 
    [66, 70, 69], 
    [71, 68, 65], 
    [65, 72, 71], 
    [73, 72, 60], 
    [65, 60, 72], 
    [74, 73, 61], 
    [73, 60, 61], 
    [61, 75, 74], 
    [75, 61, 56], 
    [75, 56, 57], 
    [75, 57, 76], 
    [76, 57, 77], 
    [54, 78, 77], 
    [77, 78, 79], 
    [77, 57, 54], 
    [79, 78, 3], 
    [3, 78, 80], 
    [78, 54, 80], 
    [80, 1, 3], 
    [80, 81, 1], 
    [80, 54, 53], 
    [53, 81, 80], 
    [81, 2, 1], 
    [53, 84, 81], 
    [81, 82, 8], 
    [81, 8, 2], 
    [83, 82, 81], 
    [81, 84, 83], 
    [53, 48, 84], 
    [84, 85, 83], 
    [48, 85, 84], 
    [85, 28, 86], 
    [85, 86, 83], 
    [45, 28, 85], 
    [43, 45, 85], 
    [48, 43, 85], 
    [87, 17, 86], 
    [82, 86, 17], 
    [86, 82, 83], 
    [86, 28, 87], 
    [87, 18, 17], 
    [87, 24, 18], 
    [28, 24, 87], 
    [8, 82, 11], 
    [17, 11, 82], 
    [88, 62, 67], 
    [62, 88, 89], 
    [90, 89, 88], 
    [89, 90, 93], 
    [92, 91, 90], 
    [93, 90, 91], 
    [89, 93, 49], 
    [49, 93, 44], 
    [93, 41, 44], 
    [93, 91, 41], 
    [94, 91, 92], 
    [94, 39, 91], 
    [95, 39, 94], 
    [97, 96, 95], 
    [95, 96, 39], 
    [97, 98, 96], 
    [98, 99, 36], 
    [96, 98, 36], 
    [36, 99, 37], 
    [36, 39, 96], 
    [41, 91, 39], 
    [89, 63, 62], 
    [63, 89, 49], 
    [51, 63, 49], 
    [45, 46, 27], 
    [30, 27, 46], 
    [46, 34, 30], 
    [45, 27, 28], 
    [11, 7, 8]
] # presynaptic_wall_list

presynaptic = m.GeometryObject(
    name = 'presynaptic',
    vertex_list = presynaptic_vertex_list,
    wall_list = presynaptic_wall_list,
    surface_regions = []
)
# ^^^^ presynaptic ^^^^


