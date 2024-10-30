import mcell as m

# ---- PSD ----
PSD_vertex_list = [
    [2.16521692276001, -2.5510413646698, -0.847018778324127], 
    [2.15599775314331, -2.51445388793945, -0.837061882019043], 
    [2.17130327224731, -2.57718372344971, -0.862766623497009], 
    [2.18354749679565, -2.55270409584045, -0.874056875705719], 
    [2.17467212677002, -2.52539038658142, -0.863603353500366], 
    [2.16873788833618, -2.49516987800598, -0.866377472877502], 
    [2.18083810806274, -2.50809001922607, -0.884416699409485], 
    [2.18901300430298, -2.52936983108521, -0.890067458152771], 
    [2.19706559181213, -2.53116631507874, -0.918635487556458], 
    [2.1937620639801, -2.55079078674316, -0.899809658527374], 
    [2.19084978103638, -2.50723338127136, -0.908260226249695], 
    [2.1830723285675, -2.4846408367157, -0.893875122070312], 
    [2.19344091415405, -2.48436284065247, -0.922371208667755], 
    [2.19870758056641, -2.50921988487244, -0.937211751937866], 
    [2.20625352859497, -2.53528833389282, -0.945619583129883], 
    [2.20480036735535, -2.48465490341187, -0.949863076210022], 
    [2.21618938446045, -2.51238608360291, -0.967632830142975], 
    [2.23607397079468, -2.53047370910645, -0.988647699356079], 
    [2.21677160263062, -2.48011636734009, -0.974718689918518], 
    [2.23587322235107, -2.49601435661316, -0.992342591285706], 
    [2.22194814682007, -2.54716229438782, -0.968396484851837], 
    [2.22173953056335, -2.58124136924744, -0.963457107543945], 
    [2.21162533760071, -2.56095385551453, -0.946568608283997], 
    [2.23722195625305, -2.56434226036072, -0.991011917591095], 
    [2.25632429122925, -2.54516935348511, -1.01070511341095], 
    [2.23743295669556, -2.59628558158875, -0.991929948329926], 
    [2.22968578338623, -2.60741472244263, -0.966932415962219], 
    [2.23278474807739, -2.62814974784851, -0.951567828655243], 
    [2.21985769271851, -2.60736918449402, -0.936690211296082], 
    [2.20718431472778, -2.58341860771179, -0.927544236183167], 
    [2.22100973129272, -2.63350105285645, -0.914450407028198], 
    [2.20331978797913, -2.60699987411499, -0.906317472457886], 
    [2.18138742446899, -2.60327792167664, -0.873226404190063], 
    [2.19212961196899, -2.57880830764771, -0.894928514957428], 
    [2.19757080078125, -2.62947487831116, -0.882687270641327], 
    [2.20979809761047, -2.65847778320312, -0.887203454971313], 
    [2.22804641723633, -2.66420841217041, -0.913901329040527], 
    [2.23681926727295, -2.65245008468628, -0.939416706562042], 
    [2.19873785972595, -2.55740118026733, -0.924229323863983], 
    [2.279376745224, -2.53606653213501, -1.03687369823456], 
    [2.26893544197083, -2.51746773719788, -1.02183413505554], 
    [2.25166153907776, -2.5158212184906, -1.00474214553833], 
    [2.26148843765259, -2.48928928375244, -1.02073323726654], 
    [2.25639057159424, -2.44918155670166, -1.02481639385223], 
    [2.24550199508667, -2.47007322311401, -1.00770616531372], 
    [2.27758836746216, -2.50334477424622, -1.04096710681915], 
    [2.27068305015564, -2.47201228141785, -1.04420709609985], 
    [2.26498675346375, -2.43716907501221, -1.04657161235809], 
    [2.25725317001343, -2.41456341743469, -1.03107810020447], 
    [2.25807023048401, -2.38255333900452, -1.04077792167664], 
    [2.24710631370544, -2.39339900016785, -1.01336669921875], 
    [2.24538922309875, -2.42028164863586, -1.00641059875488], 
    [2.22706007957458, -2.42212152481079, -0.985218584537506], 
    [2.22987723350525, -2.39491105079651, -0.990505814552307], 
    [2.23845458030701, -2.44584131240845, -0.999736368656158], 
    [2.22982287406921, -2.4684317111969, -0.992093026638031], 
    [2.22224974632263, -2.44897103309631, -0.978979408740997], 
    [2.21191763877869, -2.42733764648438, -0.964098334312439], 
    [2.20817613601685, -2.4577112197876, -0.958842217922211], 
    [2.20009565353394, -2.43774223327637, -0.945448756217957], 
    [2.19677090644836, -2.46048665046692, -0.934383273124695], 
    [2.18907070159912, -2.43549799919128, -0.9227135181427], 
    [2.18345737457275, -2.46028852462769, -0.908518075942993], 
    [2.16636061668396, -2.46520709991455, -0.88061249256134], 
    [2.17184257507324, -2.4345850944519, -0.899450361728668], 
    [2.18319773674011, -2.40990495681763, -0.917010903358459], 
    [2.15370607376099, -2.43940043449402, -0.875742197036743], 
    [2.15710020065308, -2.41749429702759, -0.88544487953186], 
    [2.16757011413574, -2.40474319458008, -0.899743676185608], 
    [2.17008662223816, -2.38300728797913, -0.909360408782959], 
    [2.18786382675171, -2.38743042945862, -0.927912592887878], 
    [2.15753364562988, -2.35958361625671, -0.906360685825348], 
    [2.17902493476868, -2.36331081390381, -0.923281133174896], 
    [2.16612386703491, -2.33508229255676, -0.922724366188049], 
    [2.18706107139587, -2.34703898429871, -0.940407872200012], 
    [2.20163869857788, -2.37333464622498, -0.947876811027527], 
    [2.21621775627136, -2.36816477775574, -0.973537862300873], 
    [2.19844031333923, -2.40909314155579, -0.942980825901031], 
    [2.21332454681396, -2.39801669120789, -0.967161297798157], 
    [2.20412921905518, -2.3431031703949, -0.960103511810303], 
    [2.19835877418518, -2.3148307800293, -0.970182299613953], 
    [2.21871566772461, -2.33728551864624, -0.985700249671936], 
    [2.23811292648315, -2.34553480148315, -1.00956356525421], 
    [2.23227739334106, -2.36765360832214, -0.996209502220154], 
    [2.23101162910461, -2.32110261917114, -1.00426125526428], 
    [2.21039795875549, -2.3017098903656, -0.997740089893341], 
    [2.23934507369995, -2.29793977737427, -1.01392960548401], 
    [2.24860644340515, -2.32544565200806, -1.02235925197601], 
    [2.25391006469727, -2.35120058059692, -1.03307378292084], 
    [2.2473156452179, -2.36892986297607, -1.01760172843933], 
    [2.18295478820801, -2.32224488258362, -0.945793867111206], 
    [2.16203665733337, -2.3065550327301, -0.931056618690491], 
    [2.17552971839905, -2.29787874221802, -0.955470502376556], 
    [2.15531325340271, -2.28488111495972, -0.944453001022339], 
    [2.13927125930786, -2.28864574432373, -0.925267696380615], 
    [2.13908386230469, -2.31166076660156, -0.910360813140869], 
    [2.14376306533813, -2.33713793754578, -0.904026627540588], 
    [2.14214682579041, -2.41772627830505, -0.869911074638367], 
    [2.13419675827026, -2.43563389778137, -0.852302432060242], 
    [2.14710640907288, -2.45690679550171, -0.857426762580872], 
    [2.14977812767029, -2.4823145866394, -0.847128748893738]
] # PSD_vertex_list

