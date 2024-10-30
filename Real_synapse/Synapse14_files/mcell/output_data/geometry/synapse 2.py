import mcell as m

# ---- synapse ----
synapse_vertex_list = [
    [-0.304096728563309, 6.46807050704956, 2.22670650482178], 
    [-0.28722220659256, 6.47454214096069, 2.25418591499329], 
    [-0.334499180316925, 6.46178483963013, 2.23730039596558], 
    [-0.315065264701843, 6.47091674804688, 2.25480628013611], 
    [-0.338373839855194, 6.47381830215454, 2.27123880386353], 
    [-0.309394061565399, 6.48054075241089, 2.28606081008911], 
    [-0.335251867771149, 6.47887420654297, 2.30023169517517], 
    [-0.285667359828949, 6.47823047637939, 2.31241369247437], 
    [-0.314511001110077, 6.47692441940308, 2.32266688346863], 
    [-0.280888676643372, 6.48041915893555, 2.2841272354126], 
    [-0.254627734422684, 6.48189973831177, 2.29728388786316], 
    [-0.262410253286362, 6.47700262069702, 2.27001094818115], 
    [-0.261489272117615, 6.47421216964722, 2.24815106391907], 
    [-0.234443932771683, 6.48145151138306, 2.26257157325745], 
    [-0.204897850751877, 6.49106168746948, 2.2594690322876], 
    [-0.223073214292526, 6.48696756362915, 2.28967022895813], 
    [-0.206576496362686, 6.48614072799683, 2.31362009048462], 
    [-0.235531747341156, 6.4757137298584, 2.31425261497498], 
    [-0.19345135986805, 6.49612331390381, 2.28671455383301], 
    [-0.17630609869957, 6.50222301483154, 2.26049423217773], 
    [-0.177671015262604, 6.49715328216553, 2.31205415725708], 
    [-0.163093388080597, 6.50497913360596, 2.28598213195801], 
    [-0.147672981023788, 6.50354671478271, 2.31021904945374], 
    [-0.147337779402733, 6.50899314880371, 2.26228809356689], 
    [-0.123173512518406, 6.50563335418701, 2.2850706577301], 
    [-0.121590867638588, 6.49149751663208, 2.32246088981628], 
    [-0.156283140182495, 6.4870457649231, 2.33184313774109], 
    [-0.180734470486641, 6.48127222061157, 2.33410477638245], 
    [-0.201422363519669, 6.47207164764404, 2.33442211151123], 
    [-0.224152505397797, 6.46868801116943, 2.3335645198822], 
    [-0.261786937713623, 6.46843719482422, 2.33055734634399], 
    [-0.291207551956177, 6.46158504486084, 2.33951044082642], 
    [-0.321342289447784, 6.45473003387451, 2.3441162109375], 
    [-0.351715832948685, 6.44789934158325, 2.34827160835266], 
    [-0.346036702394485, 6.47516298294067, 2.33068752288818], 
    [-0.37596720457077, 6.46399021148682, 2.32921361923218], 
    [-0.36673629283905, 6.47749280929565, 2.29658269882202], 
    [-0.385968565940857, 6.45599317550659, 2.27285146713257], 
    [-0.393162041902542, 6.45960903167725, 2.30670642852783], 
    [-0.361075580120087, 6.45847034454346, 2.25449585914612], 
    [-0.399180710315704, 6.44589376449585, 2.33264803886414], 
    [-0.418517410755157, 6.43679141998291, 2.31012964248657], 
    [-0.40625873208046, 6.44360303878784, 2.28622961044312], 
    [-0.314096719026566, 6.4780707359314, 2.23670649528503], 
    [-0.297222197055817, 6.48454236984253, 2.26418590545654], 
    [-0.344499170780182, 6.47178506851196, 2.24730038642883], 
    [-0.3250652551651, 6.48091697692871, 2.26480627059937], 
    [-0.348373830318451, 6.48381853103638, 2.28123879432678], 
    [-0.319394052028656, 6.49054098129272, 2.29606080055237], 
    [-0.345251858234406, 6.4888744354248, 2.31023168563843], 
    [-0.295667350292206, 6.48823070526123, 2.32241368293762], 
    [-0.324510991573334, 6.48692464828491, 2.33266687393188], 
    [-0.290888667106628, 6.49041938781738, 2.29412722587585], 
    [-0.264627724885941, 6.4918999671936, 2.30728387832642], 
    [-0.272410243749619, 6.48700284957886, 2.28001093864441], 
    [-0.271489262580872, 6.48421239852905, 2.25815105438232], 
    [-0.244443938136101, 6.49145174026489, 2.2725715637207], 
    [-0.214897856116295, 6.50106191635132, 2.26946902275085], 
    [-0.233073219656944, 6.49696779251099, 2.29967021942139], 
    [-0.216576501727104, 6.49614095687866, 2.32362008094788], 
    [-0.245531752705574, 6.48571395874023, 2.32425260543823], 
    [-0.203451365232468, 6.50612354278564, 2.29671454429626], 
    [-0.186306104063988, 6.51222324371338, 2.27049422264099], 
    [-0.187671020627022, 6.50715351104736, 2.32205414772034], 
    [-0.173093393445015, 6.51497936248779, 2.29598212242126], 
    [-0.157672986388206, 6.51354694366455, 2.32021903991699], 
    [-0.157337784767151, 6.51899337768555, 2.27228808403015], 
    [-0.133173510432243, 6.51563358306885, 2.29507064819336], 
    [-0.131590873003006, 6.50149774551392, 2.33246088027954], 
    [-0.166283145546913, 6.49704599380493, 2.34184312820435], 
    [-0.190734475851059, 6.49127244949341, 2.3441047668457], 
    [-0.211422368884087, 6.48207187652588, 2.34442210197449], 
    [-0.234152510762215, 6.47868824005127, 2.34356451034546], 
    [-0.27178692817688, 6.47843742370605, 2.34055733680725], 
    [-0.301207542419434, 6.47158527374268, 2.34951043128967], 
    [-0.331342279911041, 6.46473026275635, 2.35411620140076], 
    [-0.361715823411942, 6.45789957046509, 2.35827159881592], 
    [-0.356036692857742, 6.48516321182251, 2.34068751335144], 
    [-0.385967195034027, 6.47399044036865, 2.33921360969543], 
    [-0.376736283302307, 6.48749303817749, 2.30658268928528], 
    [-0.395968556404114, 6.46599340438843, 2.28285145759583], 
    [-0.403162032365799, 6.46960926055908, 2.31670641899109], 
    [-0.371075570583344, 6.46847057342529, 2.26449584960938], 
    [-0.409180700778961, 6.45589399337769, 2.34264802932739], 
    [-0.428517401218414, 6.44679164886475, 2.32012963294983], 
    [-0.416258722543716, 6.45360326766968, 2.29622960090637]
] # synapse_vertex_list

