import mcell as m

# ---- PSD ----
PSD_vertex_list = [
    [3.96557453541391e-09, 0.256407976150513, 1], 
    [0.0500227212905884, 0.251481175422668, 1], 
    [0.0981230884790421, 0.236890107393265, 1], 
    [0.142452642321587, 0.213195443153381, 1], 
    [0.181307837367058, 0.181307822465897, 1], 
    [0.213195443153381, 0.142452642321587, 1], 
    [0.236890107393265, 0.0981230810284615, 1], 
    [0.251481175422668, 0.0500227212905884, 1], 
    [0.256408005952835, -5.76810865737798e-09, 1], 
    [0.251481175422668, -0.0500227138400078, 1], 
    [0.236890107393265, -0.0981230810284615, 1], 
    [0.213195458054543, -0.142452642321587, 1], 
    [0.181307822465897, -0.181307837367058, 1], 
    [0.142452642321587, -0.213195458054543, 1], 
    [0.0981230959296227, -0.236890107393265, 1], 
    [0.0500227138400078, -0.251481175422668, 1], 
    [-1.24975692017415e-08, -0.256408005952835, 1], 
    [-0.0500227063894272, -0.251481175422668, 1], 
    [-0.0981230884790421, -0.236890107393265, 1], 
    [-0.142452657222748, -0.21319542825222, 1], 
    [-0.181307807564735, -0.181307837367058, 1], 
    [-0.21319542825222, -0.14245268702507, 1], 
    [-0.236890092492104, -0.098123125731945, 1], 
    [-0.251481175422668, -0.0500227324664593, 1], 
    [-0.256408005952835, 2.88405432868899e-09, 1], 
    [-0.251481175422668, 0.0500227361917496, 1], 
    [-0.236890092492104, 0.0981231108307838, 1], 
    [-0.213195443153381, 0.142452612519264, 1], 
    [-0.181307852268219, 0.181307807564735, 1], 
    [-0.142452657222748, 0.213195443153381, 1], 
    [-0.0981230884790421, 0.236890107393265, 1], 
    [-0.0500226989388466, 0.251481175422668, 1], 
    [0.00314649799838662, 0.256388604640961, 1], 
    [0.00629251915961504, 0.256330549716949, 1], 
    [0.00943759642541409, 0.256233870983124, 1], 
    [0.0125812562182546, 0.256098568439484, 1], 
    [0.0157230254262686, 0.255924701690674, 1], 
    [0.0188624337315559, 0.255712360143661, 1], 
    [0.0219990089535713, 0.255461513996124, 1], 
    [0.025132279843092, 0.255172312259674, 1], 
    [0.0282617714256048, 0.254844695329666, 1], 
    [0.0313870087265968, 0.25447878241539, 1], 
    [0.0345075242221355, 0.254074603319168, 1], 
    [0.0376228466629982, 0.253632187843323, 1], 
    [0.0407324992120266, 0.253151595592499, 1], 
    [0.0438360013067722, 0.252632826566696, 1], 
    [0.0469329059123993, 0.252076029777527, 1], 
    [0.0531049743294716, 0.250848323106766, 1], 
    [0.0561792217195034, 0.250177621841431, 1], 
    [0.0592450015246868, 0.249469220638275, 1], 
    [0.0623018592596054, 0.248723194003105, 1], 
    [0.0653493478894234, 0.247939765453339, 1], 
    [0.0683870017528534, 0.247119039297104, 1], 
    [0.0714143812656403, 0.246261104941368, 1], 
    [0.0744310170412064, 0.245366171002388, 1], 
    [0.0774364694952965, 0.244434326887131, 1], 
    [0.0804302766919136, 0.243465766310692, 1], 
    [0.0834119766950607, 0.242460548877716, 1], 
    [0.0863811150193214, 0.241418838500977, 1], 
    [0.0893372595310211, 0.24034084379673, 1], 
    [0.0922799408435822, 0.239226594567299, 1], 
    [0.0952087044715881, 0.238076284527779, 1], 
    [0.101022653281689, 0.235668063163757, 1], 
    [0.103906996548176, 0.234410524368286, 1], 
    [0.106775663793087, 0.233117610216141, 1], 
    [0.109628245234489, 0.231789574027061, 1], 
    [0.112464338541031, 0.230426669120789, 1], 
    [0.115283511579037, 0.229029059410095, 1], 
    [0.118085339665413, 0.227597013115883, 1], 
    [0.120869427919388, 0.226130783557892, 1], 
    [0.123635314404964, 0.224630504846573, 1], 
    [0.126382634043694, 0.223096445202827, 1], 
    [0.12911094725132, 0.221528872847557, 1], 
    [0.131819814443588, 0.219927936792374, 1], 
    [0.134508848190308, 0.21829392015934, 1], 
    [0.137177601456642, 0.216627016663551, 1], 
    [0.139825657010078, 0.214927420020103, 1], 
    [0.14505809545517, 0.211431220173836, 1], 
    [0.14764167368412, 0.209635138511658, 1], 
    [0.150202989578247, 0.207807421684265, 1], 
    [0.152741670608521, 0.205948397517204, 1], 
    [0.155257359147072, 0.20405837893486, 1], 
    [0.160218343138695, 0.200186505913734, 1], 
    [0.162662878632545, 0.198205292224884, 1], 
    [0.165082931518555, 0.196194216609001, 1], 
    [0.167478203773499, 0.194153696298599, 1], 
    [0.169848248362541, 0.192083939909935, 1], 
    [0.172192737460136, 0.189985305070877, 1], 
    [0.174511328339577, 0.187858104705811, 1], 
    [0.176803603768349, 0.185702547430992, 1], 
    [0.179069206118584, 0.183519035577774, 1], 
    [0.183519035577774, 0.179069206118584, 1], 
    [0.185702547430992, 0.176803603768349, 1], 
    [0.187858089804649, 0.174511328339577, 1], 
    [0.189985319972038, 0.172192752361298, 1], 
    [0.192083954811096, 0.169848248362541, 1], 
    [0.19415371119976, 0.167478188872337, 1], 
    [0.196194231510162, 0.165082931518555, 1], 
    [0.198205277323723, 0.162662878632545, 1], 
    [0.200186520814896, 0.160218343138695, 1], 
    [0.202137663960457, 0.157749712467194, 1], 
    [0.204058364033699, 0.155257359147072, 1], 
    [0.205948412418365, 0.152741670608521, 1], 
    [0.207807421684265, 0.150202989578247, 1], 
    [0.209635138511658, 0.14764167368412, 1], 
    [0.211431235074997, 0.14505809545517, 1], 
    [0.214927434921265, 0.139825657010078, 1], 
    [0.21662700176239, 0.137177586555481, 1], 
    [0.21829392015934, 0.134508848190308, 1], 
    [0.219927936792374, 0.131819814443588, 1], 
    [0.221528872847557, 0.12911094725132, 1], 
    [0.223096460103989, 0.126382634043694, 1], 
    [0.224630489945412, 0.123635314404964, 1], 
    [0.226130768656731, 0.120869420468807, 1], 
    [0.227597013115883, 0.118085332214832, 1], 
    [0.229029059410095, 0.115283504128456, 1], 
    [0.230426669120789, 0.112464338541031, 1], 
    [0.231789574027061, 0.109628245234489, 1], 
    [0.233117610216141, 0.106775656342506, 1], 
    [0.234410524368286, 0.103906996548176, 1], 
    [0.235668048262596, 0.101022653281689, 1], 
    [0.238076284527779, 0.0952086970210075, 1], 
    [0.239226579666138, 0.0922799408435822, 1], 
    [0.24034084379673, 0.0893372595310211, 1], 
    [0.241418853402138, 0.0863811075687408, 1], 
    [0.242460533976555, 0.0834119766950607, 1], 
    [0.243465751409531, 0.080430269241333, 1], 
    [0.244434341788292, 0.0774364620447159, 1], 
    [0.245366156101227, 0.0744310170412064, 1], 
    [0.246261104941368, 0.0714143812656403, 1], 
    [0.247119039297104, 0.0683870017528534, 1], 
    [0.2479397803545, 0.0653493478894234, 1], 
    [0.248723194003105, 0.0623018629848957, 1], 
    [0.249469205737114, 0.0592450052499771, 1], 
    [0.250177651643753, 0.0561792254447937, 1], 
    [0.250848323106766, 0.0531049743294716, 1], 
    [0.252076029777527, 0.046932902187109, 1], 
    [0.252632856369019, 0.0438360050320625, 1], 
    [0.253151595592499, 0.0407324954867363, 1], 
    [0.253632158041, 0.0376228392124176, 1], 
    [0.254074603319168, 0.0345075242221355, 1], 
    [0.254478812217712, 0.0313870087265968, 1], 
    [0.254844725131989, 0.0282617639750242, 1], 
    [0.255172312259674, 0.0251322779804468, 1], 
    [0.255461543798447, 0.0219990089535713, 1], 
    [0.255712360143661, 0.0188624318689108, 1], 
    [0.255924701690674, 0.0157230217009783, 1], 
    [0.256098538637161, 0.0125812506303191, 1], 
    [0.256233870983124, 0.00943758990615606, 1], 
    [0.256330579519272, 0.00629250938072801, 1], 
    [0.256388604640961, 0.00314648845233023, 1], 
    [0.256388604640961, -0.00314650125801563, 1], 
    [0.256330579519272, -0.00629252195358276, 1], 
    [0.256233870983124, -0.00943760015070438, 1], 
    [0.256098538637161, -0.0125812608748674, 1], 
    [0.255924701690674, -0.015723031014204, 1], 
    [0.255712360143661, -0.0188624393194914, 1], 
    [0.255461513996124, -0.0219990182667971, 1], 
    [0.255172312259674, -0.0251322835683823, 1], 
    [0.254844725131989, -0.0282617714256048, 1], 
    [0.254478812217712, -0.0313870124518871, 1], 
    [0.254074603319168, -0.0345075242221355, 1], 
    [0.253632158041, -0.0376228429377079, 1], 
    [0.253151595592499, -0.0407324992120266, 1], 
    [0.252632856369019, -0.0438360124826431, 1], 
    [0.252075999975204, -0.046932902187109, 1], 
    [0.250848323106766, -0.0531049706041813, 1], 
    [0.250177621841431, -0.0561792217195034, 1], 
    [0.249469220638275, -0.0592450015246868, 1], 
    [0.248723194003105, -0.0623018555343151, 1], 
    [0.247939765453339, -0.0653493404388428, 1], 
    [0.247119054198265, -0.0683870017528534, 1], 
    [0.246261119842529, -0.0714143738150597, 1], 
    [0.245366185903549, -0.0744310095906258, 1], 
    [0.244434326887131, -0.0774364620447159, 1], 
    [0.243465766310692, -0.0804302617907524, 1], 
    [0.242460548877716, -0.0834119692444801, 1], 
    [0.241418853402138, -0.0863811001181602, 1], 
    [0.24034084379673, -0.0893372446298599, 1], 
    [0.23922660946846, -0.092279925942421, 1], 
    [0.23807629942894, -0.0952086746692657, 1], 
    [0.235668078064919, -0.101022630929947, 1], 
    [0.234410554170609, -0.103906981647015, 1], 
    [0.233117625117302, -0.106775648891926, 1], 
    [0.23042668402195, -0.11246432363987, 1], 
    [0.229029089212418, -0.115283489227295, 1], 
    [0.227597028017044, -0.118085324764252, 1], 
    [0.226130783557892, -0.120869413018227, 1], 
    [0.224630519747734, -0.123635299503803, 1], 
    [0.22309647500515, -0.126382634043694, 1], 
    [0.221528872847557, -0.129110932350159, 1], 
    [0.219927936792374, -0.131819784641266, 1], 
    [0.218293935060501, -0.134508833289146, 1], 
    [0.216627031564713, -0.13717757165432, 1], 
    [0.214927449822426, -0.139825657010078, 1], 
    [0.211431249976158, -0.14505809545517, 1], 
    [0.209635153412819, -0.147641658782959, 1], 
    [0.207807436585426, -0.150202974677086, 1], 
    [0.205948397517204, -0.152741640806198, 1], 
    [0.20405837893486, -0.155257359147072, 1], 
    [0.202137663960457, -0.157749697566032, 1], 
    [0.200186520814896, -0.160218343138695, 1], 
    [0.198205292224884, -0.162662863731384, 1], 
    [0.196194216609001, -0.165082931518555, 1], 
    [0.194153696298599, -0.167478188872337, 1], 
    [0.192083954811096, -0.169848248362541, 1], 
    [0.189985319972038, -0.172192752361298, 1], 
    [0.187858104705811, -0.174511313438416, 1], 
    [0.185702562332153, -0.176803588867188, 1], 
    [0.183519035577774, -0.179069206118584, 1], 
    [0.179069206118584, -0.183519035577774, 1], 
    [0.176803603768349, -0.185702547430992, 1], 
    [0.174511328339577, -0.187858089804649, 1], 
    [0.172192737460136, -0.189985334873199, 1], 
    [0.169848248362541, -0.192083969712257, 1], 
    [0.167478173971176, -0.19415371119976, 1], 
    [0.165082916617393, -0.196194246411324, 1], 
    [0.162662863731384, -0.198205277323723, 1], 
    [0.160218343138695, -0.200186535716057, 1], 
    [0.157749697566032, -0.202137663960457, 1], 
    [0.155257344245911, -0.20405837893486, 1], 
    [0.152741655707359, -0.205948412418365, 1], 
    [0.150202974677086, -0.207807436585426, 1], 
    [0.147641658782959, -0.209635153412819, 1], 
    [0.14505809545517, -0.211431235074997, 1], 
    [0.139825642108917, -0.214927449822426, 1], 
    [0.13717757165432, -0.216627016663551, 1], 
    [0.134508833289146, -0.218293935060501, 1], 
    [0.131819799542427, -0.219927936792374, 1], 
    [0.12911094725132, -0.221528872847557, 1], 
    [0.126382634043694, -0.22309647500515, 1], 
    [0.123635314404964, -0.224630504846573, 1], 
    [0.120869420468807, -0.226130768656731, 1], 
    [0.118085339665413, -0.227597028017044, 1], 
    [0.115283504128456, -0.229029059410095, 1], 
    [0.112464338541031, -0.23042668402195, 1], 
    [0.109628245234489, -0.231789574027061, 1], 
    [0.106775656342506, -0.233117610216141, 1], 
    [0.103906996548176, -0.234410524368286, 1], 
    [0.101022653281689, -0.235668063163757, 1], 
    [0.0952086970210075, -0.238076284527779, 1], 
    [0.0922799408435822, -0.239226594567299, 1], 
    [0.0893372669816017, -0.24034084379673, 1], 
    [0.0863811150193214, -0.241418853402138, 1], 
    [0.0834119766950607, -0.242460548877716, 1], 
    [0.0804302766919136, -0.243465766310692, 1], 
    [0.0774364694952965, -0.244434341788292, 1], 
    [0.074431024491787, -0.245366171002388, 1], 
    [0.0714143812656403, -0.246261104941368, 1], 
    [0.068387009203434, -0.247119039297104, 1], 
    [0.0653493478894234, -0.2479397803545, 1], 
    [0.0623018592596054, -0.248723208904266, 1], 
    [0.0592450015246868, -0.249469235539436, 1], 
    [0.0561792142689228, -0.250177651643753, 1], 
    [0.053104966878891, -0.250848323106766, 1], 
    [0.0469328947365284, -0.252076029777527, 1], 
    [0.0438359975814819, -0.252632856369019, 1], 
    [0.0407324843108654, -0.253151595592499, 1], 
    [0.0376228354871273, -0.253632187843323, 1], 
    [0.0345075130462646, -0.25407463312149, 1], 
    [0.0313869975507259, -0.254478812217712, 1], 
    [0.0282617565244436, -0.254844725131989, 1], 
    [0.0251322668045759, -0.255172312259674, 1], 
    [0.0219989996403456, -0.255461543798447, 1], 
    [0.018862422555685, -0.255712360143661, 1], 
    [0.0157230105251074, -0.255924701690674, 1], 
    [0.0125812413170934, -0.256098538637161, 1], 
    [0.00943758059293032, -0.256233870983124, 1], 
    [0.00629250193014741, -0.256330579519272, 1], 
    [0.00314648123458028, -0.256388604640961, 1], 
    [-0.00314650661312044, -0.256388604640961, 1], 
    [-0.00629252754151821, -0.256330579519272, 1], 
    [-0.00943760480731726, -0.256233870983124, 1], 
    [-0.01258126180619, -0.256098538637161, 1], 
    [-0.015723031014204, -0.255924731492996, 1], 
    [-0.0188624393194914, -0.255712389945984, 1], 
    [-0.0219990145415068, -0.255461543798447, 1], 
    [-0.025132279843092, -0.255172312259674, 1], 
    [-0.0282617677003145, -0.254844725131989, 1], 
    [-0.0313870087265968, -0.254478812217712, 1], 
    [-0.0345075204968452, -0.254074603319168, 1], 
    [-0.0376228354871273, -0.253632187843323, 1], 
    [-0.0407324880361557, -0.253151595592499, 1], 
    [-0.0438360013067722, -0.252632856369019, 1], 
    [-0.0469328947365284, -0.252075999975204, 1], 
    [-0.0531049631536007, -0.250848323106766, 1], 
    [-0.0561792142689228, -0.250177651643753, 1], 
    [-0.0592449903488159, -0.249469235539436, 1], 
    [-0.0623018480837345, -0.248723194003105, 1], 
    [-0.0653493329882622, -0.247939795255661, 1], 
    [-0.0683869868516922, -0.247119039297104, 1], 
    [-0.0714143663644791, -0.246261104941368, 1], 
    [-0.0744310095906258, -0.245366185903549, 1], 
    [-0.0774364545941353, -0.244434326887131, 1], 
    [-0.0804302617907524, -0.243465766310692, 1], 
    [-0.0834119543433189, -0.242460548877716, 1], 
    [-0.0863811001181602, -0.241418838500977, 1], 
    [-0.0893372520804405, -0.24034084379673, 1], 
    [-0.0922799333930016, -0.239226594567299, 1], 
    [-0.0952086895704269, -0.238076284527779, 1], 
    [-0.101022645831108, -0.235668063163757, 1], 
    [-0.103906996548176, -0.234410524368286, 1], 
    [-0.106775656342506, -0.23311759531498, 1], 
    [-0.109628245234489, -0.2317895591259, 1], 
    [-0.112464338541031, -0.230426669120789, 1], 
    [-0.115283496677876, -0.229029059410095, 1], 
    [-0.118085339665413, -0.227596998214722, 1], 
    [-0.120869420468807, -0.226130768656731, 1], 
    [-0.123635321855545, -0.224630489945412, 1], 
    [-0.126382634043694, -0.223096445202827, 1], 
    [-0.12911094725132, -0.221528857946396, 1], 
    [-0.131819814443588, -0.219927906990051, 1], 
    [-0.134508848190308, -0.21829392015934, 1], 
    [-0.137177601456642, -0.21662700176239, 1], 
    [-0.13982567191124, -0.214927420020103, 1], 
    [-0.145058110356331, -0.211431220173836, 1], 
    [-0.14764167368412, -0.209635123610497, 1], 
    [-0.150202989578247, -0.207807421684265, 1], 
    [-0.152741670608521, -0.205948382616043, 1], 
    [-0.155257359147072, -0.20405837893486, 1], 
    [-0.157749712467194, -0.202137634158134, 1], 
    [-0.160218343138695, -0.200186491012573, 1], 
    [-0.162662878632545, -0.198205292224884, 1], 
    [-0.165082916617393, -0.196194216609001, 1], 
    [-0.167478188872337, -0.194153696298599, 1], 
    [-0.169848248362541, -0.192083969712257, 1], 
    [-0.172192722558975, -0.189985319972038, 1], 
    [-0.174511313438416, -0.187858104705811, 1], 
    [-0.176803588867188, -0.185702562332153, 1], 
    [-0.179069191217422, -0.183519035577774, 1], 
    [-0.183519020676613, -0.179069221019745, 1], 
    [-0.185702547430992, -0.176803603768349, 1], 
    [-0.187858074903488, -0.174511343240738, 1], 
    [-0.189985305070877, -0.172192767262459, 1], 
    [-0.192083954811096, -0.169848278164864, 1], 
    [-0.194153681397438, -0.167478203773499, 1], 
    [-0.196194216609001, -0.165082961320877, 1], 
    [-0.1982052475214, -0.162662908434868, 1], 
    [-0.200186505913734, -0.160218372941017, 1], 
    [-0.202137634158134, -0.157749727368355, 1], 
    [-0.204058349132538, -0.155257418751717, 1], 
    [-0.205948367714882, -0.152741700410843, 1], 
    [-0.207807406783104, -0.150203019380569, 1], 
    [-0.209635123610497, -0.147641703486443, 1], 
    [-0.211431205272675, -0.145058140158653, 1], 
    [-0.214927420020103, -0.139825686812401, 1], 
    [-0.216626986861229, -0.137177631258965, 1], 
    [-0.218293905258179, -0.13450887799263, 1], 
    [-0.219927906990051, -0.131819844245911, 1], 
    [-0.221528843045235, -0.129110977053642, 1], 
    [-0.223096430301666, -0.126382678747177, 1], 
    [-0.22463047504425, -0.123635359108448, 1], 
    [-0.226130738854408, -0.12086945772171, 1], 
    [-0.227597013115883, -0.118085376918316, 1], 
    [-0.229029044508934, -0.115283533930779, 1], 
    [-0.230426654219627, -0.112464368343353, 1], 
    [-0.231789574027061, -0.109628275036812, 1], 
    [-0.233117610216141, -0.106775686144829, 1], 
    [-0.234410524368286, -0.103907026350498, 1], 
    [-0.235668048262596, -0.101022683084011, 1], 
    [-0.238076284527779, -0.0952087268233299, 1], 
    [-0.239226579666138, -0.0922799706459045, 1], 
    [-0.240340813994408, -0.0893372818827629, 1], 
    [-0.241418853402138, -0.0863811448216438, 1], 
    [-0.242460533976555, -0.0834119990468025, 1], 
    [-0.243465751409531, -0.0804302990436554, 1], 
    [-0.244434341788292, -0.0774364918470383, 1], 
    [-0.245366156101227, -0.0744310468435287, 1], 
    [-0.246261104941368, -0.0714143961668015, 1], 
    [-0.247119039297104, -0.0683870241045952, 1], 
    [-0.2479397803545, -0.0653493702411652, 1], 
    [-0.248723194003105, -0.0623018816113472, 1], 
    [-0.249469205737114, -0.0592450201511383, 1], 
    [-0.250177651643753, -0.0561792366206646, 1], 
    [-0.250848323106766, -0.0531049892306328, 1], 
    [-0.252076029777527, -0.0469329170882702, 1], 
    [-0.252632856369019, -0.0438360199332237, 1], 
    [-0.253151595592499, -0.0407325066626072, 1], 
    [-0.253632158041, -0.0376228503882885, 1], 
    [-0.254074603319168, -0.0345075353980064, 1], 
    [-0.254478812217712, -0.0313870161771774, 1], 
    [-0.254844725131989, -0.02826177328825, 1], 
    [-0.255172312259674, -0.0251322854310274, 1], 
    [-0.255461543798447, -0.0219990145415068, 1], 
    [-0.255712360143661, -0.0188624374568462, 1], 
    [-0.255924701690674, -0.0157230272889137, 1], 
    [-0.256098538637161, -0.0125812562182546, 1], 
    [-0.256233870983124, -0.00943759456276894, 1], 
    [-0.256330579519272, -0.00629251450300217, 1], 
    [-0.256388604640961, -0.00314649264328182, 1], 
    [-0.256388604640961, 0.00314649846404791, 1], 
    [-0.256330579519272, 0.00629252148792148, 1], 
    [-0.256233870983124, 0.00943760015070438, 1], 
    [-0.256098538637161, 0.01258126180619, 1], 
    [-0.255924701690674, 0.0157230347394943, 1], 
    [-0.255712360143661, 0.0188624449074268, 1], 
    [-0.255461513996124, 0.0219990219920874, 1], 
    [-0.255172312259674, 0.0251322910189629, 1], 
    [-0.254844725131989, 0.0282617826014757, 1], 
    [-0.254478812217712, 0.0313870273530483, 1], 
    [-0.254074603319168, 0.0345075391232967, 1], 
    [-0.253632158041, 0.0376228578388691, 1], 
    [-0.253151595592499, 0.0407325141131878, 1], 
    [-0.252632856369019, 0.0438360273838043, 1], 
    [-0.252075999975204, 0.0469329208135605, 1], 
    [-0.250848323106766, 0.0531049966812134, 1], 
    [-0.250177621841431, 0.0561792477965355, 1], 
    [-0.249469220638275, 0.0592450238764286, 1], 
    [-0.248723194003105, 0.0623018853366375, 1], 
    [-0.247939765453339, 0.0653493702411652, 1], 
    [-0.247119024395943, 0.0683870315551758, 1], 
    [-0.246261119842529, 0.0714144185185432, 1], 
    [-0.245366171002388, 0.0744310542941093, 1], 
    [-0.244434326887131, 0.0774364918470383, 1], 
    [-0.243465766310692, 0.0804302915930748, 1], 
    [-0.242460533976555, 0.0834120064973831, 1], 
    [-0.241418853402138, 0.0863811448216438, 1], 
    [-0.240340813994408, 0.0893372893333435, 1], 
    [-0.239226579666138, 0.0922799631953239, 1], 
    [-0.238076284527779, 0.0952087193727493, 1], 
    [-0.235668063163757, 0.10102267563343, 1], 
    [-0.234410524368286, 0.103907011449337, 1], 
    [-0.23311759531498, 0.106775663793087, 1], 
    [-0.2317895591259, 0.10962825268507, 1], 
    [-0.230426669120789, 0.112464338541031, 1], 
    [-0.229029059410095, 0.115283511579037, 1], 
    [-0.227597013115883, 0.118085339665413, 1], 
    [-0.226130783557892, 0.120869413018227, 1], 
    [-0.224630519747734, 0.123635306954384, 1], 
    [-0.223096460103989, 0.126382634043694, 1], 
    [-0.221528872847557, 0.129110932350159, 1], 
    [-0.219927936792374, 0.131819784641266, 1], 
    [-0.218293935060501, 0.134508818387985, 1], 
    [-0.216627016663551, 0.13717757165432, 1], 
    [-0.214927434921265, 0.139825627207756, 1], 
    [-0.211431235074997, 0.145058050751686, 1], 
    [-0.209635153412819, 0.147641628980637, 1], 
    [-0.207807451486588, 0.150202959775925, 1], 
    [-0.205948427319527, 0.152741625905037, 1], 
    [-0.204058408737183, 0.155257329344749, 1], 
    [-0.202137678861618, 0.157749682664871, 1], 
    [-0.200186520814896, 0.160218313336372, 1], 
    [-0.198205322027206, 0.162662833929062, 1], 
    [-0.196194246411324, 0.165082901716232, 1], 
    [-0.194153726100922, 0.167478159070015, 1], 
    [-0.192083984613419, 0.169848218560219, 1], 
    [-0.189985334873199, 0.172192692756653, 1], 
    [-0.187858119606972, 0.174511283636093, 1], 
    [-0.185702577233315, 0.176803573966026, 1], 
    [-0.183519050478935, 0.179069176316261, 1], 
    [-0.179069221019745, 0.183519005775452, 1], 
    [-0.17680361866951, 0.185702532529831, 1], 
    [-0.174511343240738, 0.187858074903488, 1], 
    [-0.172192767262459, 0.189985290169716, 1], 
    [-0.169848278164864, 0.192083939909935, 1], 
    [-0.167478203773499, 0.194153681397438, 1], 
    [-0.165082946419716, 0.196194216609001, 1], 
    [-0.162662893533707, 0.198205262422562, 1], 
    [-0.160218358039856, 0.200186505913734, 1], 
    [-0.157749727368355, 0.202137634158134, 1], 
    [-0.155257374048233, 0.204058364033699, 1], 
    [-0.152741685509682, 0.205948397517204, 1], 
    [-0.150203004479408, 0.207807421684265, 1], 
    [-0.147641688585281, 0.209635123610497, 1], 
    [-0.145058125257492, 0.211431235074997, 1], 
    [-0.13982567191124, 0.214927434921265, 1], 
    [-0.137177601456642, 0.21662700176239, 1], 
    [-0.134508848190308, 0.21829392015934, 1], 
    [-0.131819814443588, 0.219927936792374, 1], 
    [-0.12911094725132, 0.221528872847557, 1], 
    [-0.126382648944855, 0.223096460103989, 1], 
    [-0.123635321855545, 0.224630504846573, 1], 
    [-0.120869427919388, 0.226130768656731, 1], 
    [-0.118085332214832, 0.227597042918205, 1], 
    [-0.115283504128456, 0.229029074311256, 1], 
    [-0.11246433109045, 0.230426669120789, 1], 
    [-0.109628245234489, 0.231789574027061, 1], 
    [-0.106775656342506, 0.233117625117302, 1], 
    [-0.103906996548176, 0.234410539269447, 1], 
    [-0.101022653281689, 0.235668078064919, 1], 
    [-0.0952086895704269, 0.23807629942894, 1], 
    [-0.0922799333930016, 0.23922660946846, 1], 
    [-0.0893372520804405, 0.24034084379673, 1], 
    [-0.0863811001181602, 0.241418853402138, 1], 
    [-0.0834119543433189, 0.242460548877716, 1], 
    [-0.0804302543401718, 0.243465781211853, 1], 
    [-0.0774364471435547, 0.244434356689453, 1], 
    [-0.0744310021400452, 0.245366185903549, 1], 
    [-0.0714143663644791, 0.246261119842529, 1], 
    [-0.0683869868516922, 0.247119054198265, 1], 
    [-0.0653493329882622, 0.2479397803545, 1], 
    [-0.0623018443584442, 0.248723208904266, 1], 
    [-0.0592449866235256, 0.249469235539436, 1], 
    [-0.0561792030930519, 0.250177681446075, 1], 
    [-0.0531049519777298, 0.250848323106766, 1], 
    [-0.0469328872859478, 0.252076029777527, 1], 
    [-0.043835986405611, 0.252632856369019, 1], 
    [-0.0407324805855751, 0.253151625394821, 1], 
    [-0.0376228280365467, 0.253632187843323, 1], 
    [-0.0345075093209743, 0.25407463312149, 1], 
    [-0.0313869938254356, 0.25447878241539, 1], 
    [-0.0282617565244436, 0.254844725131989, 1], 
    [-0.0251322686672211, 0.255172342061996, 1], 
    [-0.0219989977777004, 0.255461543798447, 1], 
    [-0.0188624262809753, 0.255712360143661, 1], 
    [-0.0157230161130428, 0.255924731492996, 1], 
    [-0.0125812469050288, 0.256098568439484, 1], 
    [-0.00943758711218834, 0.256233870983124, 1], 
    [-0.00629251077771187, 0.256330579519272, 1], 
    [-0.00314648984931409, 0.256388634443283, 1]
] # PSD_vertex_list

