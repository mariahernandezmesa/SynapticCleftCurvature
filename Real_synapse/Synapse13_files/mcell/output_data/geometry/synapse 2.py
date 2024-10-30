import mcell as m

# ---- synapse ----
synapse_vertex_list = [
    [-1.61300885677338, -2.22427225112915, 0.0782623589038849], 
    [-1.61893582344055, -2.25367116928101, 0.0829066038131714], 
    [-1.58377861976624, -2.23108196258545, 0.0718718469142914], 
    [-1.62445783615112, -2.19700241088867, 0.0814026594161987], 
    [-1.64465045928955, -2.23615789413452, 0.0919828414916992], 
    [-1.66335475444794, -2.26074528694153, 0.116356909275055], 
    [-1.65212523937225, -2.20179724693298, 0.0951738655567169], 
    [-1.67166113853455, -2.23054695129395, 0.11429888010025], 
    [-1.6387106180191, -2.27201390266418, 0.0988790690898895], 
    [-1.62774276733398, -2.30268597602844, 0.106924086809158], 
    [-1.65022528171539, -2.29039525985718, 0.123029738664627], 
    [-1.61235761642456, -2.28458452224731, 0.0884214639663696], 
    [-1.59357094764709, -2.2648332118988, 0.0775115787982941], 
    [-1.58328080177307, -2.2916841506958, 0.0798254907131195], 
    [-1.60025215148926, -2.31288576126099, 0.0953958332538605], 
    [-1.56531572341919, -2.32326340675354, 0.0907212793827057], 
    [-1.58942139148712, -2.33575916290283, 0.108849436044693], 
    [-1.61515486240387, -2.32945489883423, 0.117029219865799], 
    [-1.59929060935974, -2.3557436466217, 0.125399798154831], 
    [-1.63860356807709, -2.31886434555054, 0.130506336688995], 
    [-1.56878447532654, -2.35392069816589, 0.11553880572319], 
    [-1.57710385322571, -2.37534070014954, 0.134533405303955], 
    [-1.54743337631226, -2.37226796150208, 0.129751056432724], 
    [-1.527623295784, -2.38741827011108, 0.144106090068817], 
    [-1.5389791727066, -2.35088753700256, 0.11088889837265], 
    [-1.51734006404877, -2.36594223976135, 0.126108378171921], 
    [-1.50813591480255, -2.3436803817749, 0.107617348432541], 
    [-1.49984300136566, -2.38176012039185, 0.141346961259842], 
    [-1.48288488388062, -2.35913968086243, 0.12580195069313], 
    [-1.45751595497131, -2.35847783088684, 0.147532045841217], 
    [-1.4571385383606, -2.33596968650818, 0.123984038829803], 
    [-1.48000514507294, -2.33256196975708, 0.10350289940834], 
    [-1.47496473789215, -2.37984585762024, 0.151893347501755], 
    [-1.47416043281555, -2.40195751190186, 0.175914704799652], 
    [-1.45587623119354, -2.37865090370178, 0.173270285129547], 
    [-1.48903834819794, -2.39798903465271, 0.158372491598129], 
    [-1.49332451820374, -2.42322206497192, 0.167048811912537], 
    [-1.46837484836578, -2.42250728607178, 0.187153100967407], 
    [-1.45861208438873, -2.39887380599976, 0.19448322057724], 
    [-1.46555829048157, -2.42538642883301, 0.213142842054367], 
    [-1.44768261909485, -2.39392805099487, 0.218132078647614], 
    [-1.43862330913544, -2.37216377258301, 0.196500867605209], 
    [-1.41859102249146, -2.34695744514465, 0.190637946128845], 
    [-1.43654000759125, -2.35560464859009, 0.169622391462326], 
    [-1.42250752449036, -2.361576795578, 0.223627954721451], 
    [-1.40076553821564, -2.33424973487854, 0.238113462924957], 
    [-1.44167423248291, -2.38618183135986, 0.241009593009949], 
    [-1.41295385360718, -2.3538339138031, 0.252814203500748], 
    [-1.4287885427475, -2.37151598930359, 0.254078805446625], 
    [-1.40344262123108, -2.33502173423767, 0.210908383131027], 
    [-1.39740240573883, -2.31861209869385, 0.184996157884598], 
    [-1.38515162467957, -2.31130266189575, 0.217839688062668], 
    [-1.37779426574707, -2.28866386413574, 0.180209457874298], 
    [-1.37147331237793, -2.28519034385681, 0.241104871034622], 
    [-1.38986098766327, -2.31033158302307, 0.252506911754608], 
    [-1.36997413635254, -2.28532195091248, 0.210931777954102], 
    [-1.36199331283569, -2.26631283760071, 0.22261318564415], 
    [-1.35853958129883, -2.26421189308167, 0.19571241736412], 
    [-1.3456050157547, -2.23688077926636, 0.187981814146042], 
    [-1.35271060466766, -2.24370193481445, 0.216811746358871], 
    [-1.3615630865097, -2.2564685344696, 0.166007995605469], 
    [-1.3725038766861, -2.24021530151367, 0.138039916753769], 
    [-1.35300183296204, -2.22410821914673, 0.159443885087967], 
    [-1.38444375991821, -2.27209615707397, 0.146136999130249], 
    [-1.39647650718689, -2.25125122070312, 0.118275791406631], 
    [-1.41129434108734, -2.28110504150391, 0.124884307384491], 
    [-1.40099883079529, -2.30121541023254, 0.153620004653931], 
    [-1.42892849445343, -2.31181240081787, 0.128807932138443], 
    [-1.41698563098907, -2.32918238639832, 0.162197232246399], 
    [-1.43827080726624, -2.33873605728149, 0.145648032426834], 
    [-1.45530271530151, -2.31058168411255, 0.10278046131134], 
    [-1.43545174598694, -2.28514790534973, 0.097967654466629], 
    [-1.44769191741943, -2.25633120536804, 0.0783723890781403], 
    [-1.41940593719482, -2.25880408287048, 0.0955623984336853], 
    [-1.46982538700104, -2.27758574485779, 0.0759457349777222], 
    [-1.49680995941162, -2.28913736343384, 0.0749667286872864], 
    [-1.47851920127869, -2.23232507705688, 0.0634488761425018], 
    [-1.50411784648895, -2.25785207748413, 0.065270870923996], 
    [-1.48031377792358, -2.30825114250183, 0.0858411490917206], 
    [-1.50679409503937, -2.31781959533691, 0.0856863260269165], 
    [-1.53077864646912, -2.32889175415039, 0.0958899855613708], 
    [-1.52403032779694, -2.28382253646851, 0.069132536649704], 
    [-1.53669786453247, -2.30765986442566, 0.0823972523212433], 
    [-1.55386638641357, -2.28600239753723, 0.0732675790786743], 
    [-1.56722772121429, -2.25792050361633, 0.0693640112876892], 
    [-1.46473848819733, -2.19413661956787, 0.0701087415218353], 
    [-1.44246387481689, -2.22564029693604, 0.0742595493793488], 
    [-1.41285407543182, -2.22798681259155, 0.0931830704212189], 
    [-1.43403112888336, -2.19738817214966, 0.0791599154472351], 
    [-1.46184825897217, -2.15779399871826, 0.0760935842990875], 
    [-1.40831208229065, -2.19908428192139, 0.0940255522727966], 
    [-1.42674160003662, -2.16836667060852, 0.0854901075363159], 
    [-1.4523024559021, -2.11428189277649, 0.0849795937538147], 
    [-1.4048125743866, -2.14718818664551, 0.0979275405406952], 
    [-1.38839340209961, -2.17997598648071, 0.107862532138824], 
    [-1.36764121055603, -2.20752120018005, 0.133752316236496], 
    [-1.36686205863953, -2.17759561538696, 0.133038014173508], 
    [-1.38944029808044, -2.21857833862305, 0.112999856472015], 
    [-1.37575602531433, -2.15022039413452, 0.118819355964661], 
    [-1.3555428981781, -2.12436056137085, 0.132879704236984], 
    [-1.35094523429871, -2.15825033187866, 0.14581686258316], 
    [-1.39980554580688, -2.11742424964905, 0.105508327484131], 
    [-1.41895866394043, -2.08207511901855, 0.0987452268600464], 
    [-1.37717235088348, -2.0950403213501, 0.112602949142456], 
    [-1.3853565454483, -2.05952024459839, 0.106677889823914], 
    [-1.36129117012024, -2.07671761512756, 0.12435308098793], 
    [-1.34751331806183, -2.09427189826965, 0.139212876558304], 
    [-1.33860182762146, -2.06760573387146, 0.138941913843155], 
    [-1.32722747325897, -2.07746934890747, 0.158994883298874], 
    [-1.33288908004761, -2.10681462287903, 0.162668108940125], 
    [-1.33996737003326, -2.13812184333801, 0.167024284601212], 
    [-1.34090149402618, -2.1701295375824, 0.181266367435455], 
    [-1.3438868522644, -2.20490169525146, 0.184639066457748], 
    [-1.35221230983734, -2.19063758850098, 0.157071620225906], 
    [-1.34643971920013, -2.21782350540161, 0.211134493350983], 
    [-1.3552610874176, -2.22579741477966, 0.238962709903717], 
    [-1.36263239383698, -2.25190138816833, 0.242980301380157], 
    [-1.35553741455078, -2.05662775039673, 0.126845002174377], 
    [-1.40377998352051, -2.33371758460999, 0.269466072320938], 
    [-1.38118457794189, -2.28813815116882, 0.267731577157974], 
    [-1.4440712928772, -2.38996148109436, 0.265906691551208], 
    [-1.45814120769501, -2.41237759590149, 0.24156379699707], 
    [-1.62214779853821, -2.16592216491699, 0.084325760602951], 
    [-1.66249358654022, -2.16984534263611, 0.10074108839035], 
    [-1.66904091835022, -2.13872194290161, 0.101725965738297], 
    [-1.6383730173111, -2.13995814323425, 0.0926744937896729], 
    [-1.62300884723663, -2.21427226066589, 0.0882623568177223], 
    [-1.62893581390381, -2.24367117881775, 0.0929066017270088], 
    [-1.59377861022949, -2.22108197212219, 0.0818718448281288], 
    [-1.63445782661438, -2.18700242042542, 0.0914026573300362], 
    [-1.65465044975281, -2.22615790367126, 0.101982839405537], 
    [-1.67335474491119, -2.25074529647827, 0.126356914639473], 
    [-1.66212522983551, -2.19179725646973, 0.105173863470554], 
    [-1.6816611289978, -2.22054696083069, 0.124298878014088], 
    [-1.64871060848236, -2.26201391220093, 0.108879067003727], 
    [-1.63774275779724, -2.29268598556519, 0.116924084722996], 
    [-1.66022527217865, -2.28039526939392, 0.133029744029045], 
    [-1.62235760688782, -2.27458453178406, 0.0984214618802071], 
    [-1.60357093811035, -2.25483322143555, 0.0875115767121315], 
    [-1.59328079223633, -2.28168416023254, 0.0898254886269569], 
    [-1.61025214195251, -2.30288577079773, 0.105395831167698], 
    [-1.57531571388245, -2.31326341629028, 0.100721277296543], 
    [-1.59942138195038, -2.32575917243958, 0.11884943395853], 
    [-1.62515485286713, -2.31945490837097, 0.127029225230217], 
    [-1.609290599823, -2.34574365615845, 0.135399803519249], 
    [-1.64860355854034, -2.30886435508728, 0.140506342053413], 
    [-1.57878446578979, -2.34392070770264, 0.125538811087608], 
    [-1.58710384368896, -2.36534070968628, 0.144533410668373], 
    [-1.55743336677551, -2.36226797103882, 0.139751061797142], 
    [-1.53762328624725, -2.37741827964783, 0.154106095433235], 
    [-1.54897916316986, -2.34088754653931, 0.120888896286488], 
    [-1.52734005451202, -2.3559422492981, 0.136108383536339], 
    [-1.51813590526581, -2.33368039131165, 0.117617346346378], 
    [-1.50984299182892, -2.37176012992859, 0.15134696662426], 
    [-1.49288487434387, -2.34913969039917, 0.135801956057549], 
    [-1.46751594543457, -2.34847784042358, 0.157532051205635], 
    [-1.46713852882385, -2.32596969604492, 0.133984044194221], 
    [-1.49000513553619, -2.32256197929382, 0.113502897322178], 
    [-1.48496472835541, -2.36984586715698, 0.161893352866173], 
    [-1.48416042327881, -2.3919575214386, 0.18591471016407], 
    [-1.4658762216568, -2.36865091323853, 0.183270290493965], 
    [-1.49903833866119, -2.38798904418945, 0.168372496962547], 
    [-1.50332450866699, -2.41322207450867, 0.177048817276955], 
    [-1.47837483882904, -2.41250729560852, 0.197153106331825], 
    [-1.46861207485199, -2.3888738155365, 0.204483225941658], 
    [-1.47555828094482, -2.41538643836975, 0.223142847418785], 
    [-1.45768260955811, -2.38392806053162, 0.228132084012032], 
    [-1.44862329959869, -2.36216378211975, 0.206500872969627], 
    [-1.42859101295471, -2.3369574546814, 0.200637951493263], 
    [-1.4465399980545, -2.34560465812683, 0.179622396826744], 
    [-1.43250751495361, -2.35157680511475, 0.233627960085869], 
    [-1.41076552867889, -2.32424974441528, 0.248113468289375], 
    [-1.45167422294617, -2.37618184089661, 0.251009583473206], 
    [-1.42295384407043, -2.34383392333984, 0.262814193964005], 
    [-1.43878853321075, -2.36151599884033, 0.264078795909882], 
    [-1.41344261169434, -2.32502174377441, 0.220908388495445], 
    [-1.40740239620209, -2.30861210823059, 0.194996163249016], 
    [-1.39515161514282, -2.3013026714325, 0.227839693427086], 
    [-1.38779425621033, -2.27866387367249, 0.190209463238716], 
    [-1.38147330284119, -2.27519035339355, 0.251104861497879], 
    [-1.39986097812653, -2.30033159255981, 0.262506902217865], 
    [-1.3799741268158, -2.27532196044922, 0.22093178331852], 
    [-1.37199330329895, -2.25631284713745, 0.232613191008568], 
    [-1.36853957176208, -2.25421190261841, 0.205712422728539], 
    [-1.35560500621796, -2.2268807888031, 0.19798181951046], 
    [-1.36271059513092, -2.2337019443512, 0.226811751723289], 
    [-1.37156307697296, -2.24646854400635, 0.176008000969887], 
    [-1.38250386714935, -2.23021531105042, 0.148039922118187], 
    [-1.36300182342529, -2.21410822868347, 0.169443890452385], 
    [-1.39444375038147, -2.26209616661072, 0.156137004494667], 
    [-1.40647649765015, -2.24125123023987, 0.128275796771049], 
    [-1.4212943315506, -2.27110505104065, 0.134884312748909], 
    [-1.41099882125854, -2.29121541976929, 0.163620010018349], 
    [-1.43892848491669, -2.30181241035461, 0.138807937502861], 
    [-1.42698562145233, -2.31918239593506, 0.172197237610817], 
    [-1.44827079772949, -2.32873606681824, 0.155648037791252], 
    [-1.46530270576477, -2.30058169364929, 0.112780459225178], 
    [-1.4454517364502, -2.27514791488647, 0.107967652380466], 
    [-1.45769190788269, -2.24633121490479, 0.0883723869919777], 
    [-1.42940592765808, -2.24880409240723, 0.105562396347523], 
    [-1.47982537746429, -2.26758575439453, 0.0859457328915596], 
    [-1.50680994987488, -2.27913737297058, 0.0849667266011238], 
    [-1.48851919174194, -2.22232508659363, 0.0734488740563393], 
    [-1.51411783695221, -2.24785208702087, 0.0752708688378334], 
    [-1.49031376838684, -2.29825115203857, 0.095841147005558], 
    [-1.51679408550262, -2.30781960487366, 0.0956863239407539], 
    [-1.54077863693237, -2.31889176368713, 0.105889983475208], 
    [-1.53403031826019, -2.27382254600525, 0.0791325345635414], 
    [-1.54669785499573, -2.2976598739624, 0.0923972502350807], 
    [-1.56386637687683, -2.27600240707397, 0.0832675769925117], 
    [-1.57722771167755, -2.24792051315308, 0.0793640092015266], 
    [-1.47473847866058, -2.18413662910461, 0.0801087394356728], 
    [-1.45246386528015, -2.21564030647278, 0.0842595472931862], 
    [-1.42285406589508, -2.2179868221283, 0.103183068335056], 
    [-1.44403111934662, -2.1873881816864, 0.0891599133610725], 
    [-1.47184824943542, -2.147794008255, 0.086093582212925], 
    [-1.41831207275391, -2.18908429145813, 0.104025550186634], 
    [-1.43674159049988, -2.15836668014526, 0.0954901054501534], 
    [-1.46230244636536, -2.10428190231323, 0.0949795916676521], 
    [-1.41481256484985, -2.13718819618225, 0.107927538454533], 
    [-1.39839339256287, -2.16997599601746, 0.117862530052662], 
    [-1.37764120101929, -2.1975212097168, 0.143752321600914], 
    [-1.37686204910278, -2.16759562492371, 0.143038019537926], 
    [-1.3994402885437, -2.20857834815979, 0.122999854385853], 
    [-1.38575601577759, -2.14022040367126, 0.128819361329079], 
    [-1.36554288864136, -2.11436057090759, 0.142879709601402], 
    [-1.36094522476196, -2.14825034141541, 0.155816867947578], 
    [-1.40980553627014, -2.10742425918579, 0.115508325397968], 
    [-1.42895865440369, -2.0720751285553, 0.108745224773884], 
    [-1.38717234134674, -2.08504033088684, 0.122602947056293], 
    [-1.39535653591156, -2.04952025413513, 0.116677887737751], 
    [-1.3712911605835, -2.06671762466431, 0.134353086352348], 
    [-1.35751330852509, -2.0842719078064, 0.149212881922722], 
    [-1.34860181808472, -2.0576057434082, 0.148941919207573], 
    [-1.33722746372223, -2.06746935844421, 0.168994888663292], 
    [-1.34288907051086, -2.09681463241577, 0.172668114304543], 
    [-1.34996736049652, -2.12812185287476, 0.17702428996563], 
    [-1.35090148448944, -2.16012954711914, 0.191266372799873], 
    [-1.35388684272766, -2.19490170478821, 0.194639071822166], 
    [-1.3622123003006, -2.18063759803772, 0.167071625590324], 
    [-1.35643970966339, -2.20782351493835, 0.221134498715401], 
    [-1.36526107788086, -2.21579742431641, 0.248962715268135], 
    [-1.37263238430023, -2.24190139770508, 0.252980291843414], 
    [-1.36553740501404, -2.04662775993347, 0.136845007538795], 
    [-1.41377997398376, -2.32371759414673, 0.279466062784195], 
    [-1.39118456840515, -2.27813816070557, 0.277731567621231], 
    [-1.45407128334045, -2.3799614906311, 0.275906682014465], 
    [-1.46814119815826, -2.40237760543823, 0.251563787460327], 
    [-1.63214778900146, -2.15592217445374, 0.0943257585167885], 
    [-1.67249357700348, -2.15984535217285, 0.110741086304188], 
    [-1.67904090881348, -2.12872195243835, 0.111725963652134], 
    [-1.64837300777435, -2.129958152771, 0.10267449170351]
] # synapse_vertex_list

