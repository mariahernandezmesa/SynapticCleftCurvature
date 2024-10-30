import mcell as m

# ---- PSD ----
PSD_vertex_list = [
    [1.75957608222961, 1.41852629184723, -0.126906141638756], 
    [1.77854073047638, 1.43588006496429, -0.149725988507271], 
    [1.73081827163696, 1.44063150882721, -0.121603652834892], 
    [1.78703284263611, 1.40777373313904, -0.139504998922348], 
    [1.75390422344208, 1.45937025547028, -0.139692410826683], 
    [1.78035092353821, 1.46415877342224, -0.162858605384827], 
    [1.72283947467804, 1.46879804134369, -0.127974718809128], 
    [1.7588769197464, 1.48681831359863, -0.160308942198753], 
    [1.72506678104401, 1.49457108974457, -0.145105317234993], 
    [1.69689273834229, 1.48820579051971, -0.12319977581501], 
    [1.69409310817719, 1.51538443565369, -0.141323134303093], 
    [1.71368181705475, 1.52597081661224, -0.166714265942574], 
    [1.73894345760345, 1.50640153884888, -0.167185366153717], 
    [1.75955367088318, 1.50594115257263, -0.184045821428299], 
    [1.73678493499756, 1.52242815494537, -0.184840366244316], 
    [1.71966326236725, 1.5406391620636, -0.197809502482414], 
    [1.75032198429108, 1.52506113052368, -0.209655404090881], 
    [1.77178549766541, 1.51791679859161, -0.225669130682945], 
    [1.73309600353241, 1.54749739170074, -0.2234116345644], 
    [1.77762413024902, 1.50257563591003, -0.206479206681252], 
    [1.76183462142944, 1.53890585899353, -0.23853787779808], 
    [1.78502786159515, 1.52389895915985, -0.242598637938499], 
    [1.74756669998169, 1.56006813049316, -0.239750668406487], 
    [1.72589540481567, 1.57372260093689, -0.230707138776779], 
    [1.70200526714325, 1.58943235874176, -0.223132371902466], 
    [1.70788395404816, 1.56391131877899, -0.211519435048103], 
    [1.68100965023041, 1.58086681365967, -0.209576651453972], 
    [1.68986666202545, 1.55394649505615, -0.187790274620056], 
    [1.66550028324127, 1.55695998668671, -0.167306900024414], 
    [1.65984427928925, 1.57666313648224, -0.189489185810089], 
    [1.68533658981323, 1.53748083114624, -0.160286352038383], 
    [1.66186845302582, 1.53818666934967, -0.140252098441124], 
    [1.66719269752502, 1.51254343986511, -0.124864339828491], 
    [1.63230967521667, 1.55296277999878, -0.13412481546402], 
    [1.63911759853363, 1.52767634391785, -0.121852740645409], 
    [1.64640331268311, 1.56185615062714, -0.150032997131348], 
    [1.64086163043976, 1.57976615428925, -0.168004214763641], 
    [1.62576925754547, 1.57832181453705, -0.146456763148308], 
    [1.79452180862427, 1.50479340553284, -0.232992619276047], 
    [1.81813848018646, 1.4950202703476, -0.245473951101303], 
    [1.8025279045105, 1.48389256000519, -0.213711336255074], 
    [1.80111682415009, 1.46443605422974, -0.188647404313087], 
    [1.78081691265106, 1.48531198501587, -0.184146612882614], 
    [1.83094871044159, 1.47595548629761, -0.228267252445221], 
    [1.82109868526459, 1.46273910999298, -0.20825457572937], 
    [1.82576560974121, 1.44380879402161, -0.192717269062996], 
    [1.84664559364319, 1.44936275482178, -0.214371204376221], 
    [1.85231053829193, 1.41748213768005, -0.193256005644798], 
    [1.82522583007812, 1.39713251590729, -0.179264426231384], 
    [1.8211807012558, 1.4237095117569, -0.179508656263351], 
    [1.84979212284088, 1.37853503227234, -0.17978747189045], 
    [1.82567405700684, 1.37252378463745, -0.161958038806915], 
    [1.80695521831512, 1.39497947692871, -0.159153744578362], 
    [1.80079126358032, 1.37820029258728, -0.142144814133644], 
    [1.80082523822784, 1.41979968547821, -0.162174835801125], 
    [1.80045783519745, 1.44294369220734, -0.171920329332352]
] # PSD_vertex_list

PSD_wall_list = [
    [0, 4, 1], 
    [1, 3, 0], 
    [0, 2, 4], 
    [4, 5, 1], 
    [7, 5, 4], 
    [2, 6, 4], 
    [8, 4, 6], 
    [8, 7, 4], 
    [9, 10, 8], 
    [8, 6, 9], 
    [10, 11, 8], 
    [8, 12, 7], 
    [11, 12, 8], 
    [12, 11, 14], 
    [13, 7, 12], 
    [14, 13, 12], 
    [15, 16, 14], 
    [11, 15, 14], 
    [14, 16, 13], 
    [13, 16, 19], 
    [15, 18, 16], 
    [16, 20, 17], 
    [19, 16, 17], 
    [16, 18, 20], 
    [17, 20, 21], 
    [22, 20, 18], 
    [23, 22, 18], 
    [25, 24, 23], 
    [25, 23, 18], 
    [24, 25, 26], 
    [26, 25, 27], 
    [18, 15, 25], 
    [25, 15, 27], 
    [27, 15, 11], 
    [30, 28, 27], 
    [28, 29, 27], 
    [27, 11, 30], 
    [27, 29, 26], 
    [30, 11, 10], 
    [10, 31, 30], 
    [31, 28, 30], 
    [31, 10, 32], 
    [31, 32, 34], 
    [34, 33, 31], 
    [35, 31, 33], 
    [35, 28, 31], 
    [37, 35, 33], 
    [35, 36, 28], 
    [36, 35, 37], 
    [29, 28, 36], 
    [9, 32, 10], 
    [21, 38, 17], 
    [17, 38, 19], 
    [38, 39, 40], 
    [38, 40, 19], 
    [42, 40, 41], 
    [41, 40, 44], 
    [42, 19, 40], 
    [40, 39, 43], 
    [44, 40, 43], 
    [44, 45, 41], 
    [46, 44, 43], 
    [45, 44, 46], 
    [45, 46, 47], 
    [49, 45, 47], 
    [48, 49, 47], 
    [47, 50, 48], 
    [51, 48, 50], 
    [52, 48, 51], 
    [53, 52, 51], 
    [53, 3, 52], 
    [54, 52, 3], 
    [54, 48, 52], 
    [55, 54, 1], 
    [1, 54, 3], 
    [54, 55, 49], 
    [49, 48, 54], 
    [5, 55, 1], 
    [45, 49, 55], 
    [55, 41, 45], 
    [5, 41, 55], 
    [13, 19, 42], 
    [7, 13, 42], 
    [7, 42, 5], 
    [5, 42, 41]
] # PSD_wall_list

PSD = m.GeometryObject(
    name = 'PSD',
    vertex_list = PSD_vertex_list,
    wall_list = PSD_wall_list,
    surface_regions = []
)
# ^^^^ PSD ^^^^


