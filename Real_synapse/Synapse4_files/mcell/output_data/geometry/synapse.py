import mcell as m

# ---- synapse ----
synapse_vertex_list = [
    [2.06811094284058, 2.05938005447388, -0.0117632448673248], 
    [2.05898094177246, 2.05077219009399, -0.0336243808269501], 
    [2.03803396224976, 2.04878854751587, -0.00935089588165283], 
    [2.06954002380371, 2.06869983673096, 0.0141394436359406], 
    [2.03741908073425, 2.06558513641357, 0.0186435878276825], 
    [2.05739569664001, 2.08432149887085, 0.0328479111194611], 
    [2.08260750770569, 2.08564758300781, 0.0357410907745361], 
    [2.11335706710815, 2.07441806793213, 0.0216004252433777], 
    [2.10166788101196, 2.09964394569397, 0.0519644618034363], 
    [2.13554883003235, 2.09866857528687, 0.0476487874984741], 
    [2.14683771133423, 2.11859273910522, 0.0707046836614609], 
    [2.11831760406494, 2.11658430099487, 0.0672743916511536], 
    [2.12011551856995, 2.14362692832947, 0.0857148617506027], 
    [2.08974885940552, 2.12696433067322, 0.0699335038661957], 
    [2.08201479911804, 2.15677642822266, 0.0845953226089478], 
    [2.05899572372437, 2.13670182228088, 0.0695482343435287], 
    [2.06466245651245, 2.10805892944336, 0.0522160530090332], 
    [2.02969551086426, 2.1204354763031, 0.0569111704826355], 
    [2.03337574005127, 2.09557700157166, 0.0410719811916351], 
    [2.01501131057739, 2.07757663726807, 0.0299873352050781], 
    [1.99886441230774, 2.10464596748352, 0.0469891726970673], 
    [1.99663126468658, 2.13789296150208, 0.0654449313879013], 
    [1.96565794944763, 2.11724662780762, 0.0517353117465973], 
    [1.99058794975281, 2.07931065559387, 0.0294850170612335], 
    [1.96358597278595, 2.0887086391449, 0.0349474251270294], 
    [1.93472146987915, 2.07465982437134, 0.0252306461334229], 
    [1.95406854152679, 2.06452441215515, 0.0172885060310364], 
    [1.97643172740936, 2.06489157676697, 0.0169190466403961], 
    [1.93263006210327, 2.0987548828125, 0.0409296751022339], 
    [1.93244624137878, 2.12497806549072, 0.0558202266693115], 
    [1.90039134025574, 2.10322022438049, 0.0450848937034607], 
    [1.89971256256104, 2.0669481754303, 0.0242605805397034], 
    [1.87609994411469, 2.03363585472107, 0.00805419683456421], 
    [1.93329966068268, 2.04984831809998, 0.00991833209991455], 
    [1.90992331504822, 2.03096032142639, 0.00270664691925049], 
    [1.87173414230347, 2.0878746509552, 0.0376832187175751], 
    [1.86239624023438, 2.05972719192505, 0.0230354964733124], 
    [1.84025394916534, 2.03005194664001, 0.0111951231956482], 
    [1.83977806568146, 2.07974553108215, 0.0371107459068298], 
    [1.83322644233704, 2.05524277687073, 0.0260184407234192], 
    [1.81341338157654, 2.06611180305481, 0.0397580862045288], 
    [1.80978989601135, 2.03994250297546, 0.0259967446327209], 
    [1.80628478527069, 2.01427817344666, 0.0119612812995911], 
    [1.7800235748291, 2.04797768592834, 0.0415829718112946], 
    [1.78616654872894, 2.0256564617157, 0.0248548984527588], 
    [1.79222667217255, 2.07216453552246, 0.0525177270174026], 
    [1.76749539375305, 2.07412838935852, 0.0679062008857727], 
    [1.80908119678497, 2.10533928871155, 0.058835968375206], 
    [1.7731568813324, 2.1053774356842, 0.0838107615709305], 
    [1.77543580532074, 2.13471841812134, 0.101503297686577], 
    [1.79716742038727, 2.12849426269531, 0.0834481418132782], 
    [1.82734072208405, 2.14840507507324, 0.0800906866788864], 
    [1.80034172534943, 2.15389895439148, 0.0985308438539505], 
    [1.7751190662384, 2.15979385375977, 0.115412548184395], 
    [1.79745960235596, 2.178879737854, 0.112146601080894], 
    [1.82493591308594, 2.17325448989868, 0.100011005997658], 
    [1.84627556800842, 2.19977951049805, 0.109942063689232], 
    [1.81863963603973, 2.19591546058655, 0.113343566656113], 
    [1.85552048683167, 2.17391276359558, 0.0929106324911118], 
    [1.86883580684662, 2.14722633361816, 0.0741249322891235], 
    [1.88817358016968, 2.17610001564026, 0.09088996052742], 
    [1.87966287136078, 2.20351314544678, 0.108969509601593], 
    [1.89114284515381, 2.23441338539124, 0.127788990736008], 
    [1.90904748439789, 2.21685004234314, 0.11594195663929], 
    [1.85879230499268, 2.22636222839355, 0.125770106911659], 
    [1.91313636302948, 2.19457817077637, 0.101607233285904], 
    [1.92090368270874, 2.17268466949463, 0.0858043879270554], 
    [1.94622278213501, 2.18990063667297, 0.0973266959190369], 
    [1.93789529800415, 2.21332049369812, 0.113599553704262], 
    [1.95798599720001, 2.23312258720398, 0.127175465226173], 
    [1.9247270822525, 2.23691082000732, 0.128330439329147], 
    [1.97023451328278, 2.20725297927856, 0.109184592962265], 
    [1.98296129703522, 2.17598295211792, 0.0890443921089172], 
    [1.98756384849548, 2.22940182685852, 0.123599678277969], 
    [2.00399351119995, 2.20668888092041, 0.109131917357445], 
    [2.02016139030457, 2.23694014549255, 0.126675769686699], 
    [2.03807973861694, 2.21022367477417, 0.11201499402523], 
    [2.02725267410278, 2.18604350090027, 0.0965741127729416], 
    [2.04946351051331, 2.1648211479187, 0.0841535776853561], 
    [2.0151641368866, 2.16264939308167, 0.0817276984453201], 
    [2.07008123397827, 2.19162607192993, 0.102204978466034], 
    [2.06538534164429, 2.22714638710022, 0.122491165995598], 
    [2.1085524559021, 2.20560240745544, 0.121738344430923], 
    [2.10418605804443, 2.17380237579346, 0.100515499711037], 
    [2.13939809799194, 2.16687989234924, 0.104999676346779], 
    [2.14705777168274, 2.19104671478271, 0.126472279429436], 
    [2.16161751747131, 2.14097046852112, 0.0881746858358383], 
    [2.1454381942749, 2.21695613861084, 0.144204780459404], 
    [2.10675358772278, 2.2385950088501, 0.149014726281166], 
    [2.14020991325378, 2.23638844490051, 0.165442734956741], 
    [2.12710118293762, 2.25422382354736, 0.181620076298714], 
    [2.1161482334137, 2.27415895462036, 0.195965901017189], 
    [2.10148167610168, 2.26497840881348, 0.176650926470757], 
    [2.08881855010986, 2.28940963745117, 0.193165183067322], 
    [2.07391667366028, 2.2718493938446, 0.166645810008049], 
    [2.03544974327087, 2.26844787597656, 0.14752222597599], 
    [2.07138681411743, 2.25133180618286, 0.145684510469437], 
    [2.05477166175842, 2.29675769805908, 0.174692720174789], 
    [2.02488923072815, 2.29633450508118, 0.165012240409851], 
    [2.02335214614868, 2.31445336341858, 0.183256298303604], 
    [2.06907796859741, 2.3119592666626, 0.203242242336273], 
    [2.04314470291138, 2.31540298461914, 0.195296555757523], 
    [2.04919457435608, 2.33066296577454, 0.212071940302849], 
    [2.01445245742798, 2.34097456932068, 0.200446426868439], 
    [1.99571239948273, 2.31575441360474, 0.180081024765968], 
    [1.96590149402618, 2.34624433517456, 0.189942225813866], 
    [1.99773061275482, 2.37508487701416, 0.201318264007568], 
    [1.96856284141541, 2.38779377937317, 0.196364030241966], 
    [1.95252335071564, 2.41567420959473, 0.183972433209419], 
    [1.93260252475739, 2.38567018508911, 0.190481513738632], 
    [1.902459025383, 2.40861415863037, 0.186205074191093], 
    [1.92253053188324, 2.34936952590942, 0.187159985303879], 
    [1.92545807361603, 2.41528034210205, 0.178993239998817], 
    [1.8921480178833, 2.37972092628479, 0.194404557347298], 
    [1.87233817577362, 2.41383266448975, 0.18535852432251], 
    [1.88899993896484, 2.34710049629211, 0.186761662364006], 
    [1.86457359790802, 2.35940933227539, 0.19215190410614], 
    [1.84864628314972, 2.38836717605591, 0.194886162877083], 
    [1.82129859924316, 2.40582418441772, 0.189697906374931], 
    [1.84294044971466, 2.41627025604248, 0.176961347460747], 
    [1.81369388103485, 2.37792730331421, 0.204905062913895], 
    [1.83637261390686, 2.35263538360596, 0.194998532533646], 
    [1.86157846450806, 2.32787847518921, 0.183541730046272], 
    [1.82880640029907, 2.32313013076782, 0.185998246073723], 
    [1.80655777454376, 2.33815479278564, 0.197331160306931], 
    [1.77756798267365, 2.32575654983521, 0.200931787490845], 
    [1.78659021854401, 2.35758423805237, 0.20650489628315], 
    [1.79710638523102, 2.30048680305481, 0.180287331342697], 
    [1.81996703147888, 2.27487707138062, 0.161990001797676], 
    [1.78695237636566, 2.2661554813385, 0.164041996002197], 
    [1.83972895145416, 2.29923391342163, 0.171582266688347], 
    [1.76477885246277, 2.27819848060608, 0.178369551897049], 
    [1.75199604034424, 2.30025339126587, 0.196925222873688], 
    [1.71636378765106, 2.27024912834167, 0.199721544981003], 
    [1.74909067153931, 2.33036136627197, 0.2113888412714], 
    [1.73928785324097, 2.26714062690735, 0.184098750352859], 
    [1.74767231941223, 2.24615740776062, 0.167748376727104], 
    [1.71257936954498, 2.24186038970947, 0.182521253824234], 
    [1.72164726257324, 2.21198534965515, 0.164210423827171], 
    [1.75209677219391, 2.21935606002808, 0.15424832701683], 
    [1.74522221088409, 2.1905300617218, 0.146349459886551], 
    [1.77396762371063, 2.18576884269714, 0.128366053104401], 
    [1.77427279949188, 2.21159386634827, 0.140134230256081], 
    [1.75569808483124, 2.16619634628296, 0.133528336882591], 
    [1.80241870880127, 2.2281129360199, 0.138409316539764], 
    [1.77710270881653, 2.23775720596313, 0.152095898985863], 
    [1.79681360721588, 2.20453333854675, 0.124565973877907], 
    [1.82790291309357, 2.21926712989807, 0.125669687986374], 
    [1.83568024635315, 2.24780964851379, 0.142283901572227], 
    [1.80509829521179, 2.25159931182861, 0.151326030492783], 
    [1.8528174161911, 2.27512741088867, 0.156030312180519], 
    [1.87040627002716, 2.25299954414368, 0.141460865736008], 
    [1.90993297100067, 2.26201772689819, 0.14397981762886], 
    [1.88367295265198, 2.2770562171936, 0.153966680169106], 
    [1.90896153450012, 2.29347848892212, 0.162818372249603], 
    [1.87395489215851, 2.30064845085144, 0.167968779802322], 
    [1.89974772930145, 2.32144069671631, 0.176390990614891], 
    [1.93521177768707, 2.31711220741272, 0.175135791301727], 
    [1.96795535087585, 2.30279016494751, 0.169501006603241], 
    [1.94132876396179, 2.2831335067749, 0.157547429203987], 
    [1.98219621181488, 2.2601945400238, 0.144691467285156], 
    [1.94375741481781, 2.25568509101868, 0.140696033835411], 
    [1.99840521812439, 2.28797912597656, 0.161136895418167], 
    [1.76410150527954, 2.34821271896362, 0.210138589143753], 
    [1.78280699253082, 2.38301825523376, 0.204417869448662], 
    [1.79321813583374, 2.40524697303772, 0.192186489701271], 
    [2.09587812423706, 2.31335067749023, 0.218580201268196], 
    [2.11900854110718, 2.29228043556213, 0.216778695583344], 
    [2.03064680099487, 2.14403343200684, 0.0717853605747223], 
    [1.94860935211182, 2.16757845878601, 0.0809286385774612], 
    [1.96152567863464, 2.14514780044556, 0.0676737725734711], 
    [1.92796409130096, 2.14975905418396, 0.0706637501716614], 
    [1.90046775341034, 2.13138151168823, 0.0619411021471024], 
    [1.900674700737, 2.15515184402466, 0.0767985284328461], 
    [1.87315833568573, 2.11742997169495, 0.0548636019229889], 
    [1.84474015235901, 2.12666702270508, 0.06351038813591], 
    [1.84758508205414, 2.10366034507751, 0.049353688955307], 
    [1.94577920436859, 2.02553725242615, -0.00781187415122986], 
    [1.88936543464661, 2.00763130187988, -0.00799226760864258], 
    [1.92307770252228, 2.00555562973022, -0.0166352093219757], 
    [1.9655374288559, 2.04414892196655, 0.00390401482582092], 
    [1.97952890396118, 2.02699494361877, -0.0182908773422241], 
    [2.00381684303284, 2.04980874061584, 0.00631967186927795], 
    [2.01166677474976, 2.03162908554077, -0.0258173048496246], 
    [2.03742146492004, 2.03747367858887, -0.0418655872344971], 
    [2.07811093330383, 2.04938006401062, -0.00176324509084225], 
    [2.06898093223572, 2.04077219963074, -0.0236243810504675], 
    [2.04803395271301, 2.03878855705261, 0.00064910389482975], 
    [2.07954001426697, 2.0586998462677, 0.0241394434124231], 
    [2.04741907119751, 2.05558514595032, 0.0286435876041651], 
    [2.06739568710327, 2.07432150840759, 0.0428479090332985], 
    [2.09260749816895, 2.07564759254456, 0.0457410886883736], 
    [2.12335705757141, 2.06441807746887, 0.0316004231572151], 
    [2.11166787147522, 2.08964395523071, 0.0619644597172737], 
    [2.14554882049561, 2.08866858482361, 0.0576487854123116], 
    [2.15683770179749, 2.10859274864197, 0.0807046815752983], 
    [2.1283175945282, 2.10658431053162, 0.077274389564991], 
    [2.1301155090332, 2.13362693786621, 0.0957148596644402], 
    [2.09974884986877, 2.11696434020996, 0.0799335017800331], 
    [2.0920147895813, 2.1467764377594, 0.0945953205227852], 
    [2.06899571418762, 2.12670183181763, 0.0795482322573662], 
    [2.07466244697571, 2.0980589389801, 0.0622160509228706], 
    [2.03969550132751, 2.11043548583984, 0.0669111683964729], 
    [2.04337573051453, 2.0855770111084, 0.0510719791054726], 
    [2.02501130104065, 2.06757664680481, 0.0399873331189156], 
    [2.008864402771, 2.09464597702026, 0.0569891706109047], 
    [2.00663137435913, 2.12789297103882, 0.0754449293017387], 
    [1.97565793991089, 2.10724663734436, 0.0617353096604347], 
    [2.00058794021606, 2.06931066513062, 0.039485014975071], 
    [1.97358596324921, 2.07870864868164, 0.0449474230408669], 
    [1.94472146034241, 2.06465983390808, 0.0352306440472603], 
    [1.96406853199005, 2.05452442169189, 0.027288505807519], 
    [1.98643171787262, 2.05489158630371, 0.0269190464168787], 
    [1.94263005256653, 2.08875489234924, 0.0509296730160713], 
    [1.94244623184204, 2.11497807502747, 0.065820224583149], 
    [1.91039133071899, 2.09322023391724, 0.0550848916172981], 
    [1.90971255302429, 2.05694818496704, 0.0342605784535408], 
    [1.88609993457794, 2.02363586425781, 0.0180541966110468], 
    [1.94329965114594, 2.03984832763672, 0.0199183318763971], 
    [1.91992330551147, 2.02096033096313, 0.0127066466957331], 
    [1.88173413276672, 2.07787466049194, 0.0476832166314125], 
    [1.87239623069763, 2.04972720146179, 0.0330354943871498], 
    [1.8502539396286, 2.02005195617676, 0.0211951229721308], 
    [1.84977805614471, 2.0697455406189, 0.0471107438206673], 
    [1.84322643280029, 2.04524278640747, 0.0360184386372566], 
    [1.82341337203979, 2.05611181259155, 0.0497580841183662], 
    [1.81978988647461, 2.02994251251221, 0.0359967425465584], 
    [1.81628477573395, 2.0042781829834, 0.0219612810760736], 
    [1.79002356529236, 2.03797769546509, 0.051582969725132], 
    [1.7961665391922, 2.01565647125244, 0.0348548963665962], 
    [1.8022266626358, 2.0621645450592, 0.0625177249312401], 
    [1.77749538421631, 2.06412839889526, 0.0779061987996101], 
    [1.81908118724823, 2.09533929824829, 0.0688359662890434], 
    [1.78315687179565, 2.09537744522095, 0.0938107594847679], 
    [1.785435795784, 2.12471842765808, 0.111503295600414], 
    [1.80716741085052, 2.11849427223206, 0.0934481397271156], 
    [1.8373407125473, 2.13840508460999, 0.0900906845927238], 
    [1.81034171581268, 2.14389896392822, 0.108530841767788], 
    [1.78511905670166, 2.14979386329651, 0.125412553548813], 
    [1.80745959281921, 2.16887974739075, 0.122146598994732], 
    [1.83493590354919, 2.16325449943542, 0.110011003911495], 
    [1.85627555847168, 2.18977952003479, 0.119942061603069], 
    [1.82863962650299, 2.18591547012329, 0.12334356456995], 
    [1.86552047729492, 2.16391277313232, 0.102910630404949], 
    [1.87883579730988, 2.13722634315491, 0.084124930202961], 
    [1.89817357063293, 2.166100025177, 0.100889958441257], 
    [1.88966286182404, 2.19351315498352, 0.11896950751543], 
    [1.90114283561707, 2.22441339492798, 0.137788996100426], 
    [1.91904747486115, 2.20685005187988, 0.125941962003708], 
    [1.86879229545593, 2.2163622379303, 0.135770112276077], 
    [1.92313635349274, 2.18457818031311, 0.111607231199741], 
    [1.930903673172, 2.16268467903137, 0.0958043858408928], 
    [1.95622277259827, 2.17990064620972, 0.107326693832874], 
    [1.94789528846741, 2.20332050323486, 0.123599551618099], 
    [1.96798598766327, 2.22312259674072, 0.137175470590591], 
    [1.93472707271576, 2.22691082954407, 0.138330444693565], 
    [1.98023450374603, 2.19725298881531, 0.119184590876102], 
    [1.99296128749847, 2.16598296165466, 0.0990443900227547], 
    [1.99756383895874, 2.21940183639526, 0.133599683642387], 
    [2.01399350166321, 2.19668889045715, 0.119131915271282], 
    [2.03016138076782, 2.2269401550293, 0.136675775051117], 
    [2.0480797290802, 2.20022368431091, 0.122014991939068], 
    [2.03725266456604, 2.17604351043701, 0.106574110686779], 
    [2.05946350097656, 2.15482115745544, 0.0941535755991936], 
    [2.02516412734985, 2.15264940261841, 0.0917276963591576], 
    [2.08008122444153, 2.18162608146667, 0.112204976379871], 
    [2.07538533210754, 2.21714639663696, 0.132491171360016], 
    [2.11855244636536, 2.19560241699219, 0.131738349795341], 
    [2.11418604850769, 2.1638023853302, 0.110515497624874], 
    [2.1493980884552, 2.15687990188599, 0.114999674260616], 
    [2.157057762146, 2.18104672431946, 0.136472284793854], 
    [2.17161750793457, 2.13097047805786, 0.0981746837496758], 
    [2.15543818473816, 2.20695614814758, 0.154204785823822], 
    [2.11675357818604, 2.22859501838684, 0.159014731645584], 
    [2.15020990371704, 2.22638845443726, 0.175442740321159], 
    [2.13710117340088, 2.24422383308411, 0.191620081663132], 
    [2.12614822387695, 2.2641589641571, 0.205965906381607], 
    [2.11148166656494, 2.25497841835022, 0.186650931835175], 
    [2.09881854057312, 2.27940964698792, 0.20316518843174], 
    [2.08391666412354, 2.26184940338135, 0.176645815372467], 
    [2.04544973373413, 2.25844788551331, 0.157522231340408], 
    [2.08138680458069, 2.2413318157196, 0.155684515833855], 
    [2.06477165222168, 2.28675770759583, 0.184692725539207], 
    [2.03488922119141, 2.28633451461792, 0.175012245774269], 
    [2.03335213661194, 2.30445337295532, 0.193256303668022], 
    [2.07907795906067, 2.30195927619934, 0.213242247700691], 
    [2.05314469337463, 2.30540299415588, 0.205296561121941], 
    [2.05919456481934, 2.32066297531128, 0.222071945667267], 
    [2.02445244789124, 2.33097457885742, 0.210446432232857], 
    [2.00571250915527, 2.30575442314148, 0.190081030130386], 
    [1.97590148448944, 2.3362443447113, 0.199942231178284], 
    [2.00773072242737, 2.3650848865509, 0.211318269371986], 
    [1.97856283187866, 2.37779378890991, 0.206364035606384], 
    [1.96252334117889, 2.40567421913147, 0.193972438573837], 
    [1.94260251522064, 2.37567019462585, 0.20048151910305], 
    [1.91245901584625, 2.39861416816711, 0.196205079555511], 
    [1.9325305223465, 2.33936953544617, 0.197159990668297], 
    [1.93545806407928, 2.40528035163879, 0.188993245363235], 
    [1.90214800834656, 2.36972093582153, 0.204404562711716], 
    [1.88233816623688, 2.40383267402649, 0.195358529686928], 
    [1.8989999294281, 2.33710050582886, 0.196761667728424], 
    [1.87457358837128, 2.34940934181213, 0.202151909470558], 
    [1.85864627361298, 2.37836718559265, 0.204886168241501], 
    [1.83129858970642, 2.39582419395447, 0.199697911739349], 
    [1.85294044017792, 2.40627026557922, 0.186961352825165], 
    [1.82369387149811, 2.36792731285095, 0.214905068278313], 
    [1.84637260437012, 2.3426353931427, 0.204998537898064], 
    [1.87157845497131, 2.31787848472595, 0.19354173541069], 
    [1.83880639076233, 2.31313014030457, 0.195998251438141], 
    [1.81655776500702, 2.32815480232239, 0.207331165671349], 
    [1.7875679731369, 2.31575655937195, 0.210931792855263], 
    [1.79659020900726, 2.34758424758911, 0.216504901647568], 
    [1.80710637569427, 2.29048681259155, 0.190287336707115], 
    [1.82996702194214, 2.26487708091736, 0.171990007162094], 
    [1.79695236682892, 2.25615549087524, 0.174042001366615], 
    [1.84972894191742, 2.28923392295837, 0.181582272052765], 
    [1.77477884292603, 2.26819849014282, 0.188369557261467], 
    [1.7619960308075, 2.29025340080261, 0.206925228238106], 
    [1.72636377811432, 2.26024913787842, 0.209721550345421], 
    [1.75909066200256, 2.32036137580872, 0.221388846635818], 
    [1.74928784370422, 2.25714063644409, 0.194098755717278], 
    [1.75767230987549, 2.23615741729736, 0.177748382091522], 
    [1.72257936000824, 2.23186039924622, 0.192521259188652], 
    [1.7316472530365, 2.20198535919189, 0.174210429191589], 
    [1.76209676265717, 2.20935606956482, 0.164248332381248], 
    [1.75522220134735, 2.18053007125854, 0.156349465250969], 
    [1.78396761417389, 2.17576885223389, 0.138366058468819], 
    [1.78427278995514, 2.20159387588501, 0.150134235620499], 
    [1.76569807529449, 2.1561963558197, 0.143528342247009], 
    [1.81241869926453, 2.21811294555664, 0.148409321904182], 
    [1.78710269927979, 2.22775721549988, 0.162095904350281], 
    [1.80681359767914, 2.1945333480835, 0.134565979242325], 
    [1.83790290355682, 2.20926713943481, 0.135669693350792], 
    [1.84568023681641, 2.23780965805054, 0.152283906936646], 
    [1.81509828567505, 2.24159932136536, 0.161326035857201], 
    [1.86281740665436, 2.26512742042542, 0.166030317544937], 
    [1.88040626049042, 2.24299955368042, 0.151460871100426], 
    [1.91993296146393, 2.25201773643494, 0.153979822993279], 
    [1.89367294311523, 2.26705622673035, 0.163966685533524], 
    [1.91896152496338, 2.28347849845886, 0.172818377614021], 
    [1.88395488262177, 2.29064846038818, 0.17796878516674], 
    [1.90974771976471, 2.31144070625305, 0.186390995979309], 
    [1.94521176815033, 2.30711221694946, 0.185135796666145], 
    [1.97795534133911, 2.29279017448425, 0.179501011967659], 
    [1.95132875442505, 2.27313351631165, 0.167547434568405], 
    [1.99219620227814, 2.25019454956055, 0.154691472649574], 
    [1.95375740528107, 2.24568510055542, 0.150696039199829], 
    [2.00840520858765, 2.27797913551331, 0.171136900782585], 
    [1.7741014957428, 2.33821272850037, 0.220138594508171], 
    [1.79280698299408, 2.37301826477051, 0.21441787481308], 
    [1.803218126297, 2.39524698257446, 0.202186495065689], 
    [2.10587811470032, 2.30335068702698, 0.228580206632614], 
    [2.12900853157043, 2.28228044509888, 0.226778700947762], 
    [2.04064679145813, 2.13403344154358, 0.0817853584885597], 
    [1.95860934257507, 2.15757846832275, 0.0909286364912987], 
    [1.9715256690979, 2.1351478099823, 0.0776737704873085], 
    [1.93796408176422, 2.1397590637207, 0.0806637480854988], 
    [1.9104677438736, 2.12138152122498, 0.0719411000609398], 
    [1.91067469120026, 2.1451518535614, 0.0867985263466835], 
    [1.88315832614899, 2.10742998123169, 0.0648635998368263], 
    [1.85474014282227, 2.11666703224182, 0.0735103860497475], 
    [1.8575850725174, 2.09366035461426, 0.0593536868691444], 
    [1.95577919483185, 2.01553726196289, 0.00218812562525272], 
    [1.89936542510986, 1.99763131141663, 0.00200773216784], 
    [1.93307769298553, 1.99555563926697, -0.00663520954549313], 
    [1.97553741931915, 2.0341489315033, 0.0139040146023035], 
    [1.98952889442444, 2.01699495315552, -0.00829087756574154], 
    [2.01381683349609, 2.03980875015259, 0.0163196716457605], 
    [2.02166676521301, 2.02162909507751, -0.0158173050731421], 
    [2.0474214553833, 2.02747368812561, -0.0318655893206596]
] # synapse_vertex_list

