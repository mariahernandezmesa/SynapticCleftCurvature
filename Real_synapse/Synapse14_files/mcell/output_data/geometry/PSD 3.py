import mcell as m

# ---- PSD ----
PSD_vertex_list = [
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
    [-0.40625873208046, 6.44360303878784, 2.28622961044312]
] # PSD_vertex_list

PSD_wall_list = [
    [0, 3, 1], 
    [0, 2, 3], 
    [4, 3, 2], 
    [3, 4, 5], 
    [5, 1, 3], 
    [1, 5, 9], 
    [6, 5, 4], 
    [5, 6, 8], 
    [8, 7, 5], 
    [7, 9, 5], 
    [11, 9, 10], 
    [7, 10, 9], 
    [9, 11, 1], 
    [13, 12, 11], 
    [11, 12, 1], 
    [13, 11, 10], 
    [14, 13, 15], 
    [10, 15, 13], 
    [15, 10, 17], 
    [18, 15, 16], 
    [15, 17, 16], 
    [15, 18, 14], 
    [18, 19, 14], 
    [19, 18, 21], 
    [16, 20, 18], 
    [20, 21, 18], 
    [21, 20, 22], 
    [24, 21, 22], 
    [21, 24, 23], 
    [23, 19, 21], 
    [22, 25, 24], 
    [25, 22, 26], 
    [27, 26, 20], 
    [26, 22, 20], 
    [16, 28, 27], 
    [20, 16, 27], 
    [16, 29, 28], 
    [17, 30, 29], 
    [29, 16, 17], 
    [30, 17, 10], 
    [10, 7, 30], 
    [31, 30, 7], 
    [8, 32, 31], 
    [7, 8, 31], 
    [33, 32, 34], 
    [8, 34, 32], 
    [34, 35, 33], 
    [35, 34, 36], 
    [34, 8, 6], 
    [34, 6, 36], 
    [39, 37, 36], 
    [38, 36, 37], 
    [36, 38, 35], 
    [4, 36, 6], 
    [4, 39, 36], 
    [39, 4, 2], 
    [37, 42, 38], 
    [40, 35, 38], 
    [40, 38, 41], 
    [42, 41, 38]
] # PSD_wall_list

PSD = m.GeometryObject(
    name = 'PSD',
    vertex_list = PSD_vertex_list,
    wall_list = PSD_wall_list,
    surface_regions = []
)
# ^^^^ PSD ^^^^