PSD_wall_list = [
    [1, 4, 0], 
    [0, 3, 2], 
    [0, 4, 3], 
    [1, 5, 4], 
    [5, 6, 4], 
    [4, 7, 3], 
    [6, 7, 4], 
    [8, 9, 7], 
    [10, 8, 7], 
    [3, 7, 9], 
    [10, 7, 6], 
    [6, 11, 10], 
    [11, 12, 10], 
    [12, 13, 10], 
    [10, 13, 8], 
    [13, 16, 14], 
    [8, 13, 14], 
    [15, 13, 12], 
    [15, 16, 13], 
    [14, 16, 20], 
    [15, 18, 16], 
    [16, 19, 17], 
    [20, 16, 17], 
    [18, 19, 16], 
    [20, 23, 21], 
    [21, 22, 20], 
    [22, 14, 20], 
    [17, 23, 20], 
    [21, 23, 25], 
    [17, 24, 23], 
    [21, 25, 26], 
    [21, 26, 28], 
    [27, 28, 26], 
    [21, 28, 29], 
    [29, 28, 31], 
    [30, 28, 27], 
    [30, 31, 28], 
    [31, 34, 32], 
    [32, 33, 31], 
    [33, 29, 31], 
    [34, 31, 30], 
    [30, 35, 34], 
    [30, 36, 35], 
    [30, 37, 36], 
    [30, 27, 37], 
    [38, 29, 33], 
    [38, 33, 9], 
    [3, 9, 33], 
    [2, 3, 33], 
    [33, 32, 2], 
    [8, 14, 38], 
    [9, 8, 38], 
    [38, 22, 29], 
    [14, 22, 38], 
    [29, 22, 21], 
    [17, 41, 24], 
    [40, 39, 24], 
    [24, 41, 40], 
    [40, 41, 42], 
    [19, 42, 41], 
    [19, 41, 17], 
    [42, 43, 46], 
    [44, 43, 42], 
    [40, 42, 45], 
    [19, 44, 42], 
    [46, 45, 42], 
    [47, 46, 43], 
    [43, 48, 47], 
    [49, 48, 50], 
    [51, 50, 48], 
    [48, 43, 51], 
    [51, 43, 54], 
    [53, 50, 51], 
    [51, 52, 53], 
    [51, 54, 52], 
    [56, 54, 55], 
    [54, 44, 55], 
    [43, 44, 54], 
    [56, 52, 54], 
    [56, 55, 18], 
    [58, 56, 18], 
    [52, 56, 57], 
    [58, 57, 56], 
    [58, 60, 59], 
    [59, 57, 58], 
    [58, 18, 15], 
    [15, 60, 58], 
    [59, 60, 61], 
    [12, 60, 15], 
    [62, 61, 60], 
    [60, 12, 62], 
    [64, 61, 62], 
    [12, 11, 62], 
    [63, 62, 11], 
    [64, 62, 63], 
    [65, 61, 64], 
    [65, 64, 68], 
    [64, 63, 66], 
    [64, 66, 67], 
    [68, 64, 67], 
    [68, 69, 65], 
    [69, 72, 70], 
    [65, 69, 70], 
    [72, 69, 71], 
    [73, 72, 71], 
    [74, 72, 73], 
    [72, 75, 70], 
    [75, 72, 74], 
    [70, 75, 77], 
    [75, 79, 76], 
    [76, 78, 75], 
    [77, 75, 78], 
    [80, 81, 79], 
    [79, 81, 76], 
    [81, 83, 76], 
    [80, 85, 81], 
    [81, 84, 82], 
    [82, 83, 81], 
    [81, 85, 84], 
    [86, 84, 85], 
    [84, 86, 87], 
    [82, 87, 88], 
    [84, 87, 82], 
    [89, 88, 49], 
    [89, 82, 88], 
    [83, 82, 89], 
    [49, 50, 89], 
    [89, 50, 83], 
    [83, 53, 76], 
    [50, 53, 83], 
    [76, 53, 78], 
    [57, 78, 52], 
    [78, 53, 52], 
    [78, 57, 77], 
    [61, 77, 59], 
    [77, 57, 59], 
    [70, 77, 65], 
    [77, 61, 65], 
    [73, 90, 74], 
    [73, 91, 90], 
    [91, 92, 90], 
    [93, 92, 91], 
    [91, 94, 93], 
    [95, 94, 91], 
    [95, 91, 73], 
    [96, 95, 73], 
    [73, 71, 96], 
    [97, 67, 66], 
    [97, 66, 98], 
    [98, 66, 99], 
    [99, 66, 63], 
    [99, 63, 100], 
    [100, 5, 1], 
    [100, 63, 5], 
    [5, 63, 11], 
    [18, 55, 19], 
    [55, 44, 19], 
    [45, 39, 40], 
    [11, 6, 5]
] # PSD_wall_list

PSD = m.GeometryObject(
    name = 'PSD',
    vertex_list = PSD_vertex_list,
    wall_list = PSD_wall_list,
    surface_regions = []
)
# ^^^^ PSD ^^^^