synapse_wall_list = [
    [2, 0, 1], 
    [3, 0, 2], 
    [4, 3, 2], 
    [5, 3, 4], 
    [6, 3, 5], 
    [3, 6, 7], 
    [6, 8, 7], 
    [7, 8, 9], 
    [11, 9, 8], 
    [10, 9, 11], 
    [12, 11, 13], 
    [11, 12, 10], 
    [8, 13, 11], 
    [15, 14, 13], 
    [14, 12, 13], 
    [16, 15, 13], 
    [13, 8, 16], 
    [16, 6, 5], 
    [6, 16, 8], 
    [16, 5, 18], 
    [15, 16, 17], 
    [18, 17, 16], 
    [19, 18, 4], 
    [19, 20, 18], 
    [18, 5, 4], 
    [17, 18, 20], 
    [20, 19, 23], 
    [21, 20, 22], 
    [20, 21, 17], 
    [24, 22, 20], 
    [20, 23, 24], 
    [24, 26, 25], 
    [25, 28, 24], 
    [24, 27, 26], 
    [27, 24, 23], 
    [22, 24, 28], 
    [28, 25, 31], 
    [29, 28, 30], 
    [28, 29, 22], 
    [31, 30, 28], 
    [32, 36, 31], 
    [34, 32, 31], 
    [33, 34, 31], 
    [31, 25, 33], 
    [35, 31, 36], 
    [31, 35, 30], 
    [37, 39, 36], 
    [36, 32, 37], 
    [38, 36, 39], 
    [36, 38, 35], 
    [39, 37, 41], 
    [39, 40, 38], 
    [41, 40, 39], 
    [41, 37, 42], 
    [42, 44, 41], 
    [41, 43, 40], 
    [43, 41, 44], 
    [46, 45, 43], 
    [43, 45, 40], 
    [46, 47, 45], 
    [48, 47, 46], 
    [47, 48, 50], 
    [48, 49, 50], 
    [49, 52, 50], 
    [47, 50, 51], 
    [52, 51, 50], 
    [53, 52, 49], 
    [54, 52, 53], 
    [52, 54, 55], 
    [51, 52, 55], 
    [55, 56, 58], 
    [56, 55, 57], 
    [57, 55, 54], 
    [51, 55, 58], 
    [56, 61, 58], 
    [58, 59, 51], 
    [59, 58, 60], 
    [61, 60, 58], 
    [62, 61, 64], 
    [63, 61, 62], 
    [61, 63, 65], 
    [61, 56, 64], 
    [60, 61, 65], 
    [63, 68, 65], 
    [65, 66, 60], 
    [65, 67, 66], 
    [68, 67, 65], 
    [68, 69, 71], 
    [69, 68, 70], 
    [70, 68, 63], 
    [67, 68, 71], 
    [69, 73, 71], 
    [71, 72, 67], 
    [72, 71, 74], 
    [73, 74, 71], 
    [73, 75, 74], 
    [76, 74, 75], 
    [74, 76, 77], 
    [74, 77, 72], 
    [76, 80, 77], 
    [80, 78, 77], 
    [77, 78, 79], 
    [79, 72, 77], 
    [81, 80, 76], 
    [82, 80, 81], 
    [80, 82, 83], 
    [80, 14, 78], 
    [14, 80, 83], 
    [82, 84, 83], 
    [14, 83, 12], 
    [84, 12, 83], 
    [85, 84, 82], 
    [84, 86, 12], 
    [12, 86, 10], 
    [82, 87, 85], 
    [87, 82, 88], 
    [89, 87, 88], 
    [88, 90, 89], 
    [92, 90, 88], 
    [92, 91, 90], 
    [93, 91, 92], 
    [94, 92, 88], 
    [94, 93, 92], 
    [97, 94, 95], 
    [94, 96, 95], 
    [94, 88, 96], 
    [93, 94, 97], 
    [98, 99, 97], 
    [95, 98, 97], 
    [101, 97, 99], 
    [100, 93, 97], 
    [97, 101, 100], 
    [102, 101, 103], 
    [102, 100, 101], 
    [99, 103, 101], 
    [103, 104, 105], 
    [103, 99, 104], 
    [103, 105, 106], 
    [107, 106, 105], 
    [109, 107, 105], 
    [109, 108, 107], 
    [110, 112, 109], 
    [110, 109, 113], 
    [112, 108, 109], 
    [109, 105, 111], 
    [109, 111, 113], 
    [114, 110, 113], 
    [111, 115, 113], 
    [117, 114, 113], 
    [116, 113, 115], 
    [116, 117, 113], 
    [117, 118, 119], 
    [120, 118, 117], 
    [119, 114, 117], 
    [120, 117, 121], 
    [121, 117, 116], 
    [122, 123, 121], 
    [122, 121, 116], 
    [124, 121, 123], 
    [121, 124, 120], 
    [127, 125, 124], 
    [124, 125, 126], 
    [126, 120, 124], 
    [127, 124, 123], 
    [129, 127, 128], 
    [130, 128, 127], 
    [131, 127, 129], 
    [123, 130, 127], 
    [132, 127, 131], 
    [125, 127, 132], 
    [133, 132, 135], 
    [132, 134, 125], 
    [131, 135, 132], 
    [133, 135, 137], 
    [136, 137, 135], 
    [136, 135, 131], 
    [137, 136, 138], 
    [138, 136, 139], 
    [139, 140, 138], 
    [143, 140, 141], 
    [141, 140, 142], 
    [140, 139, 142], 
    [53, 143, 141], 
    [144, 142, 145], 
    [146, 142, 144], 
    [142, 146, 141], 
    [142, 139, 145], 
    [147, 57, 146], 
    [144, 147, 146], 
    [146, 54, 141], 
    [54, 146, 57], 
    [147, 144, 148], 
    [64, 147, 148], 
    [147, 64, 56], 
    [57, 147, 56], 
    [149, 128, 148], 
    [149, 148, 144], 
    [128, 150, 148], 
    [150, 151, 148], 
    [151, 64, 148], 
    [153, 152, 151], 
    [152, 62, 151], 
    [151, 150, 153], 
    [64, 151, 62], 
    [154, 152, 153], 
    [153, 155, 154], 
    [153, 150, 155], 
    [155, 156, 154], 
    [150, 130, 155], 
    [122, 155, 130], 
    [156, 155, 122], 
    [157, 154, 156], 
    [157, 156, 111], 
    [115, 111, 156], 
    [115, 156, 122], 
    [111, 105, 157], 
    [105, 158, 157], 
    [154, 157, 159], 
    [157, 158, 159], 
    [158, 160, 159], 
    [152, 154, 159], 
    [160, 161, 159], 
    [161, 152, 159], 
    [69, 70, 161], 
    [70, 152, 161], 
    [161, 160, 69], 
    [160, 158, 162], 
    [160, 162, 95], 
    [75, 160, 95], 
    [160, 73, 69], 
    [73, 160, 75], 
    [158, 104, 162], 
    [162, 98, 95], 
    [98, 162, 104], 
    [104, 158, 105], 
    [62, 152, 70], 
    [130, 150, 128], 
    [144, 145, 149], 
    [145, 129, 149], 
    [128, 149, 129], 
    [129, 145, 136], 
    [136, 145, 139], 
    [53, 141, 54], 
    [131, 129, 136], 
    [163, 125, 134], 
    [163, 126, 125], 
    [123, 122, 130], 
    [126, 164, 120], 
    [165, 120, 164], 
    [118, 120, 165], 
    [122, 116, 115], 
    [98, 104, 99], 
    [166, 93, 100], 
    [167, 93, 166], 
    [93, 167, 91], 
    [96, 81, 95], 
    [88, 81, 96], 
    [75, 95, 81], 
    [81, 88, 82], 
    [75, 81, 76], 
    [72, 79, 21], 
    [21, 79, 168], 
    [78, 168, 79], 
    [168, 78, 15], 
    [17, 168, 15], 
    [17, 21, 168], 
    [14, 15, 78], 
    [169, 72, 170], 
    [169, 67, 72], 
    [72, 21, 170], 
    [171, 170, 29], 
    [169, 170, 171], 
    [22, 170, 21], 
    [170, 22, 29], 
    [172, 171, 29], 
    [66, 171, 173], 
    [66, 169, 171], 
    [171, 172, 173], 
    [173, 60, 66], 
    [60, 173, 59], 
    [173, 172, 59], 
    [174, 59, 172], 
    [30, 174, 172], 
    [30, 172, 29], 
    [59, 174, 175], 
    [175, 174, 176], 
    [176, 174, 35], 
    [174, 30, 35], 
    [38, 176, 35], 
    [38, 47, 176], 
    [175, 176, 47], 
    [51, 175, 47], 
    [51, 59, 175], 
    [169, 66, 67], 
    [62, 70, 63], 
    [40, 47, 38], 
    [47, 40, 45], 
    [34, 33, 177], 
    [32, 34, 178], 
    [179, 34, 177], 
    [34, 179, 178], 
    [33, 180, 177], 
    [180, 181, 177], 
    [183, 181, 182], 
    [180, 182, 181], 
    [2, 184, 183], 
    [2, 183, 182], 
    [184, 2, 1], 
    [23, 182, 27], 
    [23, 19, 182], 
    [4, 2, 182], 
    [182, 19, 4], 
    [182, 180, 27], 
    [27, 180, 26], 
    [26, 180, 33], 
    [26, 33, 25], 
    [187, 186, 185], 
    [188, 187, 185], 
    [189, 187, 188], 
    [190, 189, 188], 
    [191, 190, 188], 
    [188, 192, 191], 
    [191, 192, 193], 
    [192, 194, 193], 
    [196, 193, 194], 
    [195, 196, 194], 
    [197, 198, 196], 
    [196, 195, 197], 
    [193, 196, 198], 
    [200, 198, 199], 
    [199, 198, 197], 
    [201, 198, 200], 
    [198, 201, 193], 
    [201, 190, 191], 
    [191, 193, 201], 
    [201, 203, 190], 
    [200, 202, 201], 
    [203, 201, 202], 
    [204, 189, 203], 
    [204, 203, 205], 
    [203, 189, 190], 
    [202, 205, 203], 
    [205, 208, 204], 
    [206, 207, 205], 
    [205, 202, 206], 
    [209, 205, 207], 
    [205, 209, 208], 
    [209, 210, 211], 
    [210, 209, 213], 
    [209, 211, 212], 
    [212, 208, 209], 
    [207, 213, 209], 
    [213, 216, 210], 
    [214, 215, 213], 
    [213, 207, 214], 
    [216, 213, 215], 
    [217, 216, 221], 
    [219, 216, 217], 
    [218, 216, 219], 
    [216, 218, 210], 
    [220, 221, 216], 
    [216, 215, 220], 
    [222, 221, 224], 
    [221, 222, 217], 
    [223, 224, 221], 
    [221, 220, 223], 
    [224, 226, 222], 
    [224, 223, 225], 
    [226, 224, 225], 
    [226, 227, 222], 
    [227, 226, 229], 
    [226, 225, 228], 
    [228, 229, 226], 
    [231, 228, 230], 
    [228, 225, 230], 
    [231, 230, 232], 
    [233, 231, 232], 
    [232, 235, 233], 
    [233, 235, 234], 
    [234, 235, 237], 
    [232, 236, 235], 
    [237, 235, 236], 
    [238, 234, 237], 
    [239, 238, 237], 
    [237, 240, 239], 
    [236, 240, 237], 
    [240, 243, 241], 
    [241, 242, 240], 
    [242, 239, 240], 
    [236, 243, 240], 
    [241, 243, 246], 
    [243, 236, 244], 
    [244, 245, 243], 
    [246, 243, 245], 
    [247, 249, 246], 
    [248, 247, 246], 
    [246, 250, 248], 
    [246, 249, 241], 
    [245, 250, 246], 
    [248, 250, 253], 
    [250, 245, 251], 
    [250, 251, 252], 
    [253, 250, 252], 
    [253, 256, 254], 
    [254, 255, 253], 
    [255, 248, 253], 
    [252, 256, 253], 
    [254, 256, 258], 
    [256, 252, 257], 
    [257, 259, 256], 
    [258, 256, 259], 
    [258, 259, 260], 
    [261, 260, 259], 
    [259, 262, 261], 
    [259, 257, 262], 
    [261, 262, 265], 
    [265, 262, 263], 
    [262, 264, 263], 
    [264, 262, 257], 
    [266, 261, 265], 
    [267, 266, 265], 
    [265, 268, 267], 
    [265, 263, 199], 
    [199, 268, 265], 
    [267, 268, 269], 
    [199, 197, 268], 
    [269, 268, 197], 
    [270, 267, 269], 
    [269, 197, 271], 
    [197, 195, 271], 
    [267, 270, 272], 
    [272, 273, 267], 
    [274, 273, 272], 
    [273, 274, 275], 
    [277, 273, 275], 
    [277, 275, 276], 
    [278, 277, 276], 
    [279, 273, 277], 
    [279, 277, 278], 
    [282, 280, 279], 
    [279, 280, 281], 
    [279, 281, 273], 
    [278, 282, 279], 
    [283, 282, 284], 
    [280, 282, 283], 
    [286, 284, 282], 
    [285, 282, 278], 
    [282, 285, 286], 
    [287, 288, 286], 
    [287, 286, 285], 
    [284, 286, 288], 
    [288, 290, 289], 
    [288, 289, 284], 
    [288, 291, 290], 
    [292, 290, 291], 
    [294, 290, 292], 
    [294, 292, 293], 
    [295, 294, 297], 
    [295, 298, 294], 
    [297, 294, 293], 
    [294, 296, 290], 
    [294, 298, 296], 
    [299, 298, 295], 
    [296, 298, 300], 
    [302, 298, 299], 
    [301, 300, 298], 
    [301, 298, 302], 
    [302, 304, 303], 
    [305, 302, 303], 
    [304, 302, 299], 
    [305, 306, 302], 
    [306, 301, 302], 
    [307, 306, 308], 
    [307, 301, 306], 
    [309, 308, 306], 
    [306, 305, 309], 
    [312, 309, 310], 
    [309, 311, 310], 
    [311, 309, 305], 
    [312, 308, 309], 
    [314, 313, 312], 
    [315, 312, 313], 
    [316, 314, 312], 
    [308, 312, 315], 
    [317, 316, 312], 
    [310, 317, 312], 
    [318, 320, 317], 
    [317, 310, 319], 
    [316, 317, 320], 
    [318, 322, 320], 
    [321, 320, 322], 
    [321, 316, 320], 
    [322, 323, 321], 
    [323, 324, 321], 
    [324, 323, 325], 
    [328, 326, 325], 
    [326, 327, 325], 
    [325, 327, 324], 
    [238, 326, 328], 
    [329, 330, 327], 
    [331, 329, 327], 
    [327, 326, 331], 
    [327, 330, 324], 
    [332, 331, 242], 
    [329, 331, 332], 
    [331, 326, 239], 
    [239, 242, 331], 
    [332, 333, 329], 
    [249, 333, 332], 
    [332, 241, 249], 
    [242, 241, 332], 
    [334, 333, 313], 
    [334, 329, 333], 
    [313, 333, 335], 
    [335, 333, 336], 
    [336, 333, 249], 
    [338, 336, 337], 
    [337, 336, 247], 
    [336, 338, 335], 
    [249, 247, 336], 
    [339, 338, 337], 
    [338, 339, 340], 
    [338, 340, 335], 
    [340, 339, 341], 
    [335, 340, 315], 
    [307, 315, 340], 
    [341, 307, 340], 
    [342, 341, 339], 
    [342, 296, 341], 
    [300, 341, 296], 
    [300, 307, 341], 
    [296, 342, 290], 
    [290, 342, 343], 
    [339, 344, 342], 
    [342, 344, 343], 
    [343, 344, 345], 
    [337, 344, 339], 
    [345, 344, 346], 
    [346, 344, 337], 
    [254, 346, 255], 
    [255, 346, 337], 
    [346, 254, 345], 
    [345, 347, 343], 
    [345, 280, 347], 
    [260, 280, 345], 
    [345, 254, 258], 
    [258, 260, 345], 
    [343, 347, 289], 
    [347, 280, 283], 
    [283, 289, 347], 
    [289, 290, 343], 
    [247, 255, 337], 
    [315, 313, 335], 
    [329, 334, 330], 
    [330, 334, 314], 
    [313, 314, 334], 
    [314, 321, 330], 
    [321, 324, 330], 
    [238, 239, 326], 
    [316, 321, 314], 
    [348, 319, 310], 
    [348, 310, 311], 
    [308, 315, 307], 
    [311, 305, 349], 
    [350, 349, 305], 
    [303, 350, 305], 
    [307, 300, 301], 
    [283, 284, 289], 
    [351, 285, 278], 
    [352, 351, 278], 
    [278, 276, 352], 
    [281, 280, 266], 
    [273, 281, 266], 
    [260, 266, 280], 
    [266, 267, 273], 
    [260, 261, 266], 
    [257, 206, 264], 
    [206, 353, 264], 
    [263, 264, 353], 
    [353, 200, 263], 
    [202, 200, 353], 
    [202, 353, 206], 
    [199, 263, 200], 
    [354, 355, 257], 
    [354, 257, 252], 
    [257, 355, 206], 
    [356, 214, 355], 
    [354, 356, 355], 
    [207, 206, 355], 
    [355, 214, 207], 
    [357, 214, 356], 
    [251, 358, 356], 
    [251, 356, 354], 
    [356, 358, 357], 
    [358, 251, 245], 
    [245, 244, 358], 
    [358, 244, 357], 
    [359, 357, 244], 
    [215, 357, 359], 
    [215, 214, 357], 
    [244, 360, 359], 
    [360, 361, 359], 
    [361, 220, 359], 
    [359, 220, 215], 
    [223, 220, 361], 
    [223, 361, 232], 
    [360, 232, 361], 
    [236, 232, 360], 
    [236, 360, 244], 
    [354, 252, 251], 
    [247, 248, 255], 
    [225, 223, 232], 
    [232, 230, 225], 
    [219, 362, 218], 
    [217, 363, 219], 
    [364, 362, 219], 
    [219, 363, 364], 
    [218, 362, 365], 
    [365, 362, 366], 
    [368, 367, 366], 
    [365, 366, 367], 
    [187, 368, 369], 
    [187, 367, 368], 
    [369, 186, 187], 
    [208, 212, 367], 
    [208, 367, 204], 
    [189, 367, 187], 
    [367, 189, 204], 
    [367, 212, 365], 
    [212, 211, 365], 
    [211, 218, 365], 
    [211, 210, 218], 
    [9, 194, 192], 
    [188, 3, 7], 
    [3, 188, 185], 
    [186, 1, 0], 
    [1, 186, 369], 
    [368, 183, 184], 
    [366, 181, 183], 
    [362, 177, 181], 
    [177, 362, 364], 
    [363, 178, 179], 
    [178, 363, 217], 
    [222, 37, 32], 
    [227, 42, 37], 
    [229, 44, 42], 
    [228, 43, 44], 
    [231, 46, 43], 
    [233, 48, 46], 
    [48, 233, 234], 
    [49, 234, 238], 
    [53, 238, 328], 
    [325, 140, 143], 
    [140, 325, 323], 
    [322, 137, 138], 
    [318, 133, 137], 
    [132, 133, 318], 
    [319, 134, 132], 
    [348, 163, 134], 
    [126, 163, 348], 
    [126, 311, 349], 
    [164, 349, 350], 
    [118, 165, 350], 
    [304, 119, 118], 
    [114, 119, 304], 
    [110, 114, 299], 
    [112, 110, 295], 
    [108, 112, 297], 
    [107, 108, 293], 
    [106, 107, 292], 
    [103, 106, 291], 
    [102, 103, 288], 
    [100, 102, 287], 
    [166, 100, 285], 
    [167, 166, 351], 
    [167, 352, 276], 
    [90, 91, 276], 
    [89, 90, 275], 
    [87, 89, 274], 
    [85, 87, 272], 
    [269, 84, 85], 
    [86, 84, 269], 
    [195, 10, 86], 
    [10, 195, 194], 
    [9, 192, 7], 
    [188, 7, 192], 
    [3, 185, 0], 
    [186, 0, 185], 
    [1, 369, 184], 
    [368, 184, 369], 
    [366, 183, 368], 
    [362, 181, 366], 
    [177, 364, 179], 
    [363, 179, 364], 
    [178, 217, 32], 
    [222, 32, 217], 
    [227, 37, 222], 
    [229, 42, 227], 
    [228, 44, 229], 
    [231, 43, 228], 
    [233, 46, 231], 
    [48, 234, 49], 
    [49, 238, 53], 
    [53, 328, 143], 
    [325, 143, 328], 
    [140, 323, 138], 
    [322, 138, 323], 
    [318, 137, 322], 
    [132, 318, 317], 
    [319, 132, 317], 
    [348, 134, 319], 
    [126, 348, 311], 
    [126, 349, 164], 
    [164, 350, 165], 
    [118, 350, 303], 
    [304, 118, 303], 
    [114, 304, 299], 
    [110, 299, 295], 
    [112, 295, 297], 
    [108, 297, 293], 
    [107, 293, 292], 
    [106, 292, 291], 
    [103, 291, 288], 
    [102, 288, 287], 
    [100, 287, 285], 
    [166, 285, 351], 
    [167, 351, 352], 
    [167, 276, 91], 
    [90, 276, 275], 
    [89, 275, 274], 
    [87, 274, 272], 
    [85, 272, 270], 
    [269, 85, 270], 
    [86, 269, 271], 
    [195, 86, 271], 
    [10, 194, 9]
] # synapse_wall_list

synapse = m.GeometryObject(
    name = 'synapse',
    vertex_list = synapse_vertex_list,
    wall_list = synapse_wall_list,
    surface_regions = []
)
# ^^^^ synapse ^^^^


