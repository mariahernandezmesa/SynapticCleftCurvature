import mcell as m

# ---- PSD ----
PSD_vertex_list = [
    [1.43179333209991, -6.99302434921265, -1.92177164554596], 
    [1.43566334247589, -7.02316856384277, -1.89851641654968], 
    [1.40684950351715, -6.98214435577393, -1.94436943531036], 
    [1.41275954246521, -7.01532220840454, -1.91837537288666], 
    [1.40129363536835, -7.00048828125, -1.9329047203064], 
    [1.37634205818176, -6.98298025131226, -1.94444799423218], 
    [1.37991416454315, -7.01022720336914, -1.9230147600174], 
    [1.35790956020355, -7.01060152053833, -1.90719151496887], 
    [1.37576043605804, -7.02979183197021, -1.89831173419952], 
    [1.4037983417511, -7.03224468231201, -1.90270256996155], 
    [1.34706282615662, -6.98889303207397, -1.92742621898651], 
    [1.33628594875336, -7.00322675704956, -1.8904093503952], 
    [1.32239556312561, -6.96646881103516, -1.93688786029816], 
    [1.34702205657959, -6.96205854415894, -1.94995605945587], 
    [1.32011234760284, -6.98360538482666, -1.90907859802246], 
    [1.29574203491211, -6.9781756401062, -1.89459681510925], 
    [1.3124418258667, -6.99420404434204, -1.87841928005219], 
    [1.29907500743866, -6.9677734375, -1.92154061794281], 
    [1.29838228225708, -6.94923782348633, -1.94714903831482], 
    [1.27723729610443, -6.95663022994995, -1.93063867092133], 
    [1.27756774425507, -6.96783065795898, -1.90845108032227], 
    [1.24931228160858, -6.96320343017578, -1.90949642658234], 
    [1.26732015609741, -6.97319746017456, -1.88640999794006], 
    [1.26393270492554, -6.98430871963501, -1.86460089683533], 
    [1.23436844348907, -6.97510051727295, -1.87560224533081], 
    [1.28862082958221, -6.9859881401062, -1.86880159378052], 
    [1.2772468328476, -6.99915885925293, -1.84832799434662], 
    [1.30212152004242, -7.00486278533936, -1.85139608383179], 
    [1.32598125934601, -7.01218938827515, -1.86043810844421], 
    [1.28880536556244, -7.01895332336426, -1.82914304733276], 
    [1.313725233078, -7.02822923660278, -1.83603727817535], 
    [1.33505403995514, -7.03617286682129, -1.8473858833313], 
    [1.34530663490295, -7.02889966964722, -1.86829113960266], 
    [1.35424172878265, -7.05895614624023, -1.85084497928619], 
    [1.37705230712891, -7.06371307373047, -1.86644899845123], 
    [1.36631572246552, -7.04308795928955, -1.876256108284], 
    [1.37503707408905, -7.08526992797852, -1.84985136985779], 
    [1.40221011638641, -7.07531070709229, -1.86865055561066], 
    [1.39042949676514, -7.05094623565674, -1.8856748342514], 
    [1.41886854171753, -7.05020093917847, -1.88729536533356], 
    [1.35555124282837, -7.02363681793213, -1.88856160640717], 
    [1.26426291465759, -7.00875854492188, -1.82988488674164], 
    [1.25107932090759, -6.99487733840942, -1.84624290466309], 
    [1.22694301605225, -6.98985528945923, -1.8450334072113], 
    [1.20616292953491, -6.97734785079956, -1.85404467582703], 
    [1.20340800285339, -6.96398878097534, -1.87997221946716], 
    [1.21928203105927, -6.95986461639404, -1.90452396869659], 
    [1.19132590293884, -6.94606781005859, -1.90245759487152], 
    [1.20723676681519, -6.94059753417969, -1.92469692230225], 
    [1.23267138004303, -6.94683170318604, -1.92899262905121], 
    [1.22418737411499, -6.92939281463623, -1.94871950149536], 
    [1.24700617790222, -6.93726873397827, -1.95712447166443], 
    [1.25526905059814, -6.95004320144653, -1.93629789352417], 
    [1.2734295129776, -6.94039678573608, -1.95364415645599]
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

