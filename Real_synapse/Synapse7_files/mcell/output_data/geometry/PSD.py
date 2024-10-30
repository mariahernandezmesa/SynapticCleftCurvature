import mcell as m

# ---- PSD ----
PSD_vertex_list = [
    [0.141839578747749, -0.0977087020874023, -0.00266999006271362], 
    [0.117015838623047, -0.108168601989746, -0.0134299397468567], 
    [0.136807933449745, -0.0759778022766113, 0.0163945555686951], 
    [0.105596989393234, -0.084932804107666, 0.00201517343521118], 
    [0.073493018746376, -0.0582952499389648, 0.00768440961837769], 
    [0.106558591127396, -0.0632281303405762, 0.0231727361679077], 
    [0.0748164355754852, -0.0826554298400879, -0.0117250084877014], 
    [0.0895259976387024, -0.104793548583984, -0.0195633769035339], 
    [0.076012521982193, -0.123367309570312, -0.0379528999328613], 
    [0.104394108057022, -0.127970218658447, -0.0265814065933228], 
    [0.0596348531544209, -0.0967574119567871, -0.032233715057373], 
    [0.027666512876749, -0.081843376159668, -0.0528813004493713], 
    [0.0497467704117298, -0.0694403648376465, -0.0232844352722168], 
    [0.047564122825861, -0.113146781921387, -0.0537671446800232], 
    [0.0650900155305862, -0.141266822814941, -0.058251678943634], 
    [0.0416475646197796, -0.131464958190918, -0.0717242956161499], 
    [0.0228460915386677, -0.108936309814453, -0.0759286284446716], 
    [0.00183969363570213, -0.0843214988708496, -0.0809026956558228], 
    [-0.000427301973104477, -0.113095760345459, -0.102132260799408], 
    [0.0236586220562458, -0.137749671936035, -0.0914561748504639], 
    [0.0331028886139393, -0.167207717895508, -0.10196191072464], 
    [0.00676025077700615, -0.14823579788208, -0.115227401256561], 
    [0.0503828413784504, -0.155497550964355, -0.0794469714164734], 
    [0.0784522294998169, -0.165240287780762, -0.068288266658783], 
    [0.0626060664653778, -0.179543495178223, -0.0885012745857239], 
    [0.0786621868610382, -0.203819751739502, -0.0977578163146973], 
    [0.0484967567026615, -0.194446086883545, -0.108226001262665], 
    [0.0893597006797791, -0.186597347259521, -0.0807228684425354], 
    [0.107991561293602, -0.178224086761475, -0.0639654994010925], 
    [0.0963259041309357, -0.151349544525146, -0.0466836094856262], 
    [0.0174829624593258, -0.184916973114014, -0.128036379814148], 
    [0.065570279955864, -0.219818592071533, -0.117209136486053], 
    [0.0397867523133755, -0.2098388671875, -0.129266381263733], 
    [0.0520103760063648, -0.233474731445312, -0.138302028179169], 
    [0.020146120339632, -0.21839427947998, -0.151806116104126], 
    [-0.00616456940770149, -0.22076940536499, -0.170519292354584], 
    [0.0140040256083012, -0.249851703643799, -0.17735493183136], 
    [-0.00719844177365303, -0.192021369934082, -0.153976857662201], 
    [0.0384756587445736, -0.247377395629883, -0.158717155456543], 
    [0.0645551532506943, -0.25739049911499, -0.149592936038971], 
    [0.0468189083039761, -0.276060104370117, -0.175215721130371], 
    [0.0776685476303101, -0.280464649200439, -0.156601548194885], 
    [0.0829183459281921, -0.307961463928223, -0.168677389621735], 
    [0.0157814808189869, -0.284964084625244, -0.199937462806702], 
    [0.0552786327898502, -0.309757232666016, -0.189006626605988], 
    [-0.0229038000106812, -0.241191864013672, -0.193664729595184], 
    [-0.0565618388354778, -0.213446140289307, -0.198006689548492], 
    [-0.0328200682997704, -0.198432922363281, -0.176496744155884], 
    [-0.0343375578522682, -0.165813446044922, -0.158277750015259], 
    [-0.0660694018006325, -0.172830581665039, -0.182254314422607], 
    [-0.0549510829150677, -0.135950565338135, -0.158985674381256], 
    [-0.0881960317492485, -0.136820316314697, -0.174369931221008], 
    [-0.104960530996323, -0.163088798522949, -0.191746652126312], 
    [-0.0934430062770844, -0.197436332702637, -0.20577210187912], 
    [-0.121119201183319, -0.130860805511475, -0.183421969413757], 
    [-0.110571950674057, -0.103385448455811, -0.169199228286743], 
    [-0.0943963006138802, -0.0814375877380371, -0.156556367874146], 
    [-0.126557767391205, -0.0692367553710938, -0.164654314517975], 
    [-0.0773704349994659, -0.108045101165771, -0.157249093055725], 
    [-0.0495730713009834, -0.10547924041748, -0.139470100402832], 
    [-0.0677199065685272, -0.0789847373962402, -0.139431595802307], 
    [-0.0301740989089012, -0.072291374206543, -0.107286095619202], 
    [-0.0655630379915237, -0.0514440536499023, -0.125945687294006], 
    [-0.0922731682658195, -0.0520601272583008, -0.144986927509308], 
    [-0.122031286358833, -0.0418720245361328, -0.152013123035431], 
    [-0.0822626054286957, -0.0216684341430664, -0.124426782131195], 
    [-0.107612140476704, -0.0263614654541016, -0.1402867436409], 
    [-0.116997241973877, 8.0108642578125e-05, -0.131426930427551], 
    [-0.133771121501923, -0.0205888748168945, -0.144294559955597], 
    [-0.161826148629189, -0.0120973587036133, -0.148648619651794], 
    [-0.149308413267136, -0.0375127792358398, -0.159344077110291], 
    [-0.143970370292664, -0.000335693359375, -0.13707047700882], 
    [-0.143348693847656, 0.0214529037475586, -0.126473665237427], 
    [-0.165158778429031, 0.0115242004394531, -0.136452317237854], 
    [-0.192022904753685, 0.00708484649658203, -0.144807279109955], 
    [-0.177604392170906, 0.0346097946166992, -0.121273577213287], 
    [-0.145994767546654, 0.0436954498291016, -0.111800312995911], 
    [-0.169575035572052, 0.0573081970214844, -0.0958255529403687], 
    [-0.143090292811394, 0.0578775405883789, -0.0915236473083496], 
    [-0.124547153711319, 0.0639104843139648, -0.0810432434082031], 
    [-0.119180336594582, 0.0473136901855469, -0.0994076728820801], 
    [-0.0986622497439384, 0.0543289184570312, -0.0827318429946899], 
    [-0.117002174258232, 0.0275173187255859, -0.118638455867767], 
    [-0.0921756774187088, 0.0333347320556641, -0.103299498558044], 
    [-0.0703747496008873, 0.0375595092773438, -0.0836325883865356], 
    [-0.0661394149065018, 0.00199127197265625, -0.103259205818176], 
    [-0.0943174362182617, 0.00729942321777344, -0.115883529186249], 
    [-0.0526760444045067, 0.0122795104980469, -0.0772049427032471], 
    [-0.033012043684721, -0.0237197875976562, -0.0800240635871887], 
    [-0.0532928109169006, -0.0313987731933594, -0.108307838439941], 
    [-0.0147374495863914, -0.0132999420166016, -0.0519996881484985], 
    [-0.00333690643310547, -0.0502262115478516, -0.0654091835021973], 
    [-0.0358120240271091, 0.0101823806762695, -0.0555844902992249], 
    [-0.0247177481651306, 0.0144329071044922, -0.0303876399993896], 
    [-0.000968847423791885, -0.00286006927490234, -0.0231403708457947], 
    [-0.0366056151688099, 0.0389385223388672, -0.0073692798614502], 
    [-0.0127734281122684, 0.0218544006347656, -0.00616538524627686], 
    [-0.0225562416017056, 0.0451278686523438, 0.015680730342865], 
    [0.00984245166182518, 0.00710678100585938, 0.00299036502838135], 
    [-0.000315103679895401, 0.0301971435546875, 0.0147072076797485], 
    [0.021042738109827, 0.0255365371704102, 0.0336349010467529], 
    [-0.00239182636141777, 0.0478858947753906, 0.0322456359863281], 
    [0.00992980971932411, 0.0612039566040039, 0.0578043460845947], 
    [-0.0234456472098827, 0.0679759979248047, 0.0383606553077698], 
    [-0.0465103164315224, 0.0620651245117188, 0.0164316892623901], 
    [-0.0194387063384056, 0.08953857421875, 0.0638139843940735], 
    [-0.0524055249989033, 0.0901117324829102, 0.0382994413375854], 
    [-0.0731832087039948, 0.0770559310913086, 0.0107394456863403], 
    [-0.0479022189974785, 0.114507675170898, 0.0644116401672363], 
    [-0.0774976015090942, 0.118800163269043, 0.0464595556259155], 
    [-0.0851896405220032, 0.09869384765625, 0.025810182094574], 
    [-0.107319325208664, 0.118935585021973, 0.025115966796875], 
    [-0.127213284373283, 0.138641357421875, 0.0315197110176086], 
    [-0.103635564446449, 0.140961647033691, 0.0486000776290894], 
    [-0.112129107117653, 0.170160293579102, 0.0676544308662415], 
    [-0.0780820101499557, 0.142525672912598, 0.070832371711731], 
    [-0.128111824393272, 0.161099433898926, 0.044460654258728], 
    [-0.0658180341124535, 0.157687187194824, 0.0923314690589905], 
    [-0.0887040048837662, 0.172013282775879, 0.0878105759620667], 
    [-0.0478171184659004, 0.136092185974121, 0.0886716246604919], 
    [-0.0191136598587036, 0.115158081054688, 0.0890585780143738], 
    [-0.0473949611186981, 0.159943580627441, 0.111713826656342], 
    [-0.0281275473535061, 0.140804290771484, 0.109667658805847], 
    [-0.00367538258433342, 0.134297370910645, 0.12379115819931], 
    [-0.0244898982346058, 0.159318923950195, 0.137322723865509], 
    [-0.010810200124979, 0.172391891479492, 0.165655672550201], 
    [-0.0544469431042671, 0.181447982788086, 0.13026350736618], 
    [0.0154643170535564, 0.147859573364258, 0.152892470359802], 
    [-0.0418560430407524, 0.18587589263916, 0.155481994152069], 
    [-0.0657067075371742, 0.20689868927002, 0.145307838916779], 
    [-0.0323066785931587, 0.195956230163574, 0.180515944957733], 
    [-0.0593697614967823, 0.216479301452637, 0.172265112400055], 
    [-0.0616088099777699, 0.239195823669434, 0.19251149892807], 
    [-0.0728634744882584, 0.254433631896973, 0.174755156040192], 
    [-0.0771807879209518, 0.239681243896484, 0.153715789318085], 
    [-0.0444529578089714, 0.220346450805664, 0.198286056518555], 
    [-0.0219376012682915, 0.20244312286377, 0.201961129903793], 
    [-0.0575583167374134, 0.248390197753906, 0.214933961629868], 
    [-0.065116360783577, 0.274084091186523, 0.223578602075577], 
    [-0.0654967278242111, 0.266724586486816, 0.198409497737885], 
    [-0.0627840608358383, 0.294750213623047, 0.206949234008789], 
    [-0.0686798468232155, 0.285953521728516, 0.180088222026825], 
    [-0.0779248103499413, 0.274606704711914, 0.155768215656281], 
    [-0.0882794931530952, 0.260202407836914, 0.130433022975922], 
    [-0.0831740871071815, 0.22769832611084, 0.13167142868042], 
    [-0.101349748671055, 0.227540016174316, 0.108623027801514], 
    [-0.0885207653045654, 0.195300102233887, 0.102367997169495], 
    [-0.0765236988663673, 0.202362060546875, 0.121982932090759], 
    [-0.109186217188835, 0.194674491882324, 0.0878042578697205], 
    [-0.0692664980888367, 0.17857837677002, 0.10719883441925], 
    [-0.00447644665837288, 0.184656143188477, 0.192555129528046], 
    [0.0186473019421101, 0.16423225402832, 0.183022379875183], 
    [0.0178375355899334, 0.18132209777832, 0.207068264484406], 
    [0.0455032773315907, 0.167912483215332, 0.207599878311157], 
    [0.0472303219139576, 0.145414352416992, 0.17730700969696], 
    [0.0737266838550568, 0.148677825927734, 0.202117502689362], 
    [0.0781135857105255, 0.126107215881348, 0.173990786075592], 
    [0.102347135543823, 0.131990432739258, 0.198100864887238], 
    [0.110391780734062, 0.108848571777344, 0.176319360733032], 
    [0.135863959789276, 0.116044044494629, 0.199859380722046], 
    [0.125445991754532, 0.139252662658691, 0.21442374587059], 
    [0.139860570430756, 0.0953197479248047, 0.1816366314888], 
    [0.127792716026306, 0.0812282562255859, 0.16072952747345], 
    [0.163522452116013, 0.0769281387329102, 0.173347294330597], 
    [0.159676849842072, 0.0570106506347656, 0.151650309562683], 
    [0.151322185993195, 0.0426435470581055, 0.133291661739349], 
    [0.130658507347107, 0.0594358444213867, 0.138923168182373], 
    [0.106633692979813, 0.0747594833374023, 0.13829243183136], 
    [0.128576442599297, 0.0387763977050781, 0.122128307819366], 
    [0.109321221709251, 0.0562372207641602, 0.123199582099915], 
    [0.0815550684928894, 0.0674495697021484, 0.115763366222382], 
    [0.099724143743515, 0.0377845764160156, 0.107662796974182], 
    [0.127469018101692, 0.0157976150512695, 0.108773291110992], 
    [0.101970434188843, 0.0111560821533203, 0.0936293005943298], 
    [0.0666888505220413, 0.0368013381958008, 0.090198814868927], 
    [0.0836025327444077, -0.000212669372558594, 0.0723177790641785], 
    [0.0356189571321011, 0.0593280792236328, 0.0785903334617615], 
    [0.0602263547480106, 0.0133075714111328, 0.0629966259002686], 
    [0.0379198230803013, 0.0335206985473633, 0.0615416765213013], 
    [0.0521198399364948, 0.0760974884033203, 0.0992543697357178], 
    [0.0366811938583851, 0.103628158569336, 0.112299025058746], 
    [0.0638021677732468, 0.0959091186523438, 0.124117374420166], 
    [0.0139778964221478, 0.0879659652709961, 0.084653377532959], 
    [0.00965531542897224, 0.113468170166016, 0.105960845947266], 
    [0.0234875045716763, 0.126058578491211, 0.128545105457306], 
    [0.0528645105659962, 0.122936248779297, 0.146478593349457], 
    [0.0877946615219116, 0.101199150085449, 0.148758590221405], 
    [0.0452448017895222, 0.00504493713378906, 0.0408297777175903], 
    [0.0311390645802021, -0.00286483764648438, 0.0172409415245056], 
    [0.0686157196760178, -0.0137672424316406, 0.0473535656929016], 
    [0.0532453544437885, -0.0268115997314453, 0.0193616151809692], 
    [0.0246792919933796, -0.0203266143798828, -0.0104367733001709], 
    [0.0819132328033447, -0.0391626358032227, 0.0325729250907898], 
    [0.0453218780457973, -0.0448684692382812, -0.00712811946868896], 
    [0.0263439305126667, -0.0505008697509766, -0.0349831581115723], 
    [0.00723827257752419, -0.0271682739257812, -0.0382194519042969], 
    [0.0942443758249283, -0.0250453948974609, 0.0563014149665833], 
    [0.107788890600204, -0.0447101593017578, 0.0426346063613892], 
    [0.120918661355972, -0.0372772216796875, 0.0624681711196899], 
    [0.136501654982567, -0.0560522079467773, 0.0409412980079651], 
    [0.108724296092987, -0.0150527954101562, 0.0784383416175842], 
    [0.133169189095497, -0.0273313522338867, 0.0805584192276001], 
    [0.13025364279747, -0.00823497772216797, 0.0962137579917908], 
    [0.15696494281292, -0.00365066528320312, 0.107539474964142], 
    [0.155065506696701, 0.0223026275634766, 0.119362831115723], 
    [-0.181307077407837, -0.0275497436523438, -0.162994742393494], 
    [-0.0230596326291561, -0.129950046539307, -0.131348729133606], 
    [-0.00849919766187668, -0.16415548324585, -0.137331426143646], 
    [0.103663682937622, -0.292148590087891, -0.150956273078918], 
    [0.0950521677732468, -0.266271114349365, -0.14100980758667], 
    [0.122935190796852, -0.277842998504639, -0.137769162654877], 
    [0.11615663766861, -0.251235008239746, -0.124126195907593], 
    [0.081416130065918, -0.24337100982666, -0.128808975219727], 
    [0.095645934343338, -0.225193977355957, -0.110091745853424]
] # PSD_vertex_list

