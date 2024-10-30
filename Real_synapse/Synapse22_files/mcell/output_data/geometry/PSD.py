import mcell as m

# ---- PSD ----
PSD_vertex_list = [
    [-1.70996856689453, -2.4498827457428, 0.327756285667419], 
    [-1.73811745643616, -2.44023776054382, 0.342068433761597], 
    [-1.70614767074585, -2.46477651596069, 0.348687738180161], 
    [-1.68187487125397, -2.4672577381134, 0.325297445058823], 
    [-1.68095421791077, -2.47986698150635, 0.351161181926727], 
    [-1.65471601486206, -2.48730373382568, 0.334258526563644], 
    [-1.65399241447449, -2.47418928146362, 0.309678226709366], 
    [-1.63058149814606, -2.47524452209473, 0.297970741987228], 
    [-1.62270951271057, -2.49043703079224, 0.319778859615326], 
    [-1.58329570293427, -2.48853778839111, 0.31478226184845], 
    [-1.60447061061859, -2.48139333724976, 0.296624302864075], 
    [-1.6284521818161, -2.49762034416199, 0.347579091787338], 
    [-1.59699940681458, -2.49766778945923, 0.33978858590126], 
    [-1.56002509593964, -2.49227380752563, 0.335581451654434], 
    [-1.60588037967682, -2.50288009643555, 0.36671569943428], 
    [-1.57742810249329, -2.49568748474121, 0.360789448022842], 
    [-1.5528199672699, -2.48519134521484, 0.360300004482269], 
    [-1.55933904647827, -2.48696208000183, 0.38183668255806], 
    [-1.5844988822937, -2.50124740600586, 0.38653376698494], 
    [-1.56367611885071, -2.49395203590393, 0.402881890535355], 
    [-1.58554518222809, -2.50904655456543, 0.411410719156265], 
    [-1.61315059661865, -2.50636863708496, 0.396115779876709], 
    [-1.64159417152405, -2.50314974784851, 0.396092921495438], 
    [-1.63391304016113, -2.50441884994507, 0.372997134923935], 
    [-1.6113646030426, -2.51261329650879, 0.422518789768219], 
    [-1.63807690143585, -2.50795197486877, 0.417280256748199], 
    [-1.66343343257904, -2.49774408340454, 0.410508811473846], 
    [-1.63865542411804, -2.51655340194702, 0.439545184373856], 
    [-1.66539001464844, -2.50683450698853, 0.434805601835251], 
    [-1.69278025627136, -2.50803256034851, 0.446135252714157], 
    [-1.66236460208893, -2.51929354667664, 0.462046980857849], 
    [-1.6914621591568, -2.49433612823486, 0.422167181968689], 
    [-1.71185457706451, -2.48005104064941, 0.407052665948868], 
    [-1.68557393550873, -2.48828816413879, 0.397830873727798], 
    [-1.72482895851135, -2.49160313606262, 0.430704474449158], 
    [-1.74809765815735, -2.46964955329895, 0.413505166769028], 
    [-1.74556958675385, -2.50399994850159, 0.44679719209671], 
    [-1.72023499011993, -2.51413536071777, 0.453980654478073], 
    [-1.76446187496185, -2.48560786247253, 0.435502529144287], 
    [-1.77556049823761, -2.51655578613281, 0.458662182092667], 
    [-1.79444086551666, -2.4862949848175, 0.444058924913406], 
    [-1.78681325912476, -2.46056652069092, 0.424158096313477], 
    [-1.77197313308716, -2.44773125648499, 0.396270573139191], 
    [-1.81132125854492, -2.4351978302002, 0.404607534408569], 
    [-1.82671844959259, -2.46141743659973, 0.436374962329865], 
    [-1.8214054107666, -2.49082779884338, 0.449561446905136], 
    [-1.84962856769562, -2.49156165122986, 0.453180879354477], 
    [-1.84333693981171, -2.4418044090271, 0.415161699056625], 
    [-1.86588144302368, -2.45266938209534, 0.425609946250916], 
    [-1.86807835102081, -2.47335362434387, 0.443622201681137], 
    [-1.89863228797913, -2.48132491111755, 0.446531355381012], 
    [-1.88943481445312, -2.46455311775208, 0.430568814277649], 
    [-1.89392602443695, -2.45941662788391, 0.407554268836975], 
    [-1.91763627529144, -2.47336721420288, 0.42092901468277], 
    [-1.9143340587616, -2.47099590301514, 0.393851310014725], 
    [-1.92427754402161, -2.48933172225952, 0.441801011562347], 
    [-1.93395435810089, -2.48900318145752, 0.399856269359589], 
    [-1.94914960861206, -2.49912476539612, 0.422078967094421], 
    [-1.92520892620087, -2.49499940872192, 0.376045018434525], 
    [-1.9040789604187, -2.47998762130737, 0.37154358625412], 
    [-1.89154422283173, -2.45952963829041, 0.383335083723068], 
    [-1.88407850265503, -2.47258520126343, 0.358378410339355], 
    [-1.8717395067215, -2.44543600082397, 0.372746378183365], 
    [-1.85098874568939, -2.4297616481781, 0.391552567481995], 
    [-1.87200164794922, -2.44339156150818, 0.401071757078171], 
    [-1.83373117446899, -2.42146897315979, 0.377426743507385], 
    [-1.81036674976349, -2.41926670074463, 0.370294600725174], 
    [-1.78960573673248, -2.43140935897827, 0.379673659801483], 
    [-1.7700023651123, -2.43516182899475, 0.360622942447662], 
    [-1.75000882148743, -2.44780349731445, 0.368481516838074], 
    [-1.745854139328, -2.45751357078552, 0.388853132724762], 
    [-1.7274729013443, -2.45889902114868, 0.36625549197197], 
    [-1.70463395118713, -2.47587013244629, 0.374742835760117], 
    [-1.72554647922516, -2.46681642532349, 0.389747262001038], 
    [-1.6798460483551, -2.48707008361816, 0.374108165502548], 
    [-1.6566869020462, -2.49398565292358, 0.360002726316452], 
    [-1.66144871711731, -2.49748396873474, 0.384939342737198], 
    [-1.8082058429718, -2.51225638389587, 0.458427548408508], 
    [-1.69855713844299, -2.524409532547, 0.46947717666626], 
    [-1.69851720333099, -2.54872298240662, 0.492175191640854], 
    [-1.6779510974884, -2.53356671333313, 0.482331156730652], 
    [-1.66960215568542, -2.5487208366394, 0.497814893722534], 
    [-1.65569543838501, -2.53915762901306, 0.485009133815765], 
    [-1.6409786939621, -2.55377960205078, 0.504766404628754], 
    [-1.63121378421783, -2.53904318809509, 0.47979399561882], 
    [-1.60073471069336, -2.53434324264526, 0.465844959020615], 
    [-1.61050724983215, -2.55088663101196, 0.492193669080734], 
    [-1.62964677810669, -2.52807545661926, 0.457481443881989], 
    [-1.61092031002045, -2.52329468727112, 0.444827169179916], 
    [-1.58189880847931, -2.51971960067749, 0.440295428037643], 
    [-1.56681442260742, -2.52899551391602, 0.468431085348129], 
    [-1.55271446704865, -2.51094150543213, 0.448038071393967], 
    [-1.56029200553894, -2.50436758995056, 0.424706310033798], 
    [-1.53409790992737, -2.49119830131531, 0.436554282903671], 
    [-1.54322373867035, -2.48702096939087, 0.415050625801086], 
    [-1.53738868236542, -2.47681045532227, 0.396454960107803], 
    [-1.5209059715271, -2.46815276145935, 0.417934477329254], 
    [-1.5155770778656, -2.4551420211792, 0.393656939268112], 
    [-1.51325380802155, -2.47470331192017, 0.448203861713409], 
    [-1.49800872802734, -2.43740105628967, 0.412306636571884], 
    [-1.50359451770782, -2.45606327056885, 0.434820026159286], 
    [-1.49281358718872, -2.45730352401733, 0.459830015897751], 
    [-1.48906946182251, -2.43982100486755, 0.440203338861465], 
    [-1.47782099246979, -2.41877436637878, 0.433548718690872], 
    [-1.47952234745026, -2.43155837059021, 0.461919665336609], 
    [-1.48217928409576, -2.4523606300354, 0.490564256906509], 
    [-1.46785032749176, -2.40461397171021, 0.456188589334488], 
    [-1.46621859073639, -2.41926741600037, 0.482903480529785], 
    [-1.45412111282349, -2.38830518722534, 0.474618881940842], 
    [-1.4656720161438, -2.42985367774963, 0.511288285255432], 
    [-1.47811055183411, -2.45565724372864, 0.527608215808868], 
    [-1.45574569702148, -2.42778062820435, 0.543463587760925], 
    [-1.46685230731964, -2.45399761199951, 0.560744285583496], 
    [-1.45430755615234, -2.46301531791687, 0.585283577442169], 
    [-1.4827002286911, -2.475266456604, 0.555052697658539], 
    [-1.47380673885345, -2.48628234863281, 0.580326557159424], 
    [-1.49854183197021, -2.50087881088257, 0.559977769851685], 
    [-1.45210564136505, -2.48307943344116, 0.605706453323364], 
    [-1.49290072917938, -2.51167225837708, 0.586808264255524], 
    [-1.47166204452515, -2.50342559814453, 0.604812681674957], 
    [-1.48838496208191, -2.52197766304016, 0.609903693199158], 
    [-1.50884389877319, -2.53580474853516, 0.600034654140472], 
    [-1.53345918655396, -2.5529637336731, 0.58571869134903], 
    [-1.51365005970001, -2.52709937095642, 0.57319712638855], 
    [-1.52390480041504, -2.55589199066162, 0.613832950592041], 
    [-1.54413998126984, -2.57504725456238, 0.603979110717773], 
    [-1.56795275211334, -2.59235429763794, 0.596048831939697], 
    [-1.55605804920197, -2.57420873641968, 0.581493973731995], 
    [-1.55663323402405, -2.56657290458679, 0.550925731658936], 
    [-1.57835745811462, -2.5869562625885, 0.572864353656769], 
    [-1.59230518341064, -2.60531949996948, 0.588717520236969], 
    [-1.60787069797516, -2.59819316864014, 0.564126968383789], 
    [-1.58937859535217, -2.58173131942749, 0.550273895263672], 
    [-1.58552229404449, -2.57128047943115, 0.527258813381195], 
    [-1.61399567127228, -2.58369421958923, 0.538629233837128], 
    [-1.61383318901062, -2.56573462486267, 0.516026020050049], 
    [-1.64144229888916, -2.5756893157959, 0.527243733406067], 
    [-1.64033782482147, -2.5974326133728, 0.550064980983734], 
    [-1.66584396362305, -2.58838224411011, 0.536805093288422], 
    [-1.63036966323853, -2.61306190490723, 0.569901347160339], 
    [-1.6148384809494, -2.61633539199829, 0.584566593170166], 
    [-1.67258596420288, -2.56771445274353, 0.516950190067291], 
    [-1.58636009693146, -2.55688953399658, 0.505414128303528], 
    [-1.56307888031006, -2.55407762527466, 0.521227657794952], 
    [-1.58535397052765, -2.54413843154907, 0.484179884195328], 
    [-1.56437814235687, -2.54177570343018, 0.496103376150131], 
    [-1.54224395751953, -2.52414155006409, 0.491195917129517], 
    [-1.54547834396362, -2.53659391403198, 0.510908961296082], 
    [-1.53914642333984, -2.54137945175171, 0.533902406692505], 
    [-1.52433431148529, -2.51619482040405, 0.514173150062561], 
    [-1.50764715671539, -2.50137567520142, 0.532597064971924], 
    [-1.52058219909668, -2.50089836120605, 0.487480074167252], 
    [-1.49930644035339, -2.4813551902771, 0.506920695304871], 
    [-1.51864969730377, -2.52227807044983, 0.5452761054039], 
    [-1.53242778778076, -2.54239130020142, 0.558580040931702], 
    [-1.50479686260223, -2.47702765464783, 0.476689577102661], 
    [-1.49343729019165, -2.4816689491272, 0.534966945648193], 
    [-1.52497363090515, -2.49477887153625, 0.461189240217209], 
    [-1.54031872749329, -2.51319003105164, 0.469981849193573], 
    [-1.45445001125336, -2.37799859046936, 0.450053751468658], 
    [-1.44055366516113, -2.3608238697052, 0.42820543050766], 
    [-1.4640097618103, -2.393878698349, 0.42965292930603], 
    [-1.43746972084045, -2.35670733451843, 0.463839918375015], 
    [-1.42710566520691, -2.32936978340149, 0.446082770824432], 
    [-1.42411732673645, -2.32855749130249, 0.470997780561447], 
    [-1.414222240448, -2.30309748649597, 0.462947607040405], 
    [-1.41412818431854, -2.29761505126953, 0.432285368442535], 
    [-1.42307186126709, -2.32744026184082, 0.417804956436157], 
    [-1.43025434017181, -2.34900617599487, 0.402605563402176], 
    [-1.41879951953888, -2.33024573326111, 0.390613526105881], 
    [-1.42808055877686, -2.35886907577515, 0.374946743249893], 
    [-1.44853591918945, -2.38321757316589, 0.376449912786484], 
    [-1.44040203094482, -2.36869668960571, 0.39719495177269], 
    [-1.45743787288666, -2.38741660118103, 0.404264479875565], 
    [-1.4786034822464, -2.4122941493988, 0.407399237155914], 
    [-1.46792268753052, -2.40288853645325, 0.384692370891571], 
    [-1.46130526065826, -2.40180039405823, 0.35550919175148], 
    [-1.49293303489685, -2.42845940589905, 0.379600673913956], 
    [-1.48113560676575, -2.42755699157715, 0.345627188682556], 
    [-1.49707555770874, -2.44699048995972, 0.352033883333206], 
    [-1.51366031169891, -2.45984387397766, 0.366463333368301], 
    [-1.53247976303101, -2.47599220275879, 0.350368678569794], 
    [-1.53571486473083, -2.47161269187927, 0.37445279955864], 
    [-1.51157855987549, -2.46710681915283, 0.338204324245453], 
    [-1.51831889152527, -2.46679639816284, 0.307332664728165], 
    [-1.49507129192352, -2.44912457466125, 0.326840043067932], 
    [-1.5336582660675, -2.47988247871399, 0.326532423496246], 
    [-1.55228292942047, -2.47984051704407, 0.307467192411423], 
    [-1.47679913043976, -2.42906904220581, 0.31930074095726], 
    [-1.46462297439575, -2.41256403923035, 0.333276450634003]
] # PSD_vertex_list