synapse_wall_list = [
    [4, 0, 1], 
    [1, 0, 2], 
    [0, 4, 3], 
    [4, 5, 7], 
    [5, 4, 8], 
    [1, 8, 4], 
    [7, 6, 4], 
    [3, 4, 6], 
    [11, 9, 8], 
    [10, 8, 9], 
    [8, 10, 5], 
    [8, 1, 11], 
    [11, 12, 13], 
    [12, 11, 1], 
    [13, 14, 11], 
    [11, 14, 9], 
    [14, 15, 16], 
    [14, 13, 15], 
    [17, 14, 16], 
    [14, 17, 9], 
    [18, 17, 16], 
    [19, 9, 17], 
    [19, 10, 9], 
    [18, 16, 20], 
    [20, 21, 18], 
    [22, 21, 20], 
    [22, 20, 24], 
    [23, 22, 25], 
    [22, 24, 25], 
    [25, 26, 28], 
    [26, 25, 24], 
    [25, 27, 23], 
    [27, 25, 28], 
    [26, 31, 28], 
    [32, 28, 29], 
    [29, 28, 30], 
    [28, 32, 27], 
    [31, 30, 28], 
    [33, 32, 34], 
    [35, 32, 33], 
    [34, 32, 29], 
    [33, 36, 35], 
    [37, 36, 33], 
    [37, 33, 38], 
    [38, 40, 39], 
    [38, 33, 34], 
    [38, 34, 41], 
    [40, 38, 41], 
    [41, 34, 43], 
    [41, 42, 44], 
    [41, 43, 42], 
    [40, 41, 44], 
    [44, 49, 45], 
    [44, 45, 47], 
    [44, 48, 46], 
    [46, 40, 44], 
    [48, 44, 47], 
    [42, 49, 44], 
    [51, 45, 49], 
    [49, 42, 50], 
    [50, 51, 49], 
    [54, 45, 51], 
    [51, 52, 55], 
    [52, 51, 50], 
    [53, 54, 51], 
    [53, 51, 55], 
    [55, 52, 57], 
    [53, 55, 56], 
    [56, 55, 57], 
    [57, 52, 60], 
    [58, 57, 60], 
    [58, 59, 57], 
    [59, 56, 57], 
    [60, 61, 62], 
    [61, 60, 63], 
    [58, 60, 62], 
    [60, 52, 63], 
    [63, 52, 66], 
    [63, 64, 61], 
    [63, 65, 64], 
    [65, 63, 66], 
    [52, 50, 66], 
    [68, 67, 66], 
    [66, 67, 65], 
    [66, 50, 68], 
    [67, 68, 69], 
    [68, 43, 69], 
    [43, 68, 42], 
    [50, 42, 68], 
    [69, 43, 29], 
    [67, 69, 30], 
    [30, 69, 29], 
    [67, 30, 70], 
    [67, 70, 71], 
    [67, 71, 65], 
    [72, 73, 71], 
    [71, 74, 72], 
    [73, 65, 71], 
    [70, 74, 71], 
    [76, 72, 74], 
    [78, 75, 74], 
    [77, 74, 75], 
    [74, 77, 76], 
    [74, 70, 78], 
    [79, 78, 31], 
    [75, 78, 79], 
    [70, 31, 78], 
    [79, 26, 80], 
    [80, 82, 79], 
    [79, 81, 75], 
    [81, 79, 82], 
    [26, 79, 31], 
    [80, 15, 82], 
    [82, 83, 81], 
    [83, 82, 15], 
    [15, 13, 83], 
    [83, 13, 84], 
    [12, 84, 13], 
    [84, 12, 2], 
    [77, 75, 81], 
    [15, 80, 24], 
    [26, 24, 80], 
    [72, 76, 86], 
    [85, 86, 76], 
    [85, 88, 86], 
    [86, 73, 72], 
    [73, 86, 87], 
    [87, 86, 88], 
    [88, 85, 89], 
    [88, 89, 91], 
    [88, 90, 87], 
    [91, 90, 88], 
    [91, 89, 92], 
    [92, 93, 91], 
    [91, 94, 90], 
    [94, 91, 93], 
    [90, 94, 97], 
    [95, 94, 96], 
    [97, 94, 95], 
    [98, 96, 94], 
    [93, 98, 94], 
    [100, 96, 98], 
    [99, 100, 98], 
    [98, 101, 99], 
    [101, 98, 93], 
    [101, 92, 102], 
    [93, 92, 101], 
    [102, 103, 101], 
    [99, 101, 103], 
    [103, 104, 105], 
    [103, 102, 104], 
    [103, 106, 99], 
    [105, 106, 103], 
    [106, 107, 108], 
    [106, 105, 107], 
    [99, 106, 109], 
    [109, 106, 108], 
    [99, 109, 110], 
    [100, 99, 110], 
    [110, 111, 100], 
    [111, 112, 113], 
    [111, 113, 100], 
    [112, 62, 113], 
    [113, 95, 96], 
    [62, 95, 113], 
    [96, 100, 113], 
    [58, 62, 112], 
    [114, 58, 112], 
    [59, 58, 114], 
    [115, 59, 114], 
    [59, 115, 116], 
    [56, 59, 116], 
    [116, 53, 56], 
    [117, 107, 105], 
    [105, 104, 117], 
    [97, 87, 90], 
    [87, 97, 64], 
    [61, 64, 97], 
    [97, 95, 61], 
    [62, 61, 95], 
    [73, 87, 64], 
    [65, 73, 64], 
    [30, 31, 70], 
    [118, 45, 54], 
    [53, 119, 54], 
    [118, 47, 45], 
    [120, 46, 48], 
    [120, 121, 46], 
    [40, 46, 121], 
    [39, 40, 121], 
    [34, 29, 43], 
    [20, 15, 24], 
    [15, 20, 16], 
    [12, 1, 2], 
    [6, 122, 3], 
    [123, 122, 6], 
    [125, 123, 124], 
    [123, 125, 122], 
    [130, 127, 126], 
    [127, 128, 126], 
    [126, 129, 130], 
    [130, 133, 131], 
    [131, 134, 130], 
    [127, 130, 134], 
    [133, 130, 132], 
    [129, 132, 130], 
    [137, 134, 135], 
    [136, 135, 134], 
    [134, 131, 136], 
    [134, 137, 127], 
    [137, 139, 138], 
    [138, 127, 137], 
    [139, 137, 140], 
    [137, 135, 140], 
    [140, 142, 141], 
    [140, 141, 139], 
    [143, 142, 140], 
    [140, 135, 143], 
    [144, 142, 143], 
    [145, 143, 135], 
    [145, 135, 136], 
    [144, 146, 142], 
    [146, 144, 147], 
    [148, 146, 147], 
    [148, 150, 146], 
    [149, 151, 148], 
    [148, 151, 150], 
    [151, 154, 152], 
    [152, 150, 151], 
    [151, 149, 153], 
    [153, 154, 151], 
    [152, 154, 157], 
    [158, 155, 154], 
    [155, 156, 154], 
    [154, 153, 158], 
    [157, 154, 156], 
    [159, 160, 158], 
    [161, 159, 158], 
    [160, 155, 158], 
    [159, 161, 162], 
    [163, 159, 162], 
    [163, 164, 159], 
    [164, 165, 166], 
    [164, 160, 159], 
    [164, 167, 160], 
    [166, 167, 164], 
    [167, 169, 160], 
    [167, 170, 168], 
    [167, 168, 169], 
    [166, 170, 167], 
    [170, 171, 175], 
    [170, 173, 171], 
    [170, 172, 174], 
    [172, 170, 166], 
    [174, 173, 170], 
    [168, 170, 175], 
    [177, 175, 171], 
    [175, 176, 168], 
    [176, 175, 177], 
    [180, 177, 171], 
    [177, 181, 178], 
    [178, 176, 177], 
    [179, 177, 180], 
    [179, 181, 177], 
    [181, 183, 178], 
    [179, 182, 181], 
    [182, 183, 181], 
    [183, 186, 178], 
    [184, 186, 183], 
    [184, 183, 185], 
    [185, 183, 182], 
    [186, 188, 187], 
    [187, 189, 186], 
    [184, 188, 186], 
    [186, 189, 178], 
    [189, 192, 178], 
    [189, 187, 190], 
    [189, 190, 191], 
    [191, 192, 189], 
    [178, 192, 176], 
    [194, 192, 193], 
    [192, 191, 193], 
    [192, 194, 176], 
    [193, 195, 194], 
    [194, 195, 169], 
    [169, 168, 194], 
    [176, 194, 168], 
    [195, 155, 169], 
    [193, 156, 195], 
    [156, 155, 195], 
    [193, 196, 156], 
    [193, 197, 196], 
    [193, 191, 197], 
    [198, 197, 199], 
    [197, 198, 200], 
    [199, 197, 191], 
    [196, 197, 200], 
    [202, 200, 198], 
    [204, 200, 201], 
    [203, 201, 200], 
    [200, 202, 203], 
    [200, 204, 196], 
    [205, 157, 204], 
    [201, 205, 204], 
    [196, 204, 157], 
    [205, 206, 152], 
    [206, 205, 208], 
    [205, 201, 207], 
    [207, 208, 205], 
    [152, 157, 205], 
    [206, 208, 141], 
    [208, 207, 209], 
    [209, 141, 208], 
    [141, 209, 139], 
    [209, 210, 139], 
    [138, 139, 210], 
    [210, 128, 138], 
    [203, 207, 201], 
    [141, 150, 206], 
    [152, 206, 150], 
    [198, 212, 202], 
    [211, 202, 212], 
    [211, 212, 214], 
    [212, 198, 199], 
    [199, 213, 212], 
    [213, 214, 212], 
    [214, 215, 211], 
    [214, 217, 215], 
    [214, 213, 216], 
    [217, 214, 216], 
    [217, 218, 215], 
    [218, 217, 219], 
    [217, 216, 220], 
    [220, 219, 217], 
    [216, 223, 220], 
    [221, 222, 220], 
    [223, 221, 220], 
    [224, 220, 222], 
    [219, 220, 224], 
    [226, 224, 222], 
    [225, 224, 226], 
    [224, 225, 227], 
    [227, 219, 224], 
    [227, 228, 218], 
    [219, 227, 218], 
    [228, 227, 229], 
    [225, 229, 227], 
    [229, 231, 230], 
    [229, 230, 228], 
    [229, 225, 232], 
    [231, 229, 232], 
    [232, 234, 233], 
    [232, 233, 231], 
    [225, 235, 232], 
    [235, 234, 232], 
    [225, 236, 235], 
    [226, 236, 225], 
    [236, 226, 237], 
    [237, 239, 238], 
    [237, 226, 239], 
    [238, 239, 188], 
    [239, 222, 221], 
    [188, 239, 221], 
    [222, 239, 226], 
    [184, 238, 188], 
    [240, 238, 184], 
    [185, 240, 184], 
    [241, 240, 185], 
    [185, 242, 241], 
    [182, 242, 185], 
    [242, 182, 179], 
    [243, 231, 233], 
    [231, 243, 230], 
    [223, 216, 213], 
    [213, 190, 223], 
    [187, 223, 190], 
    [223, 187, 221], 
    [188, 221, 187], 
    [199, 190, 213], 
    [191, 190, 199], 
    [156, 196, 157], 
    [244, 180, 171], 
    [179, 180, 245], 
    [244, 171, 173], 
    [246, 174, 172], 
    [246, 172, 247], 
    [166, 247, 172], 
    [165, 247, 166], 
    [160, 169, 155], 
    [146, 150, 141], 
    [141, 142, 146], 
    [138, 128, 127], 
    [132, 129, 248], 
    [249, 132, 248], 
    [251, 250, 249], 
    [249, 248, 251], 
    [118, 244, 173], 
    [174, 48, 47], 
    [120, 48, 174], 
    [120, 246, 247], 
    [165, 39, 121], 
    [38, 39, 165], 
    [163, 37, 38], 
    [36, 37, 163], 
    [35, 36, 162], 
    [158, 32, 35], 
    [27, 32, 158], 
    [23, 27, 153], 
    [22, 23, 149], 
    [21, 22, 148], 
    [18, 21, 147], 
    [17, 18, 144], 
    [19, 17, 143], 
    [10, 19, 145], 
    [5, 10, 136], 
    [7, 5, 131], 
    [7, 133, 132], 
    [123, 6, 132], 
    [124, 123, 249], 
    [124, 250, 251], 
    [248, 122, 125], 
    [129, 3, 122], 
    [3, 129, 126], 
    [128, 2, 0], 
    [210, 84, 2], 
    [209, 83, 84], 
    [207, 81, 83], 
    [77, 81, 207], 
    [202, 76, 77], 
    [85, 76, 202], 
    [89, 85, 211], 
    [92, 89, 215], 
    [102, 92, 218], 
    [230, 104, 102], 
    [243, 117, 104], 
    [233, 107, 117], 
    [234, 108, 107], 
    [108, 234, 235], 
    [109, 235, 236], 
    [237, 111, 110], 
    [111, 237, 238], 
    [114, 112, 238], 
    [115, 114, 240], 
    [242, 116, 115], 
    [116, 242, 179], 
    [119, 53, 179], 
    [119, 245, 180], 
    [118, 54, 180], 
    [118, 173, 47], 
    [174, 47, 173], 
    [120, 174, 246], 
    [120, 247, 121], 
    [165, 121, 247], 
    [38, 165, 164], 
    [163, 38, 164], 
    [36, 163, 162], 
    [35, 162, 161], 
    [158, 35, 161], 
    [27, 158, 153], 
    [23, 153, 149], 
    [22, 149, 148], 
    [21, 148, 147], 
    [18, 147, 144], 
    [17, 144, 143], 
    [19, 143, 145], 
    [10, 145, 136], 
    [5, 136, 131], 
    [7, 131, 133], 
    [7, 132, 6], 
    [123, 132, 249], 
    [124, 249, 250], 
    [124, 251, 125], 
    [248, 125, 251], 
    [129, 122, 248], 
    [3, 126, 0], 
    [128, 0, 126], 
    [210, 2, 128], 
    [209, 84, 210], 
    [207, 83, 209], 
    [77, 207, 203], 
    [202, 77, 203], 
    [85, 202, 211], 
    [89, 211, 215], 
    [92, 215, 218], 
    [102, 218, 228], 
    [230, 102, 228], 
    [243, 104, 230], 
    [233, 117, 243], 
    [234, 107, 233], 
    [108, 235, 109], 
    [109, 236, 110], 
    [237, 110, 236], 
    [111, 238, 112], 
    [114, 238, 240], 
    [115, 240, 241], 
    [242, 115, 241], 
    [116, 179, 53], 
    [119, 179, 245], 
    [119, 180, 54], 
    [118, 180, 244]
] # synapse_wall_list

synapse = m.GeometryObject(
    name = 'synapse',
    vertex_list = synapse_vertex_list,
    wall_list = synapse_wall_list,
    surface_regions = []
)
# ^^^^ synapse ^^^^