PSD_wall_list = [
    [0, 3, 1], 
    [2, 3, 0], 
    [3, 5, 4], 
    [3, 4, 6], 
    [7, 1, 3], 
    [3, 2, 5], 
    [6, 7, 3], 
    [10, 8, 7], 
    [8, 9, 7], 
    [7, 9, 1], 
    [10, 7, 6], 
    [12, 11, 10], 
    [13, 10, 11], 
    [6, 12, 10], 
    [8, 10, 13], 
    [13, 14, 8], 
    [13, 15, 14], 
    [16, 13, 11], 
    [15, 13, 16], 
    [11, 17, 16], 
    [15, 16, 19], 
    [17, 18, 16], 
    [19, 16, 18], 
    [15, 19, 22], 
    [19, 21, 20], 
    [22, 19, 20], 
    [18, 21, 19], 
    [22, 23, 14], 
    [14, 15, 22], 
    [23, 22, 24], 
    [24, 22, 20], 
    [23, 24, 27], 
    [20, 26, 24], 
    [27, 24, 25], 
    [24, 26, 25], 
    [27, 28, 23], 
    [23, 28, 29], 
    [8, 14, 29], 
    [14, 23, 29], 
    [9, 8, 29], 
    [30, 26, 20], 
    [30, 32, 26], 
    [25, 26, 31], 
    [32, 31, 26], 
    [31, 32, 33], 
    [32, 34, 33], 
    [30, 34, 32], 
    [34, 37, 35], 
    [34, 35, 36], 
    [38, 34, 36], 
    [37, 34, 30], 
    [34, 38, 33], 
    [40, 38, 36], 
    [39, 33, 38], 
    [40, 39, 38], 
    [36, 43, 40], 
    [41, 39, 40], 
    [40, 42, 41], 
    [42, 40, 44], 
    [44, 40, 43], 
    [45, 43, 36], 
    [36, 35, 45], 
    [35, 47, 45], 
    [46, 45, 47], 
    [47, 37, 48], 
    [48, 49, 47], 
    [35, 37, 47], 
    [46, 47, 49], 
    [48, 50, 49], 
    [50, 51, 49], 
    [52, 49, 51], 
    [49, 52, 53], 
    [49, 53, 46], 
    [51, 54, 52], 
    [51, 55, 54], 
    [56, 57, 55], 
    [56, 55, 58], 
    [58, 55, 51], 
    [59, 60, 58], 
    [58, 50, 59], 
    [58, 60, 56], 
    [58, 51, 50], 
    [60, 59, 61], 
    [60, 63, 56], 
    [60, 61, 62], 
    [62, 63, 60], 
    [64, 57, 63], 
    [63, 66, 64], 
    [63, 57, 56], 
    [62, 65, 63], 
    [65, 66, 63], 
    [64, 66, 68], 
    [66, 65, 67], 
    [68, 66, 67], 
    [68, 70, 64], 
    [69, 70, 68], 
    [68, 71, 69], 
    [67, 71, 68], 
    [71, 73, 69], 
    [67, 72, 71], 
    [71, 72, 73], 
    [75, 74, 73], 
    [74, 69, 73], 
    [75, 73, 72], 
    [76, 75, 72], 
    [75, 76, 77], 
    [76, 78, 77], 
    [78, 80, 79], 
    [76, 80, 78], 
    [81, 79, 80], 
    [81, 80, 83], 
    [80, 76, 82], 
    [83, 80, 82], 
    [84, 81, 83], 
    [83, 85, 84], 
    [86, 85, 83], 
    [83, 82, 86], 
    [65, 86, 67], 
    [85, 86, 65], 
    [82, 67, 86], 
    [87, 84, 85], 
    [88, 87, 85], 
    [85, 89, 88], 
    [65, 89, 85], 
    [89, 61, 88], 
    [65, 62, 89], 
    [89, 62, 61], 
    [90, 92, 88], 
    [88, 91, 90], 
    [88, 61, 91], 
    [92, 87, 88], 
    [93, 92, 90], 
    [93, 90, 94], 
    [94, 96, 93], 
    [93, 96, 95], 
    [96, 99, 97], 
    [95, 96, 97], 
    [98, 96, 94], 
    [96, 98, 99], 
    [100, 99, 98], 
    [100, 101, 99], 
    [99, 101, 97], 
    [102, 103, 101], 
    [102, 101, 100], 
    [97, 101, 103], 
    [103, 106, 104], 
    [97, 103, 104], 
    [102, 105, 103], 
    [105, 106, 103], 
    [107, 104, 106], 
    [107, 106, 110], 
    [108, 106, 105], 
    [106, 108, 109], 
    [106, 109, 110], 
    [110, 109, 111], 
    [112, 111, 113], 
    [109, 113, 111], 
    [113, 115, 114], 
    [116, 113, 114], 
    [115, 113, 109], 
    [112, 113, 116], 
    [118, 115, 117], 
    [117, 115, 119], 
    [114, 115, 118], 
    [109, 108, 115], 
    [115, 108, 119], 
    [119, 120, 122], 
    [119, 108, 120], 
    [122, 121, 119], 
    [121, 117, 119], 
    [121, 122, 124], 
    [122, 120, 123], 
    [124, 122, 123], 
    [127, 124, 123], 
    [128, 124, 125], 
    [125, 124, 127], 
    [124, 126, 121], 
    [126, 124, 128], 
    [130, 128, 125], 
    [128, 129, 126], 
    [129, 128, 131], 
    [130, 131, 128], 
    [132, 131, 135], 
    [131, 132, 133], 
    [133, 134, 131], 
    [134, 129, 131], 
    [131, 130, 135], 
    [132, 135, 137], 
    [136, 135, 130], 
    [137, 139, 132], 
    [137, 138, 139], 
    [133, 132, 139], 
    [139, 141, 133], 
    [140, 139, 138], 
    [140, 141, 139], 
    [141, 142, 133], 
    [143, 134, 142], 
    [142, 134, 133], 
    [143, 144, 134], 
    [144, 143, 145], 
    [147, 144, 145], 
    [145, 146, 147], 
    [146, 145, 148], 
    [148, 114, 118], 
    [146, 148, 118], 
    [147, 149, 126], 
    [149, 147, 146], 
    [144, 147, 129], 
    [147, 126, 129], 
    [126, 149, 121], 
    [149, 146, 118], 
    [117, 121, 149], 
    [118, 117, 149], 
    [129, 134, 144], 
    [130, 150, 136], 
    [125, 151, 150], 
    [150, 130, 125], 
    [152, 150, 151], 
    [152, 151, 153], 
    [154, 153, 151], 
    [154, 155, 153], 
    [154, 156, 155], 
    [156, 157, 155], 
    [157, 156, 158], 
    [157, 158, 159], 
    [160, 157, 159], 
    [159, 158, 161], 
    [158, 162, 161], 
    [162, 163, 161], 
    [163, 162, 164], 
    [164, 166, 165], 
    [166, 164, 162], 
    [169, 166, 167], 
    [162, 167, 166], 
    [169, 168, 166], 
    [166, 168, 165], 
    [167, 170, 169], 
    [170, 171, 169], 
    [169, 171, 168], 
    [171, 172, 168], 
    [172, 171, 173], 
    [174, 171, 170], 
    [174, 173, 171], 
    [173, 174, 175], 
    [175, 174, 177], 
    [174, 176, 178], 
    [179, 176, 174], 
    [174, 178, 177], 
    [170, 179, 174], 
    [179, 170, 181], 
    [181, 180, 179], 
    [182, 179, 180], 
    [179, 182, 176], 
    [182, 180, 183], 
    [183, 120, 182], 
    [105, 182, 120], 
    [105, 102, 182], 
    [182, 102, 176], 
    [183, 180, 184], 
    [123, 120, 183], 
    [184, 123, 183], 
    [127, 123, 184], 
    [184, 180, 185], 
    [184, 185, 127], 
    [180, 181, 185], 
    [185, 181, 186], 
    [127, 185, 154], 
    [154, 185, 156], 
    [156, 185, 186], 
    [186, 158, 156], 
    [162, 158, 186], 
    [186, 170, 167], 
    [181, 170, 186], 
    [186, 167, 162], 
    [100, 178, 102], 
    [102, 178, 176], 
    [177, 178, 187], 
    [178, 100, 187], 
    [177, 187, 189], 
    [187, 100, 188], 
    [190, 187, 188], 
    [190, 189, 187], 
    [4, 192, 190], 
    [193, 4, 190], 
    [190, 188, 191], 
    [190, 191, 193], 
    [192, 189, 190], 
    [193, 12, 4], 
    [194, 12, 193], 
    [193, 191, 194], 
    [194, 11, 12], 
    [195, 91, 194], 
    [194, 191, 195], 
    [194, 91, 11], 
    [90, 195, 94], 
    [94, 195, 191], 
    [195, 90, 91], 
    [5, 192, 4], 
    [192, 5, 197], 
    [189, 192, 196], 
    [196, 192, 197], 
    [197, 198, 196], 
    [197, 199, 198], 
    [197, 5, 199], 
    [199, 5, 2], 
    [196, 198, 200], 
    [201, 200, 198], 
    [202, 200, 201], 
    [172, 202, 203], 
    [173, 202, 172], 
    [202, 173, 200], 
    [172, 203, 204], 
    [204, 165, 168], 
    [168, 172, 204], 
    [200, 175, 196], 
    [173, 175, 200], 
    [196, 175, 189], 
    [191, 98, 94], 
    [98, 191, 188], 
    [189, 175, 177], 
    [98, 188, 100], 
    [151, 127, 154], 
    [125, 127, 151], 
    [108, 105, 120], 
    [97, 104, 95], 
    [11, 91, 17], 
    [61, 17, 91], 
    [72, 82, 76], 
    [72, 67, 82], 
    [205, 69, 74], 
    [205, 70, 69], 
    [64, 70, 57], 
    [18, 61, 206], 
    [61, 59, 206], 
    [61, 18, 17], 
    [59, 50, 206], 
    [206, 50, 48], 
    [206, 48, 207], 
    [206, 21, 18], 
    [206, 207, 21], 
    [21, 207, 30], 
    [207, 37, 30], 
    [207, 48, 37], 
    [42, 208, 41], 
    [41, 208, 209], 
    [210, 209, 208], 
    [211, 209, 210], 
    [209, 211, 212], 
    [213, 212, 211], 
    [213, 31, 212], 
    [31, 213, 25], 
    [33, 212, 31], 
    [212, 33, 39], 
    [212, 39, 209], 
    [209, 39, 41], 
    [20, 21, 30], 
    [4, 12, 6]
] # PSD_wall_list

PSD = m.GeometryObject(
    name = 'PSD',
    vertex_list = PSD_vertex_list,
    wall_list = PSD_wall_list,
    surface_regions = []
)
# ^^^^ PSD ^^^^