PSD_wall_list = [
    [0, 1, 2], 
    [2, 3, 0], 
    [4, 5, 3], 
    [3, 2, 4], 
    [5, 6, 3], 
    [7, 6, 8], 
    [5, 8, 6], 
    [8, 10, 7], 
    [9, 10, 8], 
    [9, 8, 12], 
    [8, 5, 11], 
    [8, 11, 12], 
    [12, 13, 9], 
    [13, 12, 15], 
    [12, 11, 14], 
    [15, 12, 14], 
    [15, 16, 13], 
    [18, 15, 14], 
    [16, 15, 17], 
    [15, 18, 17], 
    [19, 18, 20], 
    [17, 18, 19], 
    [21, 18, 14], 
    [18, 21, 20], 
    [23, 22, 21], 
    [25, 21, 22], 
    [21, 14, 23], 
    [21, 25, 24], 
    [22, 26, 25], 
    [28, 25, 26], 
    [27, 24, 25], 
    [25, 28, 27], 
    [26, 31, 28], 
    [29, 30, 28], 
    [28, 31, 29], 
    [27, 28, 30], 
    [34, 31, 32], 
    [31, 33, 32], 
    [26, 33, 31], 
    [29, 31, 34], 
    [34, 32, 35], 
    [35, 38, 34], 
    [34, 38, 36], 
    [36, 37, 34], 
    [37, 29, 34], 
    [35, 41, 38], 
    [38, 39, 36], 
    [39, 38, 40], 
    [40, 38, 41], 
    [41, 35, 42], 
    [41, 42, 43], 
    [44, 41, 43], 
    [41, 44, 40], 
    [43, 47, 44], 
    [46, 45, 44], 
    [40, 44, 45], 
    [46, 44, 49], 
    [47, 48, 44], 
    [49, 44, 48], 
    [49, 51, 50], 
    [48, 51, 49], 
    [50, 51, 53], 
    [51, 48, 52], 
    [53, 51, 52], 
    [53, 52, 54], 
    [54, 56, 53], 
    [53, 57, 55], 
    [55, 50, 53], 
    [56, 57, 53], 
    [54, 58, 56], 
    [54, 59, 58], 
    [54, 60, 59], 
    [60, 61, 59], 
    [62, 61, 60], 
    [63, 62, 64], 
    [64, 62, 60], 
    [52, 64, 60], 
    [63, 64, 47], 
    [48, 47, 64], 
    [64, 52, 48], 
    [47, 43, 63], 
    [63, 43, 65], 
    [43, 66, 65], 
    [67, 66, 43], 
    [42, 68, 67], 
    [43, 42, 67], 
    [69, 68, 42], 
    [70, 69, 42], 
    [69, 71, 1], 
    [71, 69, 70], 
    [72, 71, 73], 
    [72, 2, 71], 
    [71, 2, 1], 
    [70, 73, 71], 
    [73, 32, 72], 
    [35, 32, 73], 
    [35, 73, 70], 
    [4, 2, 72], 
    [4, 72, 74], 
    [72, 32, 33], 
    [74, 72, 33], 
    [76, 75, 74], 
    [74, 75, 4], 
    [33, 76, 74], 
    [76, 26, 22], 
    [26, 76, 33], 
    [23, 75, 76], 
    [76, 22, 23], 
    [23, 11, 75], 
    [75, 11, 5], 
    [4, 75, 5], 
    [42, 35, 70], 
    [52, 60, 54], 
    [45, 77, 40], 
    [77, 39, 40], 
    [78, 29, 37], 
    [78, 30, 29], 
    [30, 78, 80], 
    [79, 80, 78], 
    [30, 80, 82], 
    [80, 79, 81], 
    [81, 82, 80], 
    [82, 84, 30], 
    [83, 84, 82], 
    [83, 82, 81], 
    [84, 87, 30], 
    [84, 86, 85], 
    [85, 87, 84], 
    [83, 86, 84], 
    [88, 27, 87], 
    [87, 85, 88], 
    [87, 27, 30], 
    [88, 85, 89], 
    [89, 24, 88], 
    [88, 24, 27], 
    [89, 85, 90], 
    [89, 90, 91], 
    [91, 92, 89], 
    [89, 92, 20], 
    [89, 20, 24], 
    [19, 20, 92], 
    [92, 94, 19], 
    [93, 92, 91], 
    [94, 92, 93], 
    [94, 95, 19], 
    [94, 96, 95], 
    [96, 94, 93], 
    [96, 99, 97], 
    [97, 95, 96], 
    [93, 98, 96], 
    [96, 98, 100], 
    [99, 96, 100], 
    [101, 102, 100], 
    [100, 98, 101], 
    [100, 102, 99], 
    [102, 104, 103], 
    [103, 99, 102], 
    [101, 104, 102], 
    [107, 104, 105], 
    [105, 104, 101], 
    [103, 104, 106], 
    [106, 104, 107], 
    [105, 109, 107], 
    [108, 106, 107], 
    [109, 105, 110], 
    [109, 110, 111], 
    [111, 110, 112], 
    [112, 115, 113], 
    [112, 114, 115], 
    [112, 110, 114], 
    [118, 115, 116], 
    [115, 114, 116], 
    [117, 113, 115], 
    [117, 115, 119], 
    [119, 115, 118], 
    [119, 118, 120], 
    [118, 121, 120], 
    [121, 123, 122], 
    [121, 122, 124], 
    [121, 118, 123], 
    [124, 122, 125], 
    [127, 126, 125], 
    [125, 122, 127], 
    [122, 128, 127], 
    [127, 128, 129], 
    [127, 129, 126], 
    [130, 129, 131], 
    [130, 126, 129], 
    [128, 132, 129], 
    [129, 132, 131], 
    [132, 128, 133], 
    [133, 134, 132], 
    [134, 131, 132], 
    [134, 133, 135], 
    [135, 136, 134], 
    [136, 137, 134], 
    [131, 134, 137], 
    [137, 136, 138], 
    [131, 137, 139], 
    [140, 131, 139], 
    [131, 140, 130], 
    [136, 141, 138], 
    [83, 141, 136], 
    [83, 81, 141], 
    [141, 81, 79], 
    [136, 135, 83], 
    [86, 135, 142], 
    [135, 133, 142], 
    [135, 86, 83], 
    [142, 143, 145], 
    [133, 143, 142], 
    [142, 144, 86], 
    [142, 145, 144], 
    [147, 146, 145], 
    [90, 145, 146], 
    [145, 143, 147], 
    [90, 144, 145], 
    [148, 147, 143], 
    [149, 147, 148], 
    [147, 149, 146], 
    [150, 149, 153], 
    [149, 150, 152], 
    [151, 146, 149], 
    [149, 152, 151], 
    [149, 148, 153], 
    [116, 153, 123], 
    [153, 116, 150], 
    [153, 154, 123], 
    [154, 153, 148], 
    [148, 128, 154], 
    [154, 122, 123], 
    [122, 154, 128], 
    [110, 105, 152], 
    [152, 105, 155], 
    [152, 156, 110], 
    [151, 152, 155], 
    [152, 150, 156], 
    [114, 110, 156], 
    [156, 116, 114], 
    [116, 156, 150], 
    [101, 98, 155], 
    [155, 105, 101], 
    [155, 98, 157], 
    [157, 151, 155], 
    [157, 98, 93], 
    [91, 157, 93], 
    [158, 157, 91], 
    [158, 151, 157], 
    [146, 158, 90], 
    [91, 90, 158], 
    [151, 158, 146], 
    [128, 148, 143], 
    [90, 85, 144], 
    [85, 86, 144], 
    [128, 143, 133], 
    [116, 123, 118], 
    [159, 106, 108], 
    [160, 159, 162], 
    [159, 160, 161], 
    [106, 159, 161], 
    [162, 163, 160], 
    [163, 162, 164], 
    [164, 165, 163], 
    [166, 163, 165], 
    [166, 167, 163], 
    [163, 167, 160], 
    [167, 168, 160], 
    [167, 169, 168], 
    [170, 168, 169], 
    [172, 170, 171], 
    [172, 168, 170], 
    [160, 168, 172], 
    [172, 173, 160], 
    [171, 173, 172], 
    [161, 160, 173], 
    [174, 161, 173], 
    [175, 174, 173], 
    [173, 171, 175], 
    [175, 171, 176], 
    [177, 175, 176], 
    [174, 175, 177], 
    [176, 178, 177], 
    [177, 178, 179], 
    [180, 177, 179], 
    [177, 97, 99], 
    [97, 177, 180], 
    [99, 174, 177], 
    [181, 180, 183], 
    [180, 181, 182], 
    [183, 180, 179], 
    [180, 182, 97], 
    [179, 185, 183], 
    [186, 183, 184], 
    [183, 185, 184], 
    [181, 183, 186], 
    [186, 184, 187], 
    [186, 13, 181], 
    [187, 13, 186], 
    [9, 13, 187], 
    [179, 178, 185], 
    [178, 188, 185], 
    [188, 178, 189], 
    [176, 189, 178], 
    [182, 181, 16], 
    [17, 182, 16], 
    [182, 17, 95], 
    [95, 97, 182], 
    [13, 16, 181], 
    [99, 103, 174], 
    [174, 103, 161], 
    [106, 161, 103], 
    [95, 17, 19], 
    [23, 14, 11]
] # PSD_wall_list

PSD = m.GeometryObject(
    name = 'PSD',
    vertex_list = PSD_vertex_list,
    wall_list = PSD_wall_list,
    surface_regions = []
)
# ^^^^ PSD ^^^^

