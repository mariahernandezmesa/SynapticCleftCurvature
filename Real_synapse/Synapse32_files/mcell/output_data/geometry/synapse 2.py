import mcell as m

# ---- synapse ----
synapse_vertex_list = [
    [-0.11620169878006, 0.120989322662354, 0.123479306697845], 
    [-0.112866520881653, 0.0896072387695312, 0.130037784576416], 
    [-0.106405556201935, 0.100253582000732, 0.108003854751587], 
    [-0.106805115938187, 0.125246524810791, 0.0981556177139282], 
    [-0.0945029854774475, 0.126319885253906, 0.0730736255645752], 
    [-0.107104122638702, 0.151471614837646, 0.0873832106590271], 
    [-0.0950409770011902, 0.0970292091369629, 0.0851204991340637], 
    [-0.0823087692260742, 0.102316856384277, 0.0605700612068176], 
    [-0.0771077275276184, 0.0699353218078613, 0.0764822363853455], 
    [-0.0938166379928589, 0.0726618766784668, 0.108076393604279], 
    [-0.0725292265415192, 0.0475645065307617, 0.101372241973877], 
    [-0.0854832231998444, 0.0477943420410156, 0.125157058238983], 
    [-0.102855890989304, 0.062464714050293, 0.140849590301514], 
    [-0.0668182671070099, 0.0265846252441406, 0.123521268367767], 
    [-0.0536415278911591, 0.0189995765686035, 0.0992921590805054], 
    [-0.0505341589450836, -0.00337362289428711, 0.121738791465759], 
    [-0.0410593748092651, -0.00919580459594727, 0.0933248996734619], 
    [-0.0398787558078766, -0.0323085784912109, 0.108525574207306], 
    [-0.0310833156108856, -0.0342378616333008, 0.0863568782806396], 
    [-0.0335967540740967, -0.0574078559875488, 0.119204580783844], 
    [-0.0272112190723419, -0.0581526756286621, 0.0959951281547546], 
    [-0.0225940346717834, -0.0827093124389648, 0.110226988792419], 
    [-0.0138983726501465, -0.0801420211791992, 0.08515864610672], 
    [-0.0177815556526184, -0.053767204284668, 0.0739207863807678], 
    [-0.00340235233306885, -0.0762100219726562, 0.0597317218780518], 
    [-0.0110869407653809, -0.0428609848022461, 0.0513359308242798], 
    [-0.0274551808834076, -0.0185742378234863, 0.0642430186271667], 
    [-0.0135680437088013, -0.0152740478515625, 0.0371384620666504], 
    [-0.0425125062465668, 0.0103311538696289, 0.0743386745452881], 
    [-0.0312539637088776, 0.00760459899902344, 0.0496016144752502], 
    [-0.0366569459438324, 0.0369462966918945, 0.0363723039627075], 
    [-0.0207552909851074, 0.0142216682434082, 0.0264238119125366], 
    [-0.0452251434326172, 0.0299248695373535, 0.0586448907852173], 
    [-0.0557426512241364, 0.0549249649047852, 0.0541806221008301], 
    [-0.057812362909317, 0.0396628379821777, 0.0786563158035278], 
    [-0.0671706199645996, 0.0808773040771484, 0.0478318333625793], 
    [-0.0459226369857788, 0.065392017364502, 0.0281721949577332], 
    [-0.0319634079933167, 0.069209098815918, 0.00454282760620117], 
    [-0.0590330362319946, 0.0918240547180176, 0.0256658792495728], 
    [-0.0437696278095245, 0.0917568206787109, 0.00676822662353516], 
    [-0.0236244201660156, 0.0427670478820801, 0.0112360715866089], 
    [-0.00896179676055908, 0.0184001922607422, 0.00638556480407715], 
    [-0.00560969114303589, 0.0337357521057129, -0.0109731554985046], 
    [-0.0163682699203491, 0.0611429214477539, -0.0121869444847107], 
    [-0.00128710269927979, 0.0502762794494629, -0.0290011167526245], 
    [-0.02717325091362, 0.0881080627441406, -0.0129422545433044], 
    [-0.0109867453575134, 0.080317497253418, -0.0350914597511292], 
    [-0.0105546116828918, 0.10465669631958, -0.0537156462669373], 
    [0.00350916385650635, 0.0615348815917969, -0.0492077469825745], 
    [0.00107496976852417, 0.0815014839172363, -0.0622037649154663], 
    [-0.0253453254699707, 0.108510494232178, -0.0310800075531006], 
    [-0.0238834619522095, 0.128593444824219, -0.0495635271072388], 
    [-0.0376120209693909, 0.13521671295166, -0.0268017053604126], 
    [-0.0411359369754791, 0.114419460296631, -0.00877058506011963], 
    [-0.0581967234611511, 0.115988731384277, 0.0121574997901917], 
    [-0.0554168224334717, 0.143585681915283, -0.00331312417984009], 
    [-0.0710579454898834, 0.168614864349365, 0.012701153755188], 
    [-0.0450781881809235, 0.162362575531006, -0.0260223150253296], 
    [-0.0562424659729004, 0.174174785614014, -0.00746774673461914], 
    [-0.0723405182361603, 0.138479709625244, 0.0219008922576904], 
    [-0.0860176384449005, 0.159544944763184, 0.0349524617195129], 
    [-0.0736579895019531, 0.11028528213501, 0.0349071025848389], 
    [-0.0845709145069122, 0.13200569152832, 0.0474219918251038], 
    [-0.0974413752555847, 0.153011798858643, 0.0602944493293762], 
    [-0.106801778078079, 0.176566600799561, 0.0735331177711487], 
    [-0.0961256623268127, 0.177772998809814, 0.0501903891563416], 
    [-0.0850693583488464, 0.195818424224854, 0.0279351472854614], 
    [0.0118443965911865, 0.079594612121582, -0.0847129225730896], 
    [-0.000627100467681885, 0.100377082824707, -0.0780265331268311], 
    [0.0190343260765076, 0.0504012107849121, -0.0738928914070129], 
    [0.021073043346405, 0.0669369697570801, -0.10351151227951], 
    [0.0197489857673645, 0.0208454132080078, -0.053466260433197], 
    [0.0261697769165039, 0.0187239646911621, -0.0740804076194763], 
    [0.0257223844528198, 0.0435037612915039, -0.102263808250427], 
    [0.0280025005340576, 0.0259275436401367, -0.0922365784645081], 
    [0.0109334588050842, 0.0407476425170898, -0.0467731952667236], 
    [0.0103438496589661, 0.0199689865112305, -0.0302004218101501], 
    [0.00545006990432739, 0.0053558349609375, -0.00894796848297119], 
    [0.0195080637931824, -0.0114455223083496, -0.0244296193122864], 
    [0.022860050201416, -0.000890254974365234, -0.0453567504882812], 
    [0.0297769904136658, -0.00288009643554688, -0.0667517781257629], 
    [0.0394350290298462, -0.0348343849182129, -0.0527569055557251], 
    [0.0409632325172424, -0.01934814453125, -0.0772967338562012], 
    [0.0574114322662354, -0.0378637313842773, -0.084104061126709], 
    [0.0628560781478882, -0.0618743896484375, -0.0718289613723755], 
    [0.0283134579658508, -0.0366554260253906, -0.0228258371353149], 
    [0.040018618106842, -0.0604596138000488, -0.0268405675888062], 
    [0.0529469847679138, -0.0683951377868652, -0.0482795238494873], 
    [0.0682883262634277, -0.0885467529296875, -0.0589086413383484], 
    [0.0570827722549438, -0.09356689453125, -0.0307576656341553], 
    [0.0516833066940308, -0.111651420593262, 0.00441473722457886], 
    [0.0810099244117737, -0.118207931518555, -0.0492529273033142], 
    [0.0409504175186157, -0.0809297561645508, -0.00833064317703247], 
    [0.0703124403953552, -0.119524955749512, -0.022888720035553], 
    [0.0712907910346985, -0.137928009033203, -0.00638192892074585], 
    [0.0886816382408142, -0.147320747375488, -0.0299809575080872], 
    [0.0822280049324036, -0.162012100219727, -0.00300323963165283], 
    [0.100715219974518, -0.145583152770996, -0.0590688586235046], 
    [0.108587145805359, -0.139925003051758, -0.0881200432777405], 
    [0.0957888960838318, -0.123671531677246, -0.0729770660400391], 
    [0.100310742855072, -0.107941627502441, -0.0959645509719849], 
    [0.0842983722686768, -0.103768348693848, -0.0724635720252991], 
    [0.0800890922546387, -0.0823183059692383, -0.0846179723739624], 
    [0.0931223630905151, -0.0807743072509766, -0.108574748039246], 
    [0.0752438902854919, -0.0581293106079102, -0.0966575741767883], 
    [0.0885469913482666, -0.0550532341003418, -0.120968580245972], 
    [0.06903076171875, -0.0332574844360352, -0.109368920326233], 
    [0.0505465269088745, -0.0145153999328613, -0.0960960984230042], 
    [0.0687244534492493, -0.0160317420959473, -0.127640724182129], 
    [0.0836882591247559, -0.0331697463989258, -0.135468721389771], 
    [0.055157482624054, -0.00406503677368164, -0.117419838905334], 
    [0.0380303859710693, 0.0190467834472656, -0.115348815917969], 
    [0.0550165176391602, 0.00878429412841797, -0.139432787895203], 
    [0.0744643807411194, -0.0113468170166016, -0.14581698179245], 
    [0.0337696671485901, 0.0292339324951172, -0.141581892967224], 
    [0.0251941680908203, 0.0468463897705078, -0.124465465545654], 
    [0.0101926922798157, 0.0711965560913086, -0.123787641525269], 
    [0.00874096155166626, 0.0940651893615723, -0.104132473468781], 
    [0.0345830321311951, 0.0036015510559082, -0.0876942873001099], 
    [0.106011569499969, -0.0729885101318359, -0.129967033863068], 
    [0.113180041313171, -0.0995769500732422, -0.121854543685913], 
    [0.116781055927277, -0.128937721252441, -0.112526535987854], 
    [0.0716546177864075, -0.171501159667969, 0.0196662545204163], 
    [0.0632362961769104, -0.145692825317383, 0.0177159309387207], 
    [0.0543274879455566, -0.163539886474609, 0.0449205040931702], 
    [0.044042706489563, -0.133871078491211, 0.0346924662590027], 
    [0.0308921933174133, -0.106049537658691, 0.0304856300354004], 
    [0.0316043496131897, -0.145562171936035, 0.0654319524765015], 
    [0.0273074507713318, -0.122373580932617, 0.0488693714141846], 
    [0.0130192637443542, -0.102289199829102, 0.0537139773368835], 
    [0.015663206577301, -0.120364189147949, 0.0668007731437683], 
    [0.000185370445251465, -0.101724624633789, 0.0755130052566528], 
    [0.00741004943847656, -0.129477500915527, 0.0876421928405762], 
    [-0.00273466110229492, -0.130294799804688, 0.114719331264496], 
    [0.0212033987045288, -0.156526565551758, 0.0963912606239319], 
    [-0.00876754522323608, -0.105877876281738, 0.10034316778183], 
    [0.0407758951187134, -0.175041198730469, 0.0741480588912964], 
    [0.014549732208252, -0.0855693817138672, 0.0384181141853333], 
    [0.00423985719680786, -0.0639214515686035, 0.0372334718704224], 
    [0.0252346396446228, -0.0805273056030273, 0.0151814818382263], 
    [0.0238203406333923, -0.0531249046325684, -0.00365477800369263], 
    [0.0123806595802307, -0.0544142723083496, 0.0183143019676208], 
    [0.00514626502990723, -0.0298571586608887, 0.0149651765823364], 
    [-0.00104296207427979, -0.0414652824401855, 0.0317662954330444], 
    [0.0154747366905212, -0.0209388732910156, -0.00476545095443726], 
    [-0.00231993198394775, -0.00485515594482422, 0.0132246017456055], 
    [-0.106201708316803, 0.130989551544189, 0.133479297161102], 
    [-0.102866530418396, 0.0996074676513672, 0.140037775039673], 
    [-0.096405565738678, 0.110253810882568, 0.118003845214844], 
    [-0.0968051254749298, 0.135246753692627, 0.108155608177185], 
    [-0.0845029950141907, 0.136320114135742, 0.083073616027832], 
    [-0.0971041321754456, 0.161471843719482, 0.0973832011222839], 
    [-0.0850409865379333, 0.107029438018799, 0.0951204895973206], 
    [-0.0723087787628174, 0.112317085266113, 0.0705700516700745], 
    [-0.0671077370643616, 0.0799355506896973, 0.0864822268486023], 
    [-0.0838166475296021, 0.0826621055603027, 0.118076384067535], 
    [-0.0625292360782623, 0.0575647354125977, 0.111372232437134], 
    [-0.0754832327365875, 0.0577945709228516, 0.13515704870224], 
    [-0.0928559005260468, 0.0724649429321289, 0.150849580764771], 
    [-0.0568182766437531, 0.0365848541259766, 0.133521258831024], 
    [-0.0436415374279022, 0.0289998054504395, 0.109292149543762], 
    [-0.0405341684818268, 0.00662660598754883, 0.131738781929016], 
    [-0.0310593843460083, 0.000804424285888672, 0.103324890136719], 
    [-0.0298787653446198, -0.022308349609375, 0.118525564670563], 
    [-0.0210832953453064, -0.0242376327514648, 0.0963568687438965], 
    [-0.0235967636108398, -0.0474076271057129, 0.129204571247101], 
    [-0.0172111988067627, -0.0481524467468262, 0.105995118618011], 
    [-0.0125940442085266, -0.0727090835571289, 0.120226979255676], 
    [-0.00389838218688965, -0.0701417922973633, 0.0951586365699768], 
    [-0.00778156518936157, -0.043766975402832, 0.0839207768440247], 
    [0.00659763813018799, -0.0662097930908203, 0.0697317123413086], 
    [-0.00108695030212402, -0.0328607559204102, 0.0613359212875366], 
    [-0.0174551606178284, -0.00857400894165039, 0.0742430090904236], 
    [-0.00356805324554443, -0.00527381896972656, 0.0471384525299072], 
    [-0.0325125157833099, 0.0203313827514648, 0.0843386650085449], 
    [-0.0212539434432983, 0.0176048278808594, 0.0596016049385071], 
    [-0.0266569554805756, 0.0469465255737305, 0.0463722944259644], 
    [-0.0107553005218506, 0.0242218971252441, 0.0364238023757935], 
    [-0.0352251529693604, 0.0399250984191895, 0.0686448812484741], 
    [-0.0457426607608795, 0.0649251937866211, 0.0641806125640869], 
    [-0.0478123724460602, 0.0496630668640137, 0.0886563062667847], 
    [-0.0571706295013428, 0.0908775329589844, 0.0578318238258362], 
    [-0.035922646522522, 0.0753922462463379, 0.03817218542099], 
    [-0.0219634175300598, 0.0792093276977539, 0.014542818069458], 
    [-0.0490330457687378, 0.101824283599854, 0.0356658697128296], 
    [-0.0337696373462677, 0.101757049560547, 0.016768217086792], 
    [-0.0136244297027588, 0.052767276763916, 0.0212360620498657], 
    [0.00103819370269775, 0.0284004211425781, 0.016385555267334], 
    [0.00439029932022095, 0.0437359809875488, -0.000973165035247803], 
    [-0.00636827945709229, 0.0711431503295898, -0.00218695402145386], 
    [0.00871288776397705, 0.0602765083312988, -0.0190011262893677], 
    [-0.0171732306480408, 0.0981082916259766, -0.00294226408004761], 
    [-0.000986754894256592, 0.0903177261352539, -0.0250914692878723], 
    [-0.00055462121963501, 0.114656925201416, -0.0437156558036804], 
    [0.0135091543197632, 0.0715351104736328, -0.0392077565193176], 
    [0.011074960231781, 0.0915017127990723, -0.0522037744522095], 
    [-0.0153453350067139, 0.118510723114014, -0.0210800170898438], 
    [-0.0138834714889526, 0.138593673706055, -0.0395635366439819], 
    [-0.027612030506134, 0.145216941833496, -0.0168017148971558], 
    [-0.0311359465122223, 0.124419689178467, 0.00122940540313721], 
    [-0.0481967329978943, 0.125988960266113, 0.0221574902534485], 
    [-0.0454168319702148, 0.153585910797119, 0.00668686628341675], 
    [-0.0610579550266266, 0.178615093231201, 0.0227011442184448], 
    [-0.0350781977176666, 0.172362804412842, -0.0160223245620728], 
    [-0.0462424755096436, 0.18417501449585, 0.0025322437286377], 
    [-0.0623405277729034, 0.14847993850708, 0.0319008827209473], 
    [-0.0760176479816437, 0.16954517364502, 0.0449524521827698], 
    [-0.0636579990386963, 0.120285511016846, 0.0449070930480957], 
    [-0.0745709240436554, 0.142005920410156, 0.0574219822883606], 
    [-0.0874413847923279, 0.163012027740479, 0.0702944397926331], 
    [-0.0968017876148224, 0.186566829681396, 0.0835331082344055], 
    [-0.0861256718635559, 0.18777322769165, 0.0601903796195984], 
    [-0.0750693678855896, 0.205818653106689, 0.0379351377487183], 
    [0.0218443870544434, 0.089594841003418, -0.0747129321098328], 
    [0.00937288999557495, 0.110377311706543, -0.0680265426635742], 
    [0.0290343165397644, 0.060401439666748, -0.0638929009437561], 
    [0.0310730338096619, 0.076937198638916, -0.0935115218162537], 
    [0.0297489762306213, 0.0308456420898438, -0.0434662699699402], 
    [0.0361697673797607, 0.028724193572998, -0.0640804171562195], 
    [0.0357223749160767, 0.0535039901733398, -0.0922638177871704], 
    [0.0380024909973145, 0.0359277725219727, -0.0822365880012512], 
    [0.0209334492683411, 0.0507478713989258, -0.0367732048034668], 
    [0.0203438401222229, 0.0299692153930664, -0.0202004313468933], 
    [0.0154500603675842, 0.0153560638427734, 0.00105202198028564], 
    [0.0295080542564392, -0.00144529342651367, -0.0144296288490295], 
    [0.0328600406646729, 0.0091099739074707, -0.0353567600250244], 
    [0.0397769808769226, 0.00712013244628906, -0.0567517876625061], 
    [0.049435019493103, -0.024834156036377, -0.0427569150924683], 
    [0.0509632229804993, -0.00934791564941406, -0.0672967433929443], 
    [0.0674114227294922, -0.0278635025024414, -0.0741040706634521], 
    [0.072856068611145, -0.0518741607666016, -0.0618289709091187], 
    [0.0383134484291077, -0.0266551971435547, -0.0128258466720581], 
    [0.0500186085700989, -0.0504593849182129, -0.0168405771255493], 
    [0.0629469752311707, -0.0583949089050293, -0.0382795333862305], 
    [0.0782883167266846, -0.0785465240478516, -0.0489086508750916], 
    [0.0670827627182007, -0.0835666656494141, -0.0207576751708984], 
    [0.0616832971572876, -0.101651191711426, 0.0144147276878357], 
    [0.0910099148750305, -0.108207702636719, -0.0392529368400574], 
    [0.0509504079818726, -0.0709295272827148, 0.00166934728622437], 
    [0.0803124308586121, -0.109524726867676, -0.0128887295722961], 
    [0.0812907814979553, -0.127927780151367, 0.00361806154251099], 
    [0.098681628704071, -0.137320518493652, -0.0199809670448303], 
    [0.0922279953956604, -0.152011871337891, 0.006996750831604], 
    [0.110715210437775, -0.13558292388916, -0.0490688681602478], 
    [0.118587136268616, -0.129924774169922, -0.0781200528144836], 
    [0.105788886547089, -0.11367130279541, -0.0629770755767822], 
    [0.110310733318329, -0.0979413986206055, -0.085964560508728], 
    [0.0942983627319336, -0.0937681198120117, -0.0624635815620422], 
    [0.0900890827178955, -0.0723180770874023, -0.0746179819107056], 
    [0.103122353553772, -0.0707740783691406, -0.0985747575759888], 
    [0.0852438807487488, -0.0481290817260742, -0.0866575837135315], 
    [0.0985469818115234, -0.0450530052185059, -0.110968589782715], 
    [0.0790307521820068, -0.0232572555541992, -0.0993689298629761], 
    [0.0605465173721313, -0.00451517105102539, -0.0860961079597473], 
    [0.0787244439125061, -0.00603151321411133, -0.117640733718872], 
    [0.0936882495880127, -0.0231695175170898, -0.125468730926514], 
    [0.0651574730873108, 0.0059351921081543, -0.107419848442078], 
    [0.0480303764343262, 0.0290470123291016, -0.105348825454712], 
    [0.065016508102417, 0.0187845230102539, -0.129432797431946], 
    [0.0844643712043762, -0.00134658813476562, -0.135816991329193], 
    [0.0437696576118469, 0.0392341613769531, -0.131581902503967], 
    [0.0351941585540771, 0.0568466186523438, -0.114465475082397], 
    [0.0201926827430725, 0.0811967849731445, -0.113787651062012], 
    [0.0187409520149231, 0.104065418243408, -0.0941324830055237], 
    [0.0445830225944519, 0.0136017799377441, -0.077694296836853], 
    [0.116011559963226, -0.06298828125, -0.119967043399811], 
    [0.123180031776428, -0.0895767211914062, -0.111854553222656], 
    [0.126781046390533, -0.118937492370605, -0.102526545524597], 
    [0.0816546082496643, -0.161500930786133, 0.0296662449836731], 
    [0.0732362866401672, -0.135692596435547, 0.0277159214019775], 
    [0.0643274784088135, -0.153539657592773, 0.054920494556427], 
    [0.0540426969528198, -0.123870849609375, 0.0446924567222595], 
    [0.0408921837806702, -0.0960493087768555, 0.0404856204986572], 
    [0.0416043400764465, -0.135561943054199, 0.0754319429397583], 
    [0.0373074412345886, -0.112373352050781, 0.0588693618774414], 
    [0.0230192542076111, -0.0922889709472656, 0.0637139678001404], 
    [0.0256631970405579, -0.110363960266113, 0.0768007636070251], 
    [0.0101853609085083, -0.0917243957519531, 0.0855129957199097], 
    [0.0174100399017334, -0.119477272033691, 0.097642183303833], 
    [0.00726532936096191, -0.120294570922852, 0.124719321727753], 
    [0.0312033891677856, -0.146526336669922, 0.106391251087189], 
    [0.00123244524002075, -0.0958776473999023, 0.110343158245087], 
    [0.0507758855819702, -0.165040969848633, 0.0841480493545532], 
    [0.0245497226715088, -0.0755691528320312, 0.0484181046485901], 
    [0.0142398476600647, -0.0539212226867676, 0.0472334623336792], 
    [0.0352346301078796, -0.0705270767211914, 0.0251814723014832], 
    [0.0338203310966492, -0.0431246757507324, 0.00634521245956421], 
    [0.0223806500434875, -0.0444140434265137, 0.0283142924308777], 
    [0.0151462554931641, -0.0198569297790527, 0.0249651670455933], 
    [0.00895702838897705, -0.0314650535583496, 0.0417662858963013], 
    [0.0254747271537781, -0.0109386444091797, 0.00523453950881958], 
    [0.00768005847930908, 0.00514507293701172, 0.0232245922088623]
] # synapse_vertex_list

