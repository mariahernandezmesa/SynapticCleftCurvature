import mcell as m

# ---- synapse ----
synapse_vertex_list = [
    [0.0798557996749878, -0.091313362121582, 0.0726284384727478], 
    [0.0663174390792847, -0.0745792388916016, 0.053193986415863], 
    [0.0439454317092896, -0.0846128463745117, 0.0687740445137024], 
    [0.0939605236053467, -0.0764617919921875, 0.0458819270133972], 
    [0.105324745178223, -0.0556249618530273, 0.0243372917175293], 
    [0.0680270195007324, -0.0552730560302734, 0.0327793955802917], 
    [0.0415397882461548, -0.0664615631103516, 0.0468670129776001], 
    [0.0843967199325562, -0.0372829437255859, 0.0176510810852051], 
    [0.053188681602478, -0.0228796005249023, 0.0139822959899902], 
    [0.035696268081665, -0.0475330352783203, 0.029446542263031], 
    [0.0222766399383545, -0.0293235778808594, 0.0171394944190979], 
    [0.00330090522766113, -0.0453214645385742, 0.0239550471305847], 
    [0.0121556520462036, -0.0643711090087891, 0.0388334393501282], 
    [-0.0165419578552246, -0.064906120300293, 0.0303649306297302], 
    [0.0198785066604614, -0.0788993835449219, 0.0556312203407288], 
    [-0.00901412963867188, -0.083796501159668, 0.0507680177688599], 
    [-0.0384941101074219, -0.082942008972168, 0.0340644717216492], 
    [-0.0335015058517456, -0.0987014770507812, 0.0532411932945251], 
    [0.00893795490264893, -0.093414306640625, 0.072367787361145], 
    [-0.018762469291687, -0.101813316345215, 0.0740687251091003], 
    [-0.0486457347869873, -0.111686706542969, 0.0704339742660522], 
    [-0.0806924104690552, -0.115683555603027, 0.0604466199874878], 
    [-0.0586591958999634, -0.101576805114746, 0.0441258549690247], 
    [-0.0673583745956421, -0.116643905639648, 0.0899800062179565], 
    [-0.0913326740264893, -0.111405372619629, 0.0829117298126221], 
    [-0.111064791679382, -0.112055778503418, 0.0647075176239014], 
    [-0.110226273536682, -0.11407470703125, 0.0380021929740906], 
    [-0.135982871055603, -0.108620643615723, 0.0197812914848328], 
    [-0.102719187736511, -0.101413726806641, 0.0150061845779419], 
    [-0.0834581851959229, -0.105866432189941, 0.0345501303672791], 
    [-0.0680344104766846, -0.0853109359741211, 0.019327700138092], 
    [-0.0734864473342896, -0.0550775527954102, 0.0048375129699707], 
    [-0.0458824634552002, -0.0622034072875977, 0.0192686915397644], 
    [-0.093291163444519, -0.0784339904785156, 0.00351184606552124], 
    [-0.1202552318573, -0.0894651412963867, -0.00247281789779663], 
    [-0.109345436096191, -0.0589590072631836, -0.0107152462005615], 
    [-0.140770554542542, -0.0756196975708008, -0.0195786952972412], 
    [-0.111379384994507, -0.0275506973266602, -0.029282808303833], 
    [-0.0896428823471069, -0.0360746383666992, -0.0111100673675537], 
    [-0.130232810974121, -0.0506811141967773, -0.0289574265480042], 
    [-0.152054667472839, -0.058807373046875, -0.0412960052490234], 
    [-0.136392712593079, -0.0369110107421875, -0.0494412779808044], 
    [-0.122368574142456, -0.0128631591796875, -0.0531928539276123], 
    [-0.146698594093323, -0.0249195098876953, -0.071201503276825], 
    [-0.12968909740448, -0.00325202941894531, -0.0774310827255249], 
    [-0.110930442810059, 0.0243663787841797, -0.0832349061965942], 
    [-0.110303163528442, 0.00869655609130859, -0.0626735091209412], 
    [-0.0959873199462891, 0.00530910491943359, -0.0389118194580078], 
    [-0.0953363180160522, 0.030888557434082, -0.0586044192314148], 
    [-0.0944404602050781, 0.0530633926391602, -0.0871904492378235], 
    [-0.0695724487304688, 0.0343055725097656, -0.0367664098739624], 
    [-0.0799989700317383, 0.0522050857543945, -0.0604793429374695], 
    [-0.0645116567611694, 0.0752363204956055, -0.073525071144104], 
    [-0.0586475133895874, 0.0584135055541992, -0.0528048872947693], 
    [-0.0419260263442993, 0.0544977188110352, -0.038274347782135], 
    [-0.03510582447052, 0.0748319625854492, -0.0513043999671936], 
    [-0.0374665260314941, 0.0901947021484375, -0.0726718902587891], 
    [-0.00899362564086914, 0.0936527252197266, -0.0636724233627319], 
    [-0.0173555612564087, 0.0593338012695312, -0.0326974391937256], 
    [-0.00748240947723389, 0.0762815475463867, -0.0458961129188538], 
    [0.00941014289855957, 0.0643749237060547, -0.0353413820266724], 
    [0.0163015127182007, 0.0852460861206055, -0.0491431951522827], 
    [0.0249398946762085, 0.101283073425293, -0.06852787733078], 
    [0.0442755222320557, 0.0891141891479492, -0.055439829826355], 
    [0.036810040473938, 0.0704240798950195, -0.0400749444961548], 
    [0.0557008981704712, 0.0530910491943359, -0.0267497897148132], 
    [0.0283387899398804, 0.0532026290893555, -0.0261796116828918], 
    [0.0633692741394043, 0.0717639923095703, -0.0458140969276428], 
    [0.0832864046096802, 0.0542020797729492, -0.0371733903884888], 
    [0.0685125589370728, 0.0868148803710938, -0.0660813450813293], 
    [0.089823842048645, 0.0745725631713867, -0.0583488345146179], 
    [0.0892471075057983, 0.0937814712524414, -0.0881751775741577], 
    [0.112784266471863, 0.0737705230712891, -0.074078381061554], 
    [0.11094856262207, 0.0562400817871094, -0.0524854063987732], 
    [0.135091662406921, 0.0551748275756836, -0.0709646940231323], 
    [0.106219530105591, 0.0372381210327148, -0.0335719585418701], 
    [0.132861137390137, 0.0372219085693359, -0.0474533438682556], 
    [0.129966974258423, 0.0186805725097656, -0.0273069739341736], 
    [0.122492074966431, -0.00181674957275391, -0.0100635886192322], 
    [0.105498671531677, 0.0168304443359375, -0.0187240839004517], 
    [0.0742839574813843, 0.0287742614746094, -0.0155057311058044], 
    [0.0948494672775269, -0.0007171630859375, -0.00578707456588745], 
    [0.111125588417053, -0.0271520614624023, 0.00684958696365356], 
    [0.0825424194335938, -0.0172576904296875, 0.00630015134811401], 
    [0.0689047574996948, 0.000957489013671875, -6.90221786499023e-05], 
    [0.0431032180786133, 0.00840568542480469, -0.00183296203613281], 
    [0.0197551250457764, -0.00677013397216797, 0.00616508722305298], 
    [0.0123875141143799, 0.0168561935424805, -0.00601363182067871], 
    [0.0371767282485962, 0.0332794189453125, -0.0138124823570251], 
    [0.00218117237091064, 0.0419712066650391, -0.0185889005661011], 
    [-0.0300604104995728, 0.0392007827758789, -0.0231952667236328], 
    [-0.0181834697723389, 0.0202217102050781, -0.0112190246582031], 
    [-0.0101416110992432, -0.00126552581787109, 0.00170046091079712], 
    [-0.0408221483230591, 0.000794410705566406, -0.00591897964477539], 
    [-0.0467077493667603, 0.0199155807495117, -0.0195907950401306], 
    [-0.0693608522415161, 0.00651168823242188, -0.0190263986587524], 
    [-0.0640749931335449, -0.0203065872192383, -0.00410044193267822], 
    [-0.0873692035675049, -0.0127964019775391, -0.0190778374671936], 
    [-0.0314018726348877, -0.0200395584106445, 0.00647145509719849], 
    [-0.0489648580551147, -0.0392131805419922, 0.0097852349281311], 
    [-0.0237580537796021, -0.0422658920288086, 0.0176134705543518], 
    [-0.00368297100067139, -0.0236034393310547, 0.0128089785575867], 
    [0.133772373199463, 0.0797758102416992, -0.100559830665588], 
    [0.053802490234375, 0.102910041809082, -0.0811752080917358], 
    [0.0898557901382446, -0.0813131332397461, 0.0826284289360046], 
    [0.0763174295425415, -0.0645790100097656, 0.0631939768791199], 
    [0.0539454221725464, -0.0746126174926758, 0.0787740349769592], 
    [0.103960514068604, -0.0664615631103516, 0.0558819174766541], 
    [0.115324735641479, -0.0456247329711914, 0.0343372821807861], 
    [0.0780270099639893, -0.0452728271484375, 0.0427793860435486], 
    [0.0515397787094116, -0.0564613342285156, 0.0568670034408569], 
    [0.094396710395813, -0.02728271484375, 0.0276510715484619], 
    [0.0631886720657349, -0.0128793716430664, 0.0239822864532471], 
    [0.0456962585449219, -0.0375328063964844, 0.0394465327262878], 
    [0.0322766304016113, -0.0193233489990234, 0.0271394848823547], 
    [0.013300895690918, -0.0353212356567383, 0.0339550375938416], 
    [0.0221556425094604, -0.0543708801269531, 0.048833429813385], 
    [-0.00654196739196777, -0.054905891418457, 0.0403649210929871], 
    [0.0298784971237183, -0.0688991546630859, 0.0656312108039856], 
    [0.000985860824584961, -0.073796272277832, 0.0607680082321167], 
    [-0.028494119644165, -0.072941780090332, 0.044064462184906], 
    [-0.0235015153884888, -0.0887012481689453, 0.063241183757782], 
    [0.0189379453659058, -0.0834140777587891, 0.0823677778244019], 
    [-0.00876247882843018, -0.0918130874633789, 0.0840687155723572], 
    [-0.0386457443237305, -0.101686477661133, 0.0804339647293091], 
    [-0.0706924200057983, -0.105683326721191, 0.0704466104507446], 
    [-0.0486592054367065, -0.0915765762329102, 0.0541258454322815], 
    [-0.0573583841323853, -0.106643676757812, 0.0999799966812134], 
    [-0.0813326835632324, -0.101405143737793, 0.0929117202758789], 
    [-0.101064801216125, -0.102055549621582, 0.0747075080871582], 
    [-0.100226283073425, -0.104074478149414, 0.0480021834373474], 
    [-0.125982880592346, -0.0986204147338867, 0.0297812819480896], 
    [-0.0927191972732544, -0.0914134979248047, 0.0250061750411987], 
    [-0.073458194732666, -0.0958662033081055, 0.0445501208305359], 
    [-0.0580344200134277, -0.0753107070922852, 0.0293276906013489], 
    [-0.0634864568710327, -0.0450773239135742, 0.0148375034332275], 
    [-0.0358824729919434, -0.0522031784057617, 0.0292686820030212], 
    [-0.0832911729812622, -0.0684337615966797, 0.0135118365287781], 
    [-0.110255241394043, -0.0794649124145508, 0.00752717256546021], 
    [-0.0993454456329346, -0.0489587783813477, -0.000715255737304688], 
    [-0.130770564079285, -0.0656194686889648, -0.00957870483398438], 
    [-0.10137939453125, -0.0175504684448242, -0.0192828178405762], 
    [-0.0796428918838501, -0.0260744094848633, -0.00111007690429688], 
    [-0.120232820510864, -0.0406808853149414, -0.0189574360847473], 
    [-0.142054677009583, -0.0488071441650391, -0.0312960147857666], 
    [-0.126392722129822, -0.0269107818603516, -0.0394412875175476], 
    [-0.112368583679199, -0.00286293029785156, -0.0431928634643555], 
    [-0.136698603630066, -0.0149192810058594, -0.0612015128135681], 
    [-0.119689106941223, 0.00674819946289062, -0.0674310922622681], 
    [-0.100930452346802, 0.0343666076660156, -0.0732349157333374], 
    [-0.100303173065186, 0.0186967849731445, -0.0526735186576843], 
    [-0.0859873294830322, 0.0153093338012695, -0.028911828994751], 
    [-0.0853363275527954, 0.040888786315918, -0.048604428768158], 
    [-0.0844404697418213, 0.0630636215209961, -0.0771904587745667], 
    [-0.0595724582672119, 0.0443058013916016, -0.0267664194107056], 
    [-0.0699989795684814, 0.0622053146362305, -0.0504793524742126], 
    [-0.0545116662979126, 0.0852365493774414, -0.0635250806808472], 
    [-0.0486475229263306, 0.0684137344360352, -0.0428048968315125], 
    [-0.0319260358810425, 0.0644979476928711, -0.0282743573188782], 
    [-0.0251058340072632, 0.0848321914672852, -0.0413044095039368], 
    [-0.0274665355682373, 0.100194931030273, -0.0626718997955322], 
    [0.0010063648223877, 0.103652954101562, -0.0536724328994751], 
    [-0.00735557079315186, 0.0693340301513672, -0.0226974487304688], 
    [0.00251758098602295, 0.0862817764282227, -0.0358961224555969], 
    [0.0194101333618164, 0.0743751525878906, -0.0253413915634155], 
    [0.0263015031814575, 0.0952463150024414, -0.0391432046890259], 
    [0.0349398851394653, 0.111283302307129, -0.0585278868675232], 
    [0.0542755126953125, 0.0991144180297852, -0.0454398393630981], 
    [0.0468100309371948, 0.0804243087768555, -0.0300749540328979], 
    [0.065700888633728, 0.0630912780761719, -0.0167497992515564], 
    [0.0383387804031372, 0.0632028579711914, -0.016179621219635], 
    [0.0733692646026611, 0.0817642211914062, -0.035814106464386], 
    [0.093286395072937, 0.0642023086547852, -0.0271733999252319], 
    [0.0785125494003296, 0.0968151092529297, -0.0560813546180725], 
    [0.0998238325119019, 0.0845727920532227, -0.0483488440513611], 
    [0.0992470979690552, 0.103781700134277, -0.0781751871109009], 
    [0.12278425693512, 0.083770751953125, -0.0640783905982971], 
    [0.120948553085327, 0.0662403106689453, -0.0424854159355164], 
    [0.145091652870178, 0.0651750564575195, -0.0609647035598755], 
    [0.116219520568848, 0.0472383499145508, -0.0235719680786133], 
    [0.142861127853394, 0.0472221374511719, -0.0374533534049988], 
    [0.13996696472168, 0.0286808013916016, -0.0173069834709167], 
    [0.132492065429688, 0.00818347930908203, -6.35981559753418e-05], 
    [0.115498661994934, 0.0268306732177734, -0.00872409343719482], 
    [0.0842839479446411, 0.0387744903564453, -0.00550574064254761], 
    [0.104849457740784, 0.00928306579589844, 0.00421291589736938], 
    [0.12112557888031, -0.0171518325805664, 0.0168495774269104], 
    [0.0925424098968506, -0.00725746154785156, 0.0163001418113708], 
    [0.0789047479629517, 0.0109577178955078, 0.00993096828460693], 
    [0.0531032085418701, 0.0184059143066406, 0.00816702842712402], 
    [0.0297551155090332, 0.00323009490966797, 0.0161650776863098], 
    [0.0223875045776367, 0.0268564224243164, 0.00398635864257812], 
    [0.047176718711853, 0.0432796478271484, -0.00381249189376831], 
    [0.0121811628341675, 0.051971435546875, -0.00858891010284424], 
    [-0.0200604200363159, 0.0492010116577148, -0.013195276260376], 
    [-0.00818347930908203, 0.0302219390869141, -0.00121903419494629], 
    [-0.000141620635986328, 0.00873470306396484, 0.011700451374054], 
    [-0.0308221578598022, 0.0107946395874023, 0.00408101081848145], 
    [-0.0367077589035034, 0.0299158096313477, -0.00959080457687378], 
    [-0.0593608617782593, 0.0165119171142578, -0.00902640819549561], 
    [-0.0540750026702881, -0.0103063583374023, 0.00589954853057861], 
    [-0.077369213104248, -0.00279617309570312, -0.00907784700393677], 
    [-0.0214018821716309, -0.0100393295288086, 0.0164714455604553], 
    [-0.0389648675918579, -0.0292129516601562, 0.0197852253913879], 
    [-0.0137580633163452, -0.0322656631469727, 0.0276134610176086], 
    [0.00631701946258545, -0.0136032104492188, 0.0228089690208435], 
    [0.14377236366272, 0.0897760391235352, -0.0905598402023315], 
    [0.0638024806976318, 0.112910270690918, -0.071175217628479]
] # synapse_vertex_list

