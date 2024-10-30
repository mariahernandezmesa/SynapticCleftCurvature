import mcell as m

# ---- PSD ----
PSD_vertex_list = [
    [0.117919683456421, 0.00224924087524414, -0.0270066261291504], 
    [0.121789693832397, -0.0278949737548828, -0.00375139713287354], 
    [0.0929758548736572, 0.0131292343139648, -0.0496044158935547], 
    [0.0988858938217163, -0.0200486183166504, -0.0236103534698486], 
    [0.0874199867248535, -0.00521469116210938, -0.0381397008895874], 
    [0.062468409538269, 0.0122933387756348, -0.0496829748153687], 
    [0.0660405158996582, -0.01495361328125, -0.0282497406005859], 
    [0.0440359115600586, -0.0153279304504395, -0.012426495552063], 
    [0.0618867874145508, -0.0345182418823242, -0.00354671478271484], 
    [0.089924693107605, -0.0369710922241211, -0.00793755054473877], 
    [0.0331891775131226, 0.00638055801391602, -0.0326611995697021], 
    [0.0224123001098633, -0.00795316696166992, 0.00435566902160645], 
    [0.0085219144821167, 0.0288047790527344, -0.0421228408813477], 
    [0.0331484079360962, 0.0332150459289551, -0.0551910400390625], 
    [0.00623869895935059, 0.0116682052612305, -0.0143135786056519], 
    [-0.0181316137313843, 0.0170979499816895, 0.000168204307556152], 
    [-0.00143182277679443, 0.00106954574584961, 0.016345739364624], 
    [-0.014798641204834, 0.0275001525878906, -0.026775598526001], 
    [-0.0154913663864136, 0.0460357666015625, -0.0523840188980103], 
    [-0.0366363525390625, 0.0386433601379395, -0.0358736515045166], 
    [-0.0363059043884277, 0.0274429321289062, -0.0136860609054565], 
    [-0.0645613670349121, 0.0320701599121094, -0.0147314071655273], 
    [-0.0465534925460815, 0.0220761299133301, 0.00835502147674561], 
    [-0.0499409437179565, 0.0109648704528809, 0.0301641225814819], 
    [-0.0795052051544189, 0.0201730728149414, 0.0191627740859985], 
    [-0.0252528190612793, 0.00928544998168945, 0.0259634256362915], 
    [-0.0366268157958984, -0.00388526916503906, 0.0464370250701904], 
    [-0.0117521286010742, -0.00958919525146484, 0.043368935585022], 
    [0.0121076107025146, -0.0169157981872559, 0.0343269109725952], 
    [-0.0250682830810547, -0.0236797332763672, 0.0656219720840454], 
    [-0.000148415565490723, -0.0329556465148926, 0.0587277412414551], 
    [0.0211803913116455, -0.0408992767333984, 0.0473791360855103], 
    [0.0314329862594604, -0.0336260795593262, 0.0264738798141479], 
    [0.0403680801391602, -0.0636825561523438, 0.0439200401306152], 
    [0.0631786584854126, -0.0684394836425781, 0.0283160209655762], 
    [0.0524420738220215, -0.0478143692016602, 0.0185089111328125], 
    [0.0611634254455566, -0.089996337890625, 0.044913649559021], 
    [0.0883364677429199, -0.0800371170043945, 0.0261144638061523], 
    [0.0765558481216431, -0.0556726455688477, 0.00909018516540527], 
    [0.104994893074036, -0.0549273490905762, 0.00746965408325195], 
    [0.0416775941848755, -0.0283632278442383, 0.00620341300964355], 
    [-0.0496107339859009, -0.0134849548339844, 0.0648801326751709], 
    [-0.0627943277359009, 0.000396251678466797, 0.0485221147537231], 
    [-0.0869306325912476, 0.00541830062866211, 0.0497316122055054], 
    [-0.107710719108582, 0.0179257392883301, 0.0407203435897827], 
    [-0.1104656457901, 0.0312848091125488, 0.014792799949646], 
    [-0.0945916175842285, 0.0354089736938477, -0.00975894927978516], 
    [-0.122547745704651, 0.0492057800292969, -0.00769257545471191], 
    [-0.106636881828308, 0.0546760559082031, -0.029931902885437], 
    [-0.0812022686004639, 0.0484418869018555, -0.0342276096343994], 
    [-0.0896862745285034, 0.0658807754516602, -0.0539544820785522], 
    [-0.066867470741272, 0.0580048561096191, -0.0623594522476196], 
    [-0.0586045980453491, 0.0452303886413574, -0.0415328741073608], 
    [-0.0404441356658936, 0.0548768043518066, -0.0588791370391846]
] # PSD_vertex_list

PSD_wall_list = [
    [0, 1, 3], 
    [4, 2, 0], 
    [3, 4, 0], 
    [5, 4, 6], 
    [5, 2, 4], 
    [4, 3, 6], 
    [7, 10, 6], 
    [7, 6, 8], 
    [9, 6, 3], 
    [6, 9, 8], 
    [6, 10, 5], 
    [7, 11, 10], 
    [14, 10, 11], 
    [12, 10, 14], 
    [10, 12, 13], 
    [13, 5, 10], 
    [12, 14, 17], 
    [15, 14, 16], 
    [17, 14, 15], 
    [16, 14, 11], 
    [17, 18, 12], 
    [17, 19, 18], 
    [20, 17, 15], 
    [19, 17, 20], 
    [22, 20, 15], 
    [21, 20, 22], 
    [21, 19, 20], 
    [21, 22, 24], 
    [25, 22, 15], 
    [25, 23, 22], 
    [23, 24, 22], 
    [15, 16, 25], 
    [27, 25, 16], 
    [23, 25, 26], 
    [25, 27, 26], 
    [16, 28, 27], 
    [30, 27, 28], 
    [29, 26, 27], 
    [27, 30, 29], 
    [28, 31, 30], 
    [32, 33, 31], 
    [31, 28, 32], 
    [32, 35, 33], 
    [36, 33, 34], 
    [33, 35, 34], 
    [36, 34, 37], 
    [38, 39, 37], 
    [38, 37, 34], 
    [39, 9, 1], 
    [39, 38, 9], 
    [8, 38, 35], 
    [38, 8, 9], 
    [38, 34, 35], 
    [35, 32, 40], 
    [35, 40, 8], 
    [11, 40, 32], 
    [40, 11, 7], 
    [7, 8, 40], 
    [11, 32, 28], 
    [26, 29, 41], 
    [41, 42, 26], 
    [24, 23, 42], 
    [24, 42, 43], 
    [23, 26, 42], 
    [43, 44, 24], 
    [44, 45, 24], 
    [46, 24, 45], 
    [46, 45, 47], 
    [47, 48, 46], 
    [49, 46, 48], 
    [50, 49, 48], 
    [49, 50, 51], 
    [51, 53, 52], 
    [49, 51, 52], 
    [19, 53, 18], 
    [52, 53, 19], 
    [49, 52, 21], 
    [21, 52, 19], 
    [46, 49, 21], 
    [24, 46, 21], 
    [28, 16, 11], 
    [9, 3, 1]
] # PSD_wall_list

PSD = m.GeometryObject(
    name = 'PSD',
    vertex_list = PSD_vertex_list,
    wall_list = PSD_wall_list,
    surface_regions = []
)
# ^^^^ PSD ^^^^