synapse_wall_list = [
    [0, 2, 1], 
    [2, 0, 3], 
    [4, 3, 5], 
    [6, 3, 4], 
    [6, 2, 3], 
    [6, 4, 7], 
    [8, 6, 7], 
    [9, 6, 8], 
    [2, 6, 9], 
    [8, 10, 9], 
    [1, 2, 9], 
    [10, 11, 9], 
    [12, 9, 11], 
    [1, 9, 12], 
    [13, 11, 10], 
    [15, 13, 14], 
    [14, 13, 10], 
    [15, 16, 17], 
    [15, 14, 16], 
    [20, 17, 18], 
    [18, 17, 16], 
    [19, 17, 20], 
    [19, 20, 21], 
    [22, 21, 20], 
    [20, 23, 22], 
    [20, 18, 23], 
    [18, 26, 23], 
    [22, 23, 24], 
    [23, 25, 24], 
    [23, 26, 25], 
    [26, 27, 25], 
    [26, 29, 27], 
    [28, 29, 26], 
    [16, 28, 26], 
    [16, 26, 18], 
    [27, 29, 31], 
    [29, 30, 31], 
    [29, 32, 30], 
    [29, 28, 32], 
    [32, 34, 33], 
    [30, 32, 33], 
    [28, 34, 32], 
    [34, 8, 33], 
    [34, 10, 8], 
    [14, 34, 28], 
    [10, 34, 14], 
    [8, 35, 33], 
    [36, 33, 35], 
    [33, 36, 30], 
    [35, 38, 36], 
    [36, 39, 37], 
    [40, 36, 37], 
    [39, 36, 38], 
    [40, 30, 36], 
    [31, 40, 41], 
    [40, 42, 41], 
    [40, 43, 42], 
    [40, 37, 43], 
    [30, 40, 31], 
    [37, 45, 43], 
    [43, 44, 42], 
    [43, 46, 44], 
    [43, 45, 46], 
    [49, 46, 47], 
    [46, 50, 47], 
    [45, 50, 46], 
    [48, 46, 49], 
    [44, 46, 48], 
    [51, 50, 52], 
    [47, 50, 51], 
    [50, 53, 52], 
    [53, 50, 45], 
    [39, 53, 45], 
    [54, 53, 39], 
    [53, 54, 55], 
    [53, 55, 52], 
    [56, 58, 55], 
    [59, 56, 55], 
    [54, 59, 55], 
    [55, 58, 57], 
    [52, 55, 57], 
    [62, 60, 59], 
    [60, 56, 59], 
    [61, 59, 54], 
    [62, 59, 61], 
    [7, 4, 62], 
    [4, 63, 62], 
    [7, 62, 61], 
    [62, 63, 60], 
    [5, 64, 63], 
    [64, 65, 63], 
    [63, 65, 60], 
    [5, 63, 4], 
    [65, 66, 60], 
    [66, 56, 60], 
    [38, 35, 61], 
    [35, 7, 61], 
    [61, 54, 38], 
    [39, 38, 54], 
    [67, 49, 68], 
    [69, 49, 67], 
    [69, 48, 49], 
    [69, 67, 70], 
    [73, 69, 70], 
    [75, 69, 71], 
    [69, 72, 71], 
    [72, 69, 74], 
    [69, 75, 48], 
    [74, 69, 73], 
    [44, 48, 75], 
    [76, 44, 75], 
    [76, 75, 71], 
    [79, 76, 71], 
    [77, 76, 78], 
    [76, 77, 42], 
    [78, 76, 79], 
    [76, 42, 44], 
    [79, 71, 80], 
    [81, 79, 80], 
    [81, 78, 79], 
    [81, 80, 82], 
    [83, 81, 82], 
    [84, 81, 83], 
    [87, 81, 84], 
    [81, 85, 78], 
    [85, 81, 86], 
    [86, 81, 87], 
    [87, 84, 88], 
    [89, 87, 88], 
    [89, 86, 87], 
    [90, 92, 89], 
    [93, 90, 89], 
    [89, 88, 91], 
    [93, 89, 91], 
    [89, 92, 86], 
    [95, 94, 93], 
    [94, 90, 93], 
    [93, 91, 95], 
    [91, 97, 95], 
    [94, 95, 96], 
    [98, 97, 99], 
    [97, 91, 99], 
    [99, 100, 98], 
    [99, 101, 100], 
    [99, 91, 101], 
    [91, 88, 101], 
    [101, 88, 102], 
    [101, 102, 100], 
    [103, 102, 104], 
    [102, 103, 100], 
    [102, 88, 84], 
    [84, 104, 102], 
    [104, 105, 103], 
    [105, 104, 106], 
    [104, 83, 106], 
    [84, 83, 104], 
    [107, 110, 106], 
    [83, 107, 106], 
    [109, 106, 108], 
    [106, 110, 108], 
    [106, 109, 105], 
    [111, 112, 110], 
    [107, 111, 110], 
    [108, 110, 112], 
    [108, 112, 113], 
    [112, 111, 114], 
    [114, 111, 115], 
    [111, 73, 115], 
    [70, 116, 115], 
    [73, 70, 115], 
    [117, 116, 70], 
    [67, 117, 70], 
    [68, 117, 67], 
    [108, 113, 109], 
    [111, 74, 73], 
    [111, 118, 74], 
    [111, 107, 118], 
    [118, 80, 72], 
    [82, 80, 118], 
    [72, 74, 118], 
    [107, 82, 118], 
    [82, 107, 83], 
    [119, 103, 105], 
    [120, 103, 119], 
    [100, 120, 121], 
    [120, 100, 103], 
    [121, 98, 100], 
    [123, 94, 96], 
    [122, 123, 96], 
    [125, 90, 123], 
    [90, 94, 123], 
    [124, 125, 123], 
    [122, 124, 123], 
    [90, 125, 126], 
    [125, 128, 126], 
    [127, 125, 124], 
    [128, 125, 127], 
    [130, 128, 127], 
    [130, 129, 128], 
    [129, 126, 128], 
    [132, 131, 130], 
    [131, 129, 130], 
    [132, 130, 127], 
    [134, 132, 127], 
    [133, 132, 134], 
    [132, 133, 135], 
    [132, 135, 131], 
    [131, 135, 22], 
    [21, 22, 135], 
    [134, 127, 136], 
    [136, 127, 124], 
    [22, 24, 131], 
    [131, 24, 129], 
    [24, 137, 129], 
    [129, 137, 126], 
    [137, 24, 138], 
    [139, 137, 138], 
    [137, 139, 126], 
    [139, 140, 92], 
    [139, 141, 140], 
    [90, 139, 92], 
    [138, 141, 139], 
    [90, 126, 139], 
    [141, 142, 140], 
    [141, 143, 142], 
    [141, 138, 143], 
    [25, 27, 143], 
    [142, 143, 27], 
    [25, 143, 138], 
    [142, 144, 140], 
    [27, 145, 142], 
    [144, 142, 145], 
    [77, 144, 145], 
    [41, 77, 145], 
    [31, 41, 145], 
    [145, 27, 31], 
    [85, 144, 78], 
    [144, 77, 78], 
    [140, 144, 85], 
    [86, 140, 85], 
    [86, 92, 140], 
    [24, 25, 138], 
    [80, 71, 72], 
    [77, 41, 42], 
    [45, 37, 39], 
    [8, 7, 35], 
    [16, 14, 28], 
    [146, 147, 148], 
    [148, 149, 146], 
    [150, 151, 149], 
    [152, 150, 149], 
    [152, 149, 148], 
    [152, 153, 150], 
    [154, 153, 152], 
    [155, 154, 152], 
    [148, 155, 152], 
    [154, 155, 156], 
    [147, 155, 148], 
    [156, 155, 157], 
    [158, 157, 155], 
    [147, 158, 155], 
    [159, 156, 157], 
    [161, 160, 159], 
    [160, 156, 159], 
    [161, 163, 162], 
    [161, 162, 160], 
    [166, 164, 163], 
    [164, 162, 163], 
    [165, 166, 163], 
    [165, 167, 166], 
    [168, 166, 167], 
    [166, 168, 169], 
    [166, 169, 164], 
    [164, 169, 172], 
    [168, 170, 169], 
    [169, 170, 171], 
    [169, 171, 172], 
    [172, 171, 173], 
    [172, 173, 175], 
    [174, 172, 175], 
    [162, 172, 174], 
    [162, 164, 172], 
    [173, 177, 175], 
    [175, 177, 176], 
    [175, 176, 178], 
    [175, 178, 174], 
    [178, 179, 180], 
    [176, 179, 178], 
    [174, 178, 180], 
    [180, 179, 154], 
    [180, 154, 156], 
    [160, 174, 180], 
    [156, 160, 180], 
    [154, 179, 181], 
    [182, 181, 179], 
    [179, 176, 182], 
    [181, 182, 184], 
    [182, 183, 185], 
    [186, 183, 182], 
    [185, 184, 182], 
    [186, 182, 176], 
    [177, 187, 186], 
    [186, 187, 188], 
    [186, 188, 189], 
    [186, 189, 183], 
    [176, 177, 186], 
    [183, 189, 191], 
    [189, 188, 190], 
    [189, 190, 192], 
    [189, 192, 191], 
    [195, 193, 192], 
    [192, 193, 196], 
    [191, 192, 196], 
    [194, 195, 192], 
    [190, 194, 192], 
    [197, 198, 196], 
    [193, 197, 196], 
    [196, 198, 199], 
    [199, 191, 196], 
    [185, 191, 199], 
    [200, 185, 199], 
    [199, 201, 200], 
    [199, 198, 201], 
    [202, 201, 204], 
    [205, 201, 202], 
    [200, 201, 205], 
    [201, 203, 204], 
    [198, 203, 201], 
    [208, 205, 206], 
    [206, 205, 202], 
    [207, 200, 205], 
    [208, 207, 205], 
    [153, 208, 150], 
    [150, 208, 209], 
    [153, 207, 208], 
    [208, 206, 209], 
    [151, 209, 210], 
    [210, 209, 211], 
    [209, 206, 211], 
    [151, 150, 209], 
    [211, 206, 212], 
    [212, 206, 202], 
    [184, 207, 181], 
    [181, 207, 153], 
    [207, 184, 200], 
    [185, 200, 184], 
    [213, 214, 195], 
    [215, 213, 195], 
    [215, 195, 194], 
    [215, 216, 213], 
    [219, 216, 215], 
    [221, 217, 215], 
    [215, 217, 218], 
    [218, 220, 215], 
    [215, 194, 221], 
    [220, 219, 215], 
    [190, 221, 194], 
    [222, 221, 190], 
    [222, 217, 221], 
    [225, 217, 222], 
    [223, 224, 222], 
    [222, 188, 223], 
    [224, 225, 222], 
    [222, 190, 188], 
    [225, 226, 217], 
    [227, 226, 225], 
    [227, 225, 224], 
    [227, 228, 226], 
    [229, 228, 227], 
    [230, 229, 227], 
    [233, 230, 227], 
    [227, 224, 231], 
    [231, 232, 227], 
    [232, 233, 227], 
    [233, 234, 230], 
    [235, 234, 233], 
    [235, 233, 232], 
    [236, 235, 238], 
    [239, 235, 236], 
    [235, 237, 234], 
    [239, 237, 235], 
    [235, 232, 238], 
    [241, 239, 240], 
    [240, 239, 236], 
    [239, 241, 237], 
    [237, 241, 243], 
    [240, 242, 241], 
    [244, 245, 243], 
    [243, 245, 237], 
    [245, 244, 246], 
    [245, 246, 247], 
    [245, 247, 237], 
    [237, 247, 234], 
    [247, 248, 234], 
    [247, 246, 248], 
    [249, 250, 248], 
    [248, 246, 249], 
    [248, 230, 234], 
    [230, 248, 250], 
    [250, 249, 251], 
    [251, 252, 250], 
    [250, 252, 229], 
    [230, 250, 229], 
    [253, 252, 256], 
    [229, 252, 253], 
    [255, 254, 252], 
    [252, 254, 256], 
    [252, 251, 255], 
    [257, 256, 258], 
    [253, 256, 257], 
    [254, 258, 256], 
    [254, 259, 258], 
    [258, 260, 257], 
    [260, 261, 257], 
    [257, 261, 219], 
    [216, 261, 262], 
    [219, 261, 216], 
    [263, 216, 262], 
    [213, 216, 263], 
    [214, 213, 263], 
    [254, 255, 259], 
    [257, 219, 220], 
    [257, 220, 264], 
    [257, 264, 253], 
    [264, 218, 226], 
    [228, 264, 226], 
    [218, 264, 220], 
    [253, 264, 228], 
    [228, 229, 253], 
    [265, 251, 249], 
    [266, 265, 249], 
    [246, 267, 266], 
    [266, 249, 246], 
    [267, 246, 244], 
    [269, 242, 240], 
    [268, 242, 269], 
    [271, 269, 236], 
    [236, 269, 240], 
    [270, 269, 271], 
    [268, 269, 270], 
    [236, 272, 271], 
    [271, 272, 274], 
    [273, 270, 271], 
    [274, 273, 271], 
    [276, 273, 274], 
    [276, 274, 275], 
    [275, 274, 272], 
    [278, 276, 277], 
    [277, 276, 275], 
    [278, 273, 276], 
    [280, 273, 278], 
    [279, 280, 278], 
    [278, 281, 279], 
    [278, 277, 281], 
    [277, 168, 281], 
    [167, 281, 168], 
    [280, 282, 273], 
    [282, 270, 273], 
    [168, 277, 170], 
    [277, 275, 170], 
    [170, 275, 283], 
    [275, 272, 283], 
    [283, 284, 170], 
    [285, 284, 283], 
    [283, 272, 285], 
    [285, 238, 286], 
    [285, 286, 287], 
    [236, 238, 285], 
    [284, 285, 287], 
    [236, 285, 272], 
    [287, 286, 288], 
    [287, 288, 289], 
    [287, 289, 284], 
    [171, 289, 173], 
    [288, 173, 289], 
    [171, 284, 289], 
    [288, 286, 290], 
    [173, 288, 291], 
    [290, 291, 288], 
    [223, 291, 290], 
    [187, 291, 223], 
    [177, 291, 187], 
    [291, 177, 173], 
    [231, 224, 290], 
    [290, 224, 223], 
    [286, 231, 290], 
    [232, 231, 286], 
    [232, 286, 238], 
    [170, 284, 171], 
    [226, 218, 217], 
    [223, 188, 187], 
    [191, 185, 183], 
    [154, 181, 153], 
    [162, 174, 160], 
    [203, 57, 58], 
    [57, 203, 198], 
    [52, 198, 197], 
    [51, 197, 193], 
    [195, 49, 47], 
    [68, 49, 195], 
    [68, 214, 263], 
    [262, 116, 117], 
    [116, 262, 261], 
    [260, 114, 115], 
    [112, 114, 260], 
    [259, 113, 112], 
    [255, 109, 113], 
    [251, 105, 109], 
    [105, 251, 265], 
    [119, 265, 266], 
    [267, 121, 120], 
    [98, 121, 267], 
    [97, 98, 244], 
    [95, 97, 243], 
    [96, 95, 241], 
    [122, 96, 242], 
    [124, 122, 268], 
    [136, 124, 270], 
    [134, 136, 282], 
    [133, 134, 280], 
    [135, 133, 279], 
    [21, 135, 281], 
    [19, 21, 167], 
    [17, 19, 165], 
    [15, 17, 163], 
    [13, 15, 161], 
    [11, 13, 159], 
    [12, 11, 157], 
    [1, 12, 158], 
    [0, 1, 147], 
    [149, 3, 0], 
    [5, 3, 149], 
    [64, 5, 151], 
    [211, 65, 64], 
    [66, 65, 211], 
    [202, 56, 66], 
    [58, 56, 202], 
    [203, 58, 204], 
    [57, 198, 52], 
    [52, 197, 51], 
    [51, 193, 47], 
    [195, 47, 193], 
    [68, 195, 214], 
    [68, 263, 117], 
    [262, 117, 263], 
    [116, 261, 115], 
    [260, 115, 261], 
    [112, 260, 258], 
    [259, 112, 258], 
    [255, 113, 259], 
    [251, 109, 255], 
    [105, 265, 119], 
    [119, 266, 120], 
    [267, 120, 266], 
    [98, 267, 244], 
    [97, 244, 243], 
    [95, 243, 241], 
    [96, 241, 242], 
    [122, 242, 268], 
    [124, 268, 270], 
    [136, 270, 282], 
    [134, 282, 280], 
    [133, 280, 279], 
    [135, 279, 281], 
    [21, 281, 167], 
    [19, 167, 165], 
    [17, 165, 163], 
    [15, 163, 161], 
    [13, 161, 159], 
    [11, 159, 157], 
    [12, 157, 158], 
    [1, 158, 147], 
    [0, 147, 146], 
    [149, 0, 146], 
    [5, 149, 151], 
    [64, 151, 210], 
    [211, 64, 210], 
    [66, 211, 212], 
    [202, 66, 212], 
    [58, 202, 204]
] # synapse_wall_list

synapse = m.GeometryObject(
    name = 'synapse',
    vertex_list = synapse_vertex_list,
    wall_list = synapse_wall_list,
    surface_regions = []
)
# ^^^^ synapse ^^^^