synapse_wall_list = [
    [0, 1, 3], 
    [0, 3, 2], 
    [4, 2, 3], 
    [3, 5, 4], 
    [5, 3, 1], 
    [1, 9, 5], 
    [6, 4, 5], 
    [5, 8, 6], 
    [8, 5, 7], 
    [7, 5, 9], 
    [11, 10, 9], 
    [7, 9, 10], 
    [9, 1, 11], 
    [13, 11, 12], 
    [11, 1, 12], 
    [13, 10, 11], 
    [14, 15, 13], 
    [10, 13, 15], 
    [15, 17, 10], 
    [18, 16, 15], 
    [15, 16, 17], 
    [15, 14, 18], 
    [18, 14, 19], 
    [19, 21, 18], 
    [16, 18, 20], 
    [20, 18, 21], 
    [21, 22, 20], 
    [24, 22, 21], 
    [21, 23, 24], 
    [23, 21, 19], 
    [22, 24, 25], 
    [25, 26, 22], 
    [27, 20, 26], 
    [26, 20, 22], 
    [16, 27, 28], 
    [20, 27, 16], 
    [16, 28, 29], 
    [17, 29, 30], 
    [29, 17, 16], 
    [30, 10, 17], 
    [10, 30, 7], 
    [31, 7, 30], 
    [8, 31, 32], 
    [7, 31, 8], 
    [33, 34, 32], 
    [8, 32, 34], 
    [34, 33, 35], 
    [35, 36, 34], 
    [34, 6, 8], 
    [34, 36, 6], 
    [39, 36, 37], 
    [38, 37, 36], 
    [36, 35, 38], 
    [4, 6, 36], 
    [4, 36, 39], 
    [39, 2, 4], 
    [37, 38, 42], 
    [40, 38, 35], 
    [40, 41, 38], 
    [42, 38, 41], 
    [43, 46, 44], 
    [43, 45, 46], 
    [47, 46, 45], 
    [46, 47, 48], 
    [48, 44, 46], 
    [44, 48, 52], 
    [49, 48, 47], 
    [48, 49, 51], 
    [51, 50, 48], 
    [50, 52, 48], 
    [54, 52, 53], 
    [50, 53, 52], 
    [52, 54, 44], 
    [56, 55, 54], 
    [54, 55, 44], 
    [56, 54, 53], 
    [57, 56, 58], 
    [53, 58, 56], 
    [58, 53, 60], 
    [61, 58, 59], 
    [58, 60, 59], 
    [58, 61, 57], 
    [61, 62, 57], 
    [62, 61, 64], 
    [59, 63, 61], 
    [63, 64, 61], 
    [64, 63, 65], 
    [67, 64, 65], 
    [64, 67, 66], 
    [66, 62, 64], 
    [65, 68, 67], 
    [68, 65, 69], 
    [70, 69, 63], 
    [69, 65, 63], 
    [59, 71, 70], 
    [63, 59, 70], 
    [59, 72, 71], 
    [60, 73, 72], 
    [72, 59, 60], 
    [73, 60, 53], 
    [53, 50, 73], 
    [74, 73, 50], 
    [51, 75, 74], 
    [50, 51, 74], 
    [76, 75, 77], 
    [51, 77, 75], 
    [77, 78, 76], 
    [78, 77, 79], 
    [77, 51, 49], 
    [77, 49, 79], 
    [82, 80, 79], 
    [81, 79, 80], 
    [79, 81, 78], 
    [47, 79, 49], 
    [47, 82, 79], 
    [82, 47, 45], 
    [80, 85, 81], 
    [83, 78, 81], 
    [83, 81, 84], 
    [85, 84, 81], 
    [1, 0, 43], 
    [55, 12, 1], 
    [12, 55, 56], 
    [13, 56, 57], 
    [62, 19, 14], 
    [19, 62, 66], 
    [67, 24, 23], 
    [25, 24, 67], 
    [26, 25, 68], 
    [27, 26, 69], 
    [28, 27, 70], 
    [29, 28, 71], 
    [30, 29, 72], 
    [31, 30, 73], 
    [32, 31, 74], 
    [33, 32, 75], 
    [35, 33, 76], 
    [40, 35, 78], 
    [40, 83, 84], 
    [41, 84, 85], 
    [42, 85, 80], 
    [37, 80, 82], 
    [39, 82, 45], 
    [2, 45, 43], 
    [1, 43, 44], 
    [55, 1, 44], 
    [12, 56, 13], 
    [13, 57, 14], 
    [62, 14, 57], 
    [19, 66, 23], 
    [67, 23, 66], 
    [25, 67, 68], 
    [26, 68, 69], 
    [27, 69, 70], 
    [28, 70, 71], 
    [29, 71, 72], 
    [30, 72, 73], 
    [31, 73, 74], 
    [32, 74, 75], 
    [33, 75, 76], 
    [35, 76, 78], 
    [40, 78, 83], 
    [40, 84, 41], 
    [41, 85, 42], 
    [42, 80, 37], 
    [37, 82, 39], 
    [39, 45, 2], 
    [2, 43, 0]
] # synapse_wall_list

synapse = m.GeometryObject(
    name = 'synapse',
    vertex_list = synapse_vertex_list,
    wall_list = synapse_wall_list,
    surface_regions = []
)
# ^^^^ synapse ^^^^

