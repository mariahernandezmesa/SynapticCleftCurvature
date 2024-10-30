import mcell as m

# ---- presynaptic ----
presynaptic_vertex_list = [
    [-0.826584458351135, -2.44588136672974, 0.305769115686417], 
    [-0.844454944133759, -2.45260810852051, 0.324942082166672], 
    [-0.836105644702911, -2.47906565666199, 0.310764670372009], 
    [-0.818159878253937, -2.46659159660339, 0.295852512121201], 
    [-0.816353440284729, -2.4952712059021, 0.286470711231232], 
    [-0.825347483158112, -2.53699660301208, 0.285393714904785], 
    [-0.83389276266098, -2.50775814056396, 0.303138077259064], 
    [-0.842143297195435, -2.5032594203949, 0.328543305397034], 
    [-0.83937019109726, -2.52831649780273, 0.316138863563538], 
    [-0.836118698120117, -2.55642342567444, 0.325076639652252], 
    [-0.840871572494507, -2.52849292755127, 0.341495245695114], 
    [-0.835677027702332, -2.5243456363678, 0.366478145122528], 
    [-0.844153881072998, -2.49959087371826, 0.357284635305405], 
    [-0.83203911781311, -2.55066084861755, 0.359627544879913], 
    [-0.810921788215637, -2.56085515022278, 0.38334321975708], 
    [-0.821202099323273, -2.57062411308289, 0.342310696840286], 
    [-0.824084401130676, -2.53547501564026, 0.386378288269043], 
    [-0.812243223190308, -2.57288217544556, 0.361652731895447], 
    [-0.794692993164062, -2.58209800720215, 0.375768452882767], 
    [-0.808304369449615, -2.59886384010315, 0.35025829076767], 
    [-0.79255872964859, -2.61608743667603, 0.333995848894119], 
    [-0.783859431743622, -2.602618932724, 0.365014791488647], 
    [-0.806191504001617, -2.60332798957825, 0.324982494115829], 
    [-0.819827556610107, -2.58439111709595, 0.323942482471466], 
    [-0.779408156871796, -2.62188172340393, 0.351455360651016], 
    [-0.757052421569824, -2.61521887779236, 0.363443821668625], 
    [-0.776171624660492, -2.63102722167969, 0.331556707620621], 
    [-0.753276944160461, -2.64452362060547, 0.340760201215744], 
    [-0.742031574249268, -2.63518524169922, 0.36534982919693], 
    [-0.764155924320221, -2.64502239227295, 0.315867781639099], 
    [-0.76940381526947, -2.63270783424377, 0.292984485626221], 
    [-0.789673328399658, -2.62133002281189, 0.310888141393661], 
    [-0.80952000617981, -2.60002183914185, 0.303538084030151], 
    [-0.789346575737, -2.61038756370544, 0.285084366798401], 
    [-0.805037498474121, -2.5885603427887, 0.279670834541321], 
    [-0.825646281242371, -2.57435774803162, 0.303198426961899], 
    [-0.81523472070694, -2.56684374809265, 0.282195955514908], 
    [-0.740809917449951, -2.61493062973022, 0.385262370109558], 
    [-0.758729696273804, -2.59226703643799, 0.403781622648239], 
    [-0.768831253051758, -2.59487342834473, 0.381732612848282], 
    [-0.787389516830444, -2.57370948791504, 0.401025384664536], 
    [-0.808407008647919, -2.54793787002563, 0.405914723873138], 
    [-0.833464980125427, -2.50753140449524, 0.386922925710678], 
    [-0.843844532966614, -2.48242115974426, 0.384230345487595], 
    [-0.848213076591492, -2.47210335731506, 0.361322641372681], 
    [-0.852945148944855, -2.45135045051575, 0.349114924669266], 
    [-0.845894575119019, -2.47738790512085, 0.337131559848785]
] # presynaptic_vertex_list

presynaptic_wall_list = [
    [1, 2, 0], 
    [2, 3, 0], 
    [3, 2, 4], 
    [5, 4, 6], 
    [6, 4, 2], 
    [5, 6, 8], 
    [7, 6, 2], 
    [6, 7, 8], 
    [8, 9, 5], 
    [9, 8, 10], 
    [10, 8, 7], 
    [10, 11, 13], 
    [12, 11, 10], 
    [10, 7, 12], 
    [13, 9, 10], 
    [13, 16, 14], 
    [14, 17, 13], 
    [13, 17, 15], 
    [15, 9, 13], 
    [13, 11, 16], 
    [14, 18, 17], 
    [17, 19, 15], 
    [18, 19, 17], 
    [19, 23, 15], 
    [20, 22, 19], 
    [19, 24, 20], 
    [18, 21, 19], 
    [21, 24, 19], 
    [19, 22, 23], 
    [24, 26, 20], 
    [24, 21, 25], 
    [25, 27, 24], 
    [24, 27, 26], 
    [27, 25, 28], 
    [26, 27, 29], 
    [26, 29, 31], 
    [31, 29, 30], 
    [20, 26, 31], 
    [31, 22, 20], 
    [31, 32, 22], 
    [31, 30, 33], 
    [31, 33, 32], 
    [32, 33, 34], 
    [34, 35, 32], 
    [35, 34, 36], 
    [35, 36, 5], 
    [9, 35, 5], 
    [35, 9, 23], 
    [23, 32, 35], 
    [23, 22, 32], 
    [37, 28, 25], 
    [37, 39, 38], 
    [25, 39, 37], 
    [40, 38, 39], 
    [39, 18, 40], 
    [39, 25, 21], 
    [21, 18, 39], 
    [40, 18, 14], 
    [40, 14, 41], 
    [41, 14, 16], 
    [15, 23, 9], 
    [42, 16, 11], 
    [12, 43, 42], 
    [42, 11, 12], 
    [12, 44, 43], 
    [44, 46, 45], 
    [12, 46, 44], 
    [2, 1, 46], 
    [46, 7, 2], 
    [12, 7, 46], 
    [46, 1, 45]
] # presynaptic_wall_list

presynaptic = m.GeometryObject(
    name = 'presynaptic',
    vertex_list = presynaptic_vertex_list,
    wall_list = presynaptic_wall_list,
    surface_regions = []
)
# ^^^^ presynaptic ^^^^