PSD_wall_list = [
    [269, 509, 389], 
    [509, 32, 0], 
    [32, 509, 33], 
    [33, 509, 34], 
    [34, 36, 35], 
    [36, 38, 37], 
    [38, 40, 39], 
    [40, 42, 41], 
    [42, 46, 43], 
    [43, 46, 44], 
    [44, 46, 45], 
    [46, 47, 1], 
    [47, 46, 48], 
    [48, 46, 49], 
    [49, 51, 50], 
    [51, 53, 52], 
    [53, 55, 54], 
    [55, 57, 56], 
    [57, 61, 58], 
    [58, 61, 59], 
    [59, 61, 60], 
    [61, 62, 2], 
    [62, 64, 63], 
    [64, 66, 65], 
    [66, 68, 67], 
    [68, 70, 69], 
    [70, 72, 71], 
    [72, 76, 73], 
    [73, 76, 74], 
    [74, 76, 75], 
    [76, 77, 3], 
    [77, 79, 78], 
    [79, 81, 80], 
    [82, 84, 83], 
    [84, 86, 85], 
    [86, 90, 87], 
    [87, 90, 88], 
    [88, 90, 89], 
    [90, 91, 4], 
    [91, 90, 92], 
    [92, 90, 93], 
    [93, 95, 94], 
    [95, 97, 96], 
    [97, 99, 98], 
    [99, 101, 100], 
    [101, 105, 102], 
    [102, 105, 103], 
    [103, 105, 104], 
    [105, 106, 5], 
    [106, 105, 107], 
    [107, 105, 108], 
    [108, 110, 109], 
    [110, 112, 111], 
    [112, 114, 113], 
    [114, 116, 115], 
    [116, 120, 117], 
    [117, 120, 118], 
    [118, 120, 119], 
    [120, 121, 6], 
    [121, 120, 122], 
    [122, 120, 123], 
    [123, 125, 124], 
    [125, 127, 126], 
    [127, 129, 128], 
    [129, 131, 130], 
    [131, 135, 132], 
    [132, 135, 133], 
    [133, 135, 134], 
    [135, 136, 7], 
    [136, 135, 137], 
    [137, 135, 138], 
    [138, 140, 139], 
    [140, 142, 141], 
    [142, 144, 143], 
    [144, 146, 145], 
    [146, 150, 147], 
    [147, 150, 148], 
    [148, 150, 149], 
    [150, 151, 8], 
    [151, 150, 152], 
    [152, 150, 153], 
    [153, 155, 154], 
    [155, 157, 156], 
    [157, 159, 158], 
    [159, 161, 160], 
    [161, 165, 162], 
    [162, 165, 163], 
    [163, 165, 164], 
    [165, 166, 9], 
    [166, 165, 167], 
    [167, 165, 168], 
    [168, 170, 169], 
    [170, 172, 171], 
    [172, 174, 173], 
    [174, 176, 175], 
    [176, 180, 177], 
    [177, 180, 178], 
    [178, 180, 179], 
    [180, 181, 10], 
    [181, 183, 182], 
    [184, 186, 185], 
    [186, 188, 187], 
    [188, 190, 189], 
    [190, 194, 191], 
    [191, 194, 192], 
    [192, 194, 193], 
    [194, 195, 11], 
    [195, 194, 196], 
    [196, 194, 197], 
    [197, 199, 198], 
    [199, 201, 200], 
    [201, 203, 202], 
    [203, 205, 204], 
    [205, 209, 206], 
    [206, 209, 207], 
    [207, 209, 208], 
    [209, 210, 12], 
    [210, 209, 211], 
    [211, 209, 212], 
    [212, 214, 213], 
    [214, 216, 215], 
    [216, 218, 217], 
    [218, 220, 219], 
    [220, 224, 221], 
    [221, 224, 222], 
    [222, 224, 223], 
    [224, 225, 13], 
    [225, 224, 226], 
    [226, 224, 227], 
    [227, 229, 228], 
    [229, 231, 230], 
    [231, 233, 232], 
    [233, 235, 234], 
    [235, 239, 236], 
    [236, 239, 237], 
    [237, 239, 238], 
    [239, 240, 14], 
    [240, 239, 241], 
    [241, 239, 242], 
    [242, 244, 243], 
    [244, 246, 245], 
    [246, 248, 247], 
    [248, 250, 249], 
    [250, 254, 251], 
    [251, 254, 252], 
    [252, 254, 253], 
    [254, 255, 15], 
    [255, 254, 256], 
    [256, 254, 257], 
    [257, 259, 258], 
    [259, 261, 260], 
    [261, 263, 262], 
    [263, 265, 264], 
    [265, 269, 266], 
    [266, 269, 267], 
    [267, 269, 268], 
    [269, 270, 16], 
    [270, 272, 271], 
    [272, 274, 273], 
    [274, 276, 275], 
    [276, 278, 277], 
    [278, 280, 279], 
    [280, 284, 281], 
    [281, 284, 282], 
    [282, 284, 283], 
    [284, 285, 17], 
    [285, 284, 286], 
    [286, 284, 287], 
    [287, 289, 288], 
    [289, 291, 290], 
    [291, 293, 292], 
    [293, 295, 294], 
    [295, 299, 296], 
    [296, 299, 297], 
    [297, 299, 298], 
    [299, 300, 18], 
    [300, 302, 301], 
    [302, 304, 303], 
    [304, 306, 305], 
    [306, 308, 307], 
    [308, 310, 309], 
    [310, 314, 311], 
    [311, 314, 312], 
    [312, 314, 313], 
    [314, 315, 19], 
    [315, 314, 316], 
    [316, 314, 317], 
    [317, 319, 318], 
    [319, 321, 320], 
    [321, 323, 322], 
    [323, 325, 324], 
    [325, 329, 326], 
    [326, 329, 327], 
    [327, 329, 328], 
    [329, 330, 20], 
    [330, 329, 331], 
    [331, 329, 332], 
    [332, 334, 333], 
    [334, 336, 335], 
    [336, 338, 337], 
    [338, 340, 339], 
    [340, 344, 341], 
    [341, 344, 342], 
    [342, 344, 343], 
    [344, 345, 21], 
    [345, 344, 346], 
    [346, 344, 347], 
    [347, 349, 348], 
    [349, 351, 350], 
    [351, 353, 352], 
    [353, 355, 354], 
    [355, 359, 356], 
    [356, 359, 357], 
    [357, 359, 358], 
    [359, 360, 22], 
    [360, 359, 361], 
    [361, 359, 362], 
    [362, 364, 363], 
    [364, 366, 365], 
    [366, 368, 367], 
    [368, 370, 369], 
    [370, 374, 371], 
    [371, 374, 372], 
    [372, 374, 373], 
    [374, 375, 23], 
    [375, 374, 376], 
    [376, 374, 377], 
    [377, 379, 378], 
    [379, 381, 380], 
    [381, 383, 382], 
    [383, 385, 384], 
    [385, 389, 386], 
    [386, 389, 387], 
    [387, 389, 388], 
    [389, 390, 24], 
    [390, 389, 391], 
    [391, 389, 392], 
    [392, 394, 393], 
    [394, 396, 395], 
    [396, 398, 397], 
    [398, 400, 399], 
    [400, 404, 401], 
    [401, 404, 402], 
    [402, 404, 403], 
    [404, 405, 25], 
    [405, 404, 406], 
    [406, 404, 407], 
    [407, 409, 408], 
    [409, 411, 410], 
    [411, 413, 412], 
    [413, 415, 414], 
    [415, 419, 416], 
    [416, 419, 417], 
    [417, 419, 418], 
    [419, 420, 26], 
    [420, 422, 421], 
    [422, 424, 423], 
    [424, 426, 425], 
    [426, 428, 427], 
    [428, 430, 429], 
    [430, 434, 431], 
    [431, 434, 432], 
    [432, 434, 433], 
    [434, 435, 27], 
    [435, 434, 436], 
    [436, 434, 437], 
    [437, 439, 438], 
    [439, 441, 440], 
    [441, 443, 442], 
    [443, 445, 444], 
    [445, 449, 446], 
    [446, 449, 447], 
    [447, 449, 448], 
    [449, 450, 28], 
    [450, 449, 451], 
    [451, 449, 452], 
    [452, 454, 453], 
    [454, 456, 455], 
    [456, 458, 457], 
    [458, 460, 459], 
    [460, 464, 461], 
    [461, 464, 462], 
    [462, 464, 463], 
    [464, 465, 29], 
    [465, 464, 466], 
    [466, 464, 467], 
    [467, 469, 468], 
    [469, 471, 470], 
    [471, 473, 472], 
    [473, 475, 474], 
    [475, 479, 476], 
    [476, 479, 477], 
    [477, 479, 478], 
    [479, 480, 30], 
    [480, 479, 481], 
    [481, 479, 482], 
    [482, 484, 483], 
    [484, 486, 485], 
    [486, 488, 487], 
    [488, 490, 489], 
    [490, 494, 491], 
    [491, 494, 492], 
    [492, 494, 493], 
    [494, 495, 31], 
    [495, 494, 496], 
    [496, 494, 497], 
    [497, 499, 498], 
    [499, 501, 500], 
    [501, 503, 502], 
    [503, 505, 504], 
    [505, 509, 506], 
    [506, 509, 507], 
    [507, 509, 508], 
    [34, 509, 36], 
    [36, 509, 38], 
    [38, 46, 40], 
    [40, 46, 42], 
    [49, 46, 51], 
    [51, 46, 53], 
    [53, 61, 55], 
    [55, 61, 57], 
    [61, 64, 62], 
    [64, 61, 66], 
    [66, 61, 68], 
    [68, 76, 70], 
    [70, 76, 72], 
    [76, 79, 77], 
    [79, 76, 81], 
    [81, 76, 82], 
    [82, 90, 84], 
    [84, 90, 86], 
    [93, 90, 95], 
    [95, 90, 97], 
    [97, 105, 99], 
    [99, 105, 101], 
    [108, 105, 110], 
    [110, 105, 112], 
    [112, 120, 114], 
    [114, 120, 116], 
    [123, 120, 125], 
    [125, 120, 127], 
    [127, 135, 129], 
    [129, 135, 131], 
    [138, 135, 140], 
    [140, 135, 142], 
    [142, 150, 144], 
    [144, 150, 146], 
    [153, 150, 155], 
    [155, 150, 157], 
    [157, 165, 159], 
    [159, 165, 161], 
    [168, 165, 170], 
    [170, 165, 172], 
    [172, 180, 174], 
    [174, 180, 176], 
    [180, 183, 181], 
    [183, 180, 184], 
    [184, 180, 186], 
    [186, 194, 188], 
    [188, 194, 190], 
    [197, 194, 199], 
    [199, 194, 201], 
    [201, 209, 203], 
    [203, 209, 205], 
    [212, 209, 214], 
    [214, 209, 216], 
    [216, 224, 218], 
    [218, 224, 220], 
    [227, 224, 229], 
    [229, 224, 231], 
    [231, 239, 233], 
    [233, 239, 235], 
    [242, 239, 244], 
    [244, 239, 246], 
    [246, 254, 248], 
    [248, 254, 250], 
    [257, 254, 259], 
    [259, 254, 261], 
    [261, 269, 263], 
    [263, 269, 265], 
    [269, 272, 270], 
    [272, 269, 274], 
    [274, 269, 276], 
    [276, 284, 278], 
    [278, 284, 280], 
    [287, 284, 289], 
    [289, 284, 291], 
    [291, 299, 293], 
    [293, 299, 295], 
    [299, 302, 300], 
    [302, 299, 304], 
    [304, 299, 306], 
    [306, 314, 308], 
    [308, 314, 310], 
    [317, 314, 319], 
    [319, 314, 321], 
    [321, 329, 323], 
    [323, 329, 325], 
    [332, 329, 334], 
    [334, 329, 336], 
    [336, 344, 338], 
    [338, 344, 340], 
    [347, 344, 349], 
    [349, 344, 351], 
    [351, 359, 353], 
    [353, 359, 355], 
    [362, 359, 364], 
    [364, 359, 366], 
    [366, 374, 368], 
    [368, 374, 370], 
    [377, 374, 379], 
    [379, 374, 381], 
    [381, 389, 383], 
    [383, 389, 385], 
    [392, 389, 394], 
    [394, 389, 396], 
    [396, 404, 398], 
    [398, 404, 400], 
    [407, 404, 409], 
    [409, 404, 411], 
    [411, 419, 413], 
    [413, 419, 415], 
    [419, 422, 420], 
    [422, 419, 424], 
    [424, 419, 426], 
    [426, 434, 428], 
    [428, 434, 430], 
    [437, 434, 439], 
    [439, 434, 441], 
    [441, 449, 443], 
    [443, 449, 445], 
    [452, 449, 454], 
    [454, 449, 456], 
    [456, 464, 458], 
    [458, 464, 460], 
    [467, 464, 469], 
    [469, 464, 471], 
    [471, 479, 473], 
    [473, 479, 475], 
    [482, 479, 484], 
    [484, 479, 486], 
    [486, 494, 488], 
    [488, 494, 490], 
    [497, 494, 499], 
    [499, 494, 501], 
    [501, 509, 503], 
    [503, 509, 505], 
    [509, 61, 38], 
    [38, 53, 46], 
    [61, 53, 38], 
    [61, 509, 68], 
    [68, 82, 76], 
    [150, 90, 82], 
    [68, 150, 82], 
    [90, 120, 97], 
    [97, 112, 105], 
    [120, 112, 97], 
    [120, 142, 127], 
    [127, 142, 135], 
    [142, 120, 150], 
    [150, 180, 157], 
    [157, 172, 165], 
    [180, 172, 157], 
    [180, 150, 186], 
    [186, 201, 194], 
    [269, 209, 201], 
    [186, 269, 201], 
    [209, 239, 216], 
    [216, 231, 224], 
    [239, 231, 216], 
    [239, 209, 246], 
    [246, 261, 254], 
    [269, 261, 246], 
    [269, 291, 276], 
    [276, 291, 284], 
    [291, 306, 299], 
    [269, 306, 291], 
    [306, 321, 314], 
    [351, 336, 321], 
    [321, 336, 329], 
    [306, 351, 321], 
    [336, 351, 344], 
    [351, 389, 359], 
    [359, 381, 366], 
    [366, 381, 374], 
    [381, 359, 389], 
    [389, 419, 396], 
    [396, 411, 404], 
    [419, 411, 396], 
    [419, 389, 426], 
    [426, 441, 434], 
    [509, 449, 441], 
    [426, 509, 441], 
    [449, 479, 456], 
    [456, 471, 464], 
    [479, 471, 456], 
    [479, 449, 486], 
    [486, 501, 494], 
    [501, 449, 509], 
    [509, 150, 68], 
    [150, 269, 186], 
    [246, 209, 269], 
    [269, 389, 306], 
    [389, 509, 426], 
    [486, 449, 501], 
    [90, 150, 120], 
    [389, 351, 306], 
    [509, 269, 150]
] # PSD_wall_list

PSD = m.GeometryObject(
    name = 'PSD',
    vertex_list = PSD_vertex_list,
    wall_list = PSD_wall_list,
    surface_regions = []
)
# ^^^^ PSD ^^^^