synapse_wall_list = [
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
    [6, 1, 2], 
    [104, 107, 105], 
    [104, 105, 106], 
    [105, 107, 109], 
    [107, 108, 109], 
    [110, 105, 109], 
    [113, 110, 109], 
    [109, 111, 112], 
    [111, 109, 108], 
    [109, 112, 113], 
    [110, 113, 116], 
    [114, 115, 113], 
    [113, 112, 114], 
    [116, 113, 115], 
    [118, 110, 116], 
    [117, 119, 116], 
    [115, 117, 116], 
    [118, 116, 119], 
    [119, 117, 120], 
    [119, 120, 121], 
    [119, 122, 118], 
    [121, 123, 119], 
    [122, 119, 123], 
    [123, 121, 124], 
    [126, 124, 121], 
    [124, 126, 125], 
    [127, 124, 125], 
    [125, 128, 127], 
    [128, 125, 129], 
    [129, 125, 130], 
    [130, 132, 131], 
    [125, 133, 130], 
    [130, 133, 132], 
    [132, 133, 134], 
    [134, 133, 126], 
    [133, 125, 126], 
    [126, 120, 134], 
    [135, 134, 136], 
    [134, 135, 137], 
    [134, 120, 136], 
    [134, 137, 132], 
    [137, 139, 138], 
    [138, 132, 137], 
    [137, 135, 139], 
    [139, 140, 138], 
    [139, 143, 140], 
    [135, 142, 139], 
    [139, 142, 141], 
    [143, 139, 141], 
    [140, 143, 144], 
    [145, 143, 141], 
    [143, 145, 144], 
    [145, 146, 147], 
    [141, 146, 145], 
    [147, 146, 148], 
    [150, 149, 148], 
    [146, 150, 148], 
    [152, 149, 150], 
    [146, 151, 150], 
    [150, 151, 152], 
    [152, 153, 149], 
    [153, 152, 155], 
    [152, 154, 155], 
    [151, 154, 152], 
    [153, 155, 156], 
    [154, 157, 155], 
    [157, 156, 155], 
    [158, 157, 154], 
    [157, 158, 159], 
    [156, 157, 159], 
    [160, 159, 161], 
    [159, 160, 156], 
    [158, 162, 159], 
    [161, 159, 163], 
    [162, 163, 159], 
    [164, 165, 163], 
    [163, 162, 164], 
    [163, 165, 161], 
    [166, 161, 165], 
    [165, 167, 166], 
    [168, 167, 165], 
    [165, 164, 168], 
    [167, 168, 171], 
    [168, 169, 171], 
    [169, 168, 170], 
    [164, 170, 168], 
    [167, 171, 173], 
    [169, 172, 171], 
    [172, 174, 171], 
    [171, 174, 173], 
    [175, 173, 174], 
    [175, 174, 176], 
    [177, 176, 174], 
    [174, 172, 177], 
    [177, 178, 176], 
    [178, 177, 180], 
    [177, 179, 180], 
    [172, 179, 177], 
    [179, 181, 180], 
    [179, 183, 181], 
    [182, 181, 183], 
    [183, 179, 184], 
    [184, 185, 183], 
    [183, 185, 182], 
    [185, 186, 182], 
    [187, 186, 185], 
    [184, 188, 185], 
    [187, 185, 188], 
    [188, 184, 189], 
    [112, 188, 189], 
    [112, 187, 188], 
    [190, 112, 189], 
    [189, 184, 192], 
    [190, 189, 191], 
    [192, 191, 189], 
    [192, 169, 170], 
    [169, 192, 184], 
    [170, 193, 192], 
    [191, 192, 193], 
    [193, 170, 164], 
    [191, 193, 195], 
    [195, 193, 194], 
    [162, 194, 193], 
    [193, 164, 162], 
    [195, 197, 196], 
    [195, 196, 191], 
    [197, 195, 198], 
    [194, 198, 195], 
    [198, 154, 199], 
    [154, 198, 194], 
    [199, 197, 198], 
    [200, 197, 199], 
    [201, 200, 199], 
    [199, 154, 151], 
    [151, 201, 199], 
    [142, 200, 201], 
    [141, 142, 201], 
    [201, 151, 141], 
    [200, 142, 135], 
    [203, 200, 135], 
    [203, 202, 200], 
    [202, 197, 200], 
    [135, 136, 203], 
    [202, 203, 204], 
    [136, 204, 203], 
    [117, 204, 136], 
    [204, 117, 115], 
    [204, 205, 202], 
    [115, 205, 204], 
    [114, 190, 205], 
    [115, 114, 205], 
    [205, 196, 202], 
    [196, 205, 190], 
    [197, 202, 196], 
    [191, 196, 190], 
    [158, 194, 162], 
    [194, 158, 154], 
    [112, 190, 114], 
    [186, 187, 111], 
    [111, 187, 112], 
    [108, 186, 111], 
    [172, 169, 184], 
    [179, 172, 184], 
    [176, 178, 206], 
    [176, 206, 175], 
    [173, 175, 207], 
    [167, 173, 207], 
    [166, 167, 207], 
    [146, 141, 151], 
    [131, 132, 138], 
    [120, 117, 136], 
    [126, 121, 120], 
    [106, 118, 122], 
    [106, 110, 118], 
    [110, 106, 105], 
    [175, 102, 71], 
    [207, 71, 103], 
    [166, 103, 62], 
    [161, 62, 57], 
    [57, 160, 161], 
    [156, 56, 52], 
    [52, 153, 156], 
    [149, 49, 45], 
    [148, 45, 44], 
    [147, 44, 43], 
    [41, 147, 43], 
    [144, 41, 40], 
    [36, 144, 40], 
    [34, 140, 36], 
    [34, 131, 138], 
    [26, 131, 27], 
    [25, 130, 26], 
    [24, 129, 25], 
    [23, 128, 24], 
    [20, 127, 23], 
    [19, 124, 20], 
    [18, 123, 19], 
    [2, 122, 18], 
    [0, 106, 2], 
    [3, 104, 0], 
    [4, 107, 3], 
    [82, 108, 4], 
    [78, 186, 82], 
    [77, 182, 78], 
    [76, 181, 77], 
    [76, 178, 180], 
    [206, 74, 102], 
    [175, 206, 102], 
    [207, 175, 71], 
    [166, 207, 103], 
    [161, 166, 62], 
    [57, 56, 160], 
    [156, 160, 56], 
    [52, 49, 153], 
    [149, 153, 49], 
    [148, 149, 45], 
    [147, 148, 44], 
    [41, 145, 147], 
    [144, 145, 41], 
    [36, 140, 144], 
    [34, 138, 140], 
    [34, 27, 131], 
    [26, 130, 131], 
    [25, 129, 130], 
    [24, 128, 129], 
    [23, 127, 128], 
    [20, 124, 127], 
    [19, 123, 124], 
    [18, 122, 123], 
    [2, 106, 122], 
    [0, 104, 106], 
    [3, 107, 104], 
    [4, 108, 107], 
    [82, 186, 108], 
    [78, 182, 186], 
    [77, 181, 182], 
    [76, 180, 181], 
    [76, 74, 178], 
    [206, 178, 74]
] # synapse_wall_list

synapse = m.GeometryObject(
    name = 'synapse',
    vertex_list = synapse_vertex_list,
    wall_list = synapse_wall_list,
    surface_regions = []
)
# ^^^^ synapse ^^^^

