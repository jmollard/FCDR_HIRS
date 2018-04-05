"""Harmonisation definitions.

Definitions relating to the output of harmonisation.

In particular, the `harmonisation_parameters` dictionary contains the
relevant parameters for each satellite and channel for which harmonisation
has so far been applied in the form of:

`Dict[str, Dict[int, Dict[int, float]]]`

For example, to get a₀ for noaa18:

`harmonisation_parameters["noaa18"][12][0]`

Corresponding uncertainties are contained in
`harmonisation_parameters_uncertainty`.  Covariance is not yet supported.
Harmonisation parameters are derived using software developed by Ralf Quast.
"""

###############################################
###                                         ###
### AUTOMATICALLY GENERATED — DO NOT EDIT!! ###
###                                         ###
###############################################

harmonisation_parameters =  {'metopa': {1: {0: 2.9459138777326034e-15,
                1: -2.2739776101697823e-22,
                2: 0.005711424345785645},
            2: {0: -6.195721205598414e-16,
                1: -6.32609491306781e-21,
                2: 0.02336282290172156},
            3: {0: -1.189513369829004e-13,
                1: -2.715184898632757e-19,
                2: -0.03705793189072383},
            4: {0: -1.8864330570359248e-13,
                1: -3.572095149176044e-19,
                2: -0.06107017682572921},
            5: {0: -1.437127403268467e-14,
                1: 6.725605721551585e-21,
                2: 0.03393006160695815},
            6: {0: -4.738326165985468e-14,
                1: -2.3860990345722715e-20,
                2: 0.024036781299609237},
            7: {0: -2.6331525698261622e-14,
                1: 1.382165444780876e-21,
                2: 0.03487641042888461},
            8: {0: -3.675207233899877e-15,
                1: 2.6452558576820022e-21,
                2: 0.019407284903765754},
            9: {0: -2.8955689193614424e-15,
                1: -1.2086313782705723e-20,
                2: 0.016082872619687036},
            10: {0: -9.06898926360435e-15,
                 1: 2.225208754130968e-21,
                 2: 0.021542477438892507},
            11: {0: -8.396195462259682e-15,
                 1: -2.940158144492321e-20,
                 2: 0.02089964660672204},
            12: {0: -7.844590349560227e-15,
                 1: -2.633410495149053e-19,
                 2: -0.1812184351932442},
            13: {0: 4.6583576313809825e-17,
                 1: -5.620009446926258e-22,
                 2: -0.01476856151737801},
            14: {0: -7.477376175254476e-17,
                 1: -5.828731978733168e-22,
                 2: 0.007230402930668027},
            15: {0: 1.7441979200042097e-17,
                 1: -6.047386764997141e-21,
                 2: -0.1800858717283149},
            16: {0: 2.5224168357702795e-17,
                 1: 1.6088029241560773e-22,
                 2: -1.4746393566183548e-05},
            17: {0: -6.010506246413946e-18,
                 1: 3.057701821021635e-22,
                 2: 0.023384395595586378},
            18: {0: -2.415075666688314e-17,
                 1: 1.2492514884824884e-22,
                 2: 0.017868871229273338},
            19: {0: -2.3093755859618257e-17,
                 1: 6.60968650847717e-23,
                 2: 0.0161271219863739}},
 'metopb': {1: {0: -1.0326438075901344e-18,
                1: 3.581645254311237e-26,
                2: -1.9585793200225172e-06},
            2: {0: 4.662075626425774e-18,
                1: -1.442692801234667e-24,
                2: 3.347597682714817e-05},
            3: {0: 1.0502095817645573e-14,
                1: -2.7222177096234842e-21,
                2: 0.01655331505091362},
            4: {0: 1.0321350290747667e-14,
                1: -6.891170615730952e-21,
                2: 0.015299087552116616},
            5: {0: 1.1035424629313562e-16,
                1: -8.734682881740742e-23,
                2: 0.00020816057552206006},
            6: {0: 8.580420602148403e-15,
                1: -5.571688611061433e-21,
                2: 0.01710397666236089},
            7: {0: 5.814740515367723e-15,
                1: -6.919811617473798e-21,
                2: 0.013868472500666832},
            8: {0: 6.124649518494441e-16,
                1: -4.750495029643108e-22,
                2: 0.001131518629656097},
            9: {0: 1.0874503334333802e-14,
                1: -1.728646281700086e-21,
                2: 0.009453085073810864},
            10: {0: 5.3251029866543375e-15,
                 1: -4.111330105570341e-21,
                 2: 0.012029757893997904},
            11: {0: 6.733464423221369e-15,
                 1: -6.544670043253038e-22,
                 2: 0.0005023287636405707},
            12: {0: -1.2388160932295723e-15,
                 1: -3.9381137713181333e-23,
                 2: 0.00011072310993646597},
            13: {0: 2.855831935479564e-16,
                 1: 7.948315097473503e-21,
                 2: -0.001764309795164534},
            14: {0: -1.3455183048775652e-16,
                 1: 8.873766688139932e-22,
                 2: -9.26902973147112e-05},
            15: {0: 1.1752505831869147e-16,
                 1: 2.622512696703731e-21,
                 2: -0.00016343373942860132},
            16: {0: 1.891629177256318e-18,
                 1: -1.2919435350438698e-24,
                 2: 8.88764122223308e-08},
            17: {0: 1.0721080151999916e-16,
                 1: -2.7746840705140243e-22,
                 2: -8.762404727639799e-05},
            18: {0: 1.0790166741739146e-17,
                 1: -1.5955120364611098e-22,
                 2: -3.2324468212228995e-05},
            19: {0: -1.0275220341743264e-18,
                 1: -2.405819753051396e-23,
                 2: -2.2586526667535833e-05}},
 'noaa16': {1: {0: 2.1981035116281284e-17,
                1: -1.98401289305685e-24,
                2: 3.272677992403012e-05},
            2: {0: 9.4556215473339e-15,
                1: -1.600399312797981e-21,
                2: 0.014278614823386238},
            3: {0: -4.2154261971640465e-15,
                1: -2.130044906727428e-21,
                2: 0.02620809987677492},
            4: {0: 1.1136556386967663e-14,
                1: -5.7487287871042436e-21,
                2: 0.014046790275231398},
            5: {0: 4.9003079337695566e-15,
                1: -4.9602712522488035e-21,
                2: 0.008334317814677637},
            6: {0: 6.137444825478719e-15,
                1: -5.947407570740178e-21,
                2: 0.01160680979993146},
            7: {0: 4.376654480514933e-15,
                1: -4.705117263002122e-21,
                2: 0.013196167555431512},
            8: {0: 1.4524807409238381e-15,
                1: -1.807014585529545e-21,
                2: 0.0030047587707673303},
            9: {0: 1.27797068035622e-14,
                1: -6.652067203178955e-21,
                2: 0.01483888990656299},
            10: {0: 6.0153811191365745e-15,
                 1: -7.144677329972351e-21,
                 2: 0.012325982963144697},
            11: {0: 5.132506916436998e-16,
                 1: -8.979531993969339e-21,
                 2: 0.0255979248290206},
            12: {0: 9.685182346807509e-16,
                 1: 1.0455309153412308e-21,
                 2: -0.0028609740204330898},
            13: {0: 3.2025113526260156e-16,
                 1: 3.1625275495122114e-21,
                 2: 0.00036784682559598265},
            14: {0: 1.373924128761997e-16,
                 1: 1.459991922215918e-21,
                 2: -0.00016006605226943338},
            15: {0: 2.483139709388412e-16,
                 1: 1.6770150635599395e-21,
                 2: -0.0005283799258381536},
            16: {0: -1.826759791093597e-17,
                 1: 1.2413356617479875e-23,
                 2: -3.4068099848560724e-07},
            17: {0: 9.998985732448382e-17,
                 1: 8.463130925371371e-22,
                 2: 0.001160182050137345},
            18: {0: 7.216049632747504e-17,
                 1: 3.864938926656317e-22,
                 2: 3.4012810219886976e-05},
            19: {0: 3.065326234054672e-17,
                 1: 4.613269967929728e-22,
                 2: 0.0001449001064623788}},
 'noaa17': {1: {0: 2.822835748176776e-17,
                1: -7.209732123868976e-26,
                2: 4.214372697225709e-05},
            2: {0: 1.479951446492339e-14,
                1: -2.554706536352075e-22,
                2: 0.015998591925008694},
            3: {0: -2.1616400522126237e-14,
                1: -1.8336255880274066e-21,
                2: 0.03999454789177733},
            4: {0: -7.918108113192742e-15,
                1: -4.896383750313522e-21,
                2: 0.0299640392502991},
            5: {0: 7.712851406658583e-15,
                1: -3.047456577299435e-21,
                2: 0.01356229801429573},
            6: {0: -4.104000519871999e-15,
                1: 1.4113293994067366e-21,
                2: 0.01962715018930668},
            7: {0: -1.0336136903214851e-14,
                1: 1.7560374589293178e-20,
                2: 0.03541691062090254},
            8: {0: 6.538117991132209e-15,
                1: -4.491853243606799e-21,
                2: 0.01233038332494187},
            9: {0: 5.205982894813794e-15,
                1: -2.017160564286301e-21,
                2: 0.015988782207430465},
            10: {0: 3.0221351602780675e-15,
                 1: 2.3040704309692383e-21,
                 2: 0.016800679388920454},
            11: {0: -4.9718049736159916e-15,
                 1: -1.5993288471554415e-20,
                 2: 0.04531682778208925},
            12: {0: 2.244901201871615e-15,
                 1: 1.916931642552264e-21,
                 2: -0.007664174672129015},
            13: {0: 2.704535493598785e-16,
                 1: 6.585053665531251e-21,
                 2: -0.0017574100060458822},
            14: {0: 2.6617473106673236e-17,
                 1: 2.816647274118229e-22,
                 2: -5.5963592348710277e-05},
            15: {0: 2.2226156141124736e-16,
                 1: 3.1680915459597374e-21,
                 2: -0.003748542475120758},
            16: {0: -8.721917357721034e-17,
                 1: 1.1732060210952814e-23,
                 2: -5.525705908469544e-07},
            17: {0: 2.6529950843160068e-17,
                 1: -2.358751542824845e-21,
                 2: 0.002127927644189919},
            18: {0: 7.068041402228235e-17,
                 1: 1.976518643568063e-22,
                 2: 9.548812371162203e-05},
            19: {0: -3.2685950288122907e-17,
                 1: 3.5726177685099345e-22,
                 2: -0.0002458987993453486}},
 'noaa18': {1: {0: -3.903404632924674e-18,
                1: 4.681435885558904e-25,
                2: -7.158738219236094e-06},
            2: {0: 7.607186163634055e-15,
                1: -6.165219165785353e-22,
                2: 0.012029429055794941},
            3: {0: -1.7803382822049628e-14,
                1: -2.8588467659273914e-21,
                2: 0.028544798385060452},
            4: {0: 6.289830240774194e-15,
                1: -5.926147685869203e-21,
                2: 0.01955320956466878},
            5: {0: 1.3200055423380618e-15,
                1: -1.0121946555723475e-21,
                2: 0.0020916239544851896},
            6: {0: 5.939745317045895e-15,
                1: -4.3557984605228576e-21,
                2: 0.010302517127315563},
            7: {0: 7.034199958869325e-15,
                1: -7.110110876761916e-21,
                2: 0.014187319557166879},
            8: {0: 1.1184999311145486e-15,
                1: -8.061403609807594e-22,
                2: 0.0015193018340127881},
            9: {0: 7.832210595605091e-15,
                1: -1.2139068421909917e-21,
                2: 0.006921973168562212},
            10: {0: 4.26107417855422e-15,
                 1: -3.5992159894846386e-21,
                 2: 0.0076855781858063054},
            11: {0: 6.467895963248214e-15,
                 1: -3.3030225860034415e-21,
                 2: 0.01086517895555592},
            12: {0: 2.202037365265115e-15,
                 1: -9.419043269709739e-23,
                 2: 0.00020169582781055583},
            13: {0: 4.46572586566355e-16,
                 1: 2.649410547490992e-21,
                 2: -0.00015400600528094307},
            14: {0: -6.986055410507437e-18,
                 1: 8.143639051906336e-22,
                 2: -3.666226666637885e-05},
            15: {0: 3.052344535130292e-16,
                 1: 1.781341135553704e-21,
                 2: -5.142128967065682e-05},
            16: {0: 7.100605957992629e-17,
                 1: -4.170804149441224e-25,
                 2: 1.1464325794880974e-08},
            17: {0: 2.984826402725178e-17,
                 1: -1.432006421257944e-21,
                 2: 0.00015196251993818122},
            18: {0: 3.6399921710270946e-17,
                 1: 9.386296208605088e-23,
                 2: -1.3402679789059531e-05},
            19: {0: 6.481254643278746e-18,
                 1: -5.521898217024104e-23,
                 2: 4.143125812855333e-06}},
 'noaa19': {1: {0: -1.9502316362445616e-18,
                1: 1.0965972020782942e-25,
                2: -3.3316503653198854e-06},
            2: {0: 1.6493651237149987e-15,
                1: -1.7197024532125369e-22,
                2: 0.0026443563947484666},
            3: {0: 3.689343298553664e-16,
                1: -3.763950131653173e-21,
                2: 0.01310301540108312},
            4: {0: 6.635992844959846e-15,
                1: -7.014993179252888e-21,
                2: 0.016063750385092047},
            5: {0: 1.1164899399278539e-15,
                1: -8.019550326485014e-22,
                2: 0.0018914724079368383},
            6: {0: 8.583888976632662e-15,
                1: -9.389400599178043e-21,
                2: 0.0157402498660863},
            7: {0: 6.843977813190224e-15,
                1: -8.260564956961734e-21,
                2: 0.013425528256907434},
            8: {0: 1.7052968763433566e-16,
                1: -1.8154719613007173e-22,
                2: 0.0002456532636415776},
            9: {0: 7.143167855162613e-15,
                1: -1.5214824737650761e-21,
                2: 0.005555044950893242},
            10: {0: 2.212307012723523e-15,
                 1: -2.684227221464015e-21,
                 2: 0.0039833417076406965},
            11: {0: 3.654960873348135e-15,
                 1: -4.47437788935762e-21,
                 2: 0.006305140706534277},
            12: {0: 2.9748420781270013e-15,
                 1: -4.370962086584327e-22,
                 2: 0.0006987442409026323},
            13: {0: 3.838459480417321e-16,
                 1: 5.577120653977014e-21,
                 2: -0.00032872839300781013},
            14: {0: -3.233614534369687e-18,
                 1: -2.239942826974507e-22,
                 2: 9.789783239687e-06},
            15: {0: 3.9961277129899807e-16,
                 1: 4.582851988196585e-21,
                 2: -0.00020612036214553512},
            16: {0: 6.7134169791399456e-18,
                 1: -4.283419128176311e-25,
                 2: 3.4624503346966524e-08},
            17: {0: 6.009239498448829e-17,
                 1: -9.68295445965095e-22,
                 2: 9.62496538922928e-05},
            18: {0: 4.7151389891368395e-17,
                 1: -2.4575606099457227e-24,
                 2: 1.976131709917894e-07},
            19: {0: -1.5000482169255413e-17,
                 1: 5.755896026503849e-23,
                 2: -3.2452367703937603e-06}}}
harmonisation_parameter_uncertainties =  {'metopa': {1: {0: 9.809815765447625e-16,
                1: 1.402579427608114e-20,
                2: 0.00011109316320511251},
            2: {0: 1.85374888743893e-16,
                1: 1.2012723195114284e-21,
                2: 6.312696296930315e-05},
            3: {0: 1.2736338491100224e-16,
                1: 2.628475831815069e-22,
                2: 5.371829190787073e-05},
            4: {0: 1.2948510325667087e-16,
                1: 2.101611283078794e-22,
                2: 5.471740161885782e-05},
            5: {0: 1.2137173242567747e-16,
                1: 9.143169908096689e-23,
                2: 1.813755642077654e-05},
            6: {0: 1.0000522061355523e-16,
                1: 5.474753339634463e-23,
                2: 1.3662885748403636e-05},
            7: {0: 7.908995274395027e-17,
                1: 2.677215336301411e-23,
                2: 1.561446568960896e-05},
            8: {0: 2.595584718151052e-17,
                1: 7.377488673083666e-24,
                2: 8.843027738285749e-06},
            9: {0: 2.7243150274708623e-17,
                1: 7.537550103919002e-23,
                2: 7.90006905795128e-06},
            10: {0: 5.0251107394744934e-17,
                 1: 1.191083019772206e-23,
                 2: 1.3768699890510952e-05},
            11: {0: 1.5981468675791103e-17,
                 1: 5.784053730374402e-23,
                 2: 1.7294793176385677e-05},
            12: {0: 8.27901715657992e-18,
                 1: 2.181293458915969e-22,
                 2: 0.00017426373731676276},
            13: {0: 3.765195835831319e-19,
                 1: 1.3853671475041769e-24,
                 2: 7.215443138279341e-06},
            14: {0: 3.1546075577927465e-19,
                 1: 2.408417493651358e-24,
                 2: 2.7034184039205176e-05},
            15: {0: 2.955479759195686e-19,
                 1: 6.000545960173239e-24,
                 2: 0.00013244443679063522},
            16: {0: 2.0598691686055674e-19,
                 1: 5.6727518654229664e-24,
                 2: 0.00015069587651619297},
            17: {0: 1.7258811710623203e-19,
                 1: 7.899126742265839e-25,
                 2: 8.94993127375636e-06},
            18: {0: 1.505201211192349e-19,
                 1: 4.468078101835632e-25,
                 2: 1.0783709556744717e-05},
            19: {0: 9.15735444475136e-20,
                 1: 2.288748840788553e-25,
                 2: 1.0355670669203814e-05}},
 'metopb': {1: {0: 3.9005124814553275e-14,
                1: 1.3267979174630604e-18,
                2: 0.007016244769347007},
            2: {0: 4.829811116312893e-15,
                1: 5.0034656113453936e-20,
                2: 0.0030226444052002606},
            3: {0: 4.777803382294029e-15,
                1: 3.596100512135035e-20,
                2: 0.0033715260566708895},
            4: {0: 4.7978647479504464e-15,
                1: 1.3433841739700457e-20,
                2: 0.0033454662004725726},
            5: {0: 4.559251561335189e-15,
                1: 8.635490893991588e-21,
                2: 0.0015347247521221496},
            6: {0: 2.8012902808534613e-15,
                1: 3.994731816247228e-21,
                2: 0.0004281290640630327},
            7: {0: 2.223502654104285e-15,
                1: 1.6953865127597713e-21,
                2: 0.00042110359480490534},
            8: {0: 6.817547529133401e-16,
                1: 3.822868828953413e-22,
                2: 0.0002517384868944412},
            9: {0: 4.9183444958474385e-16,
                1: 3.3587525014113748e-21,
                2: 0.0002859602874915579},
            10: {0: 1.3193317232160652e-15,
                 1: 7.457251718250943e-22,
                 2: 0.00037539869132092313},
            11: {0: 4.095062882637853e-16,
                 1: 3.3968972643222974e-21,
                 2: 0.0008174075784077638},
            12: {0: 6.997641680630925e-16,
                 1: 4.589748820042524e-20,
                 2: 0.019100825401748508},
            13: {0: 4.427307590121368e-18,
                 1: 7.475965057641489e-23,
                 2: 0.0005452657639558649},
            14: {0: 4.139699240968863e-18,
                 1: 2.0989614664507665e-22,
                 2: 0.001726996959461824},
            15: {0: 3.5615655762954415e-18,
                 1: 3.0237778789728634e-22,
                 2: 0.0037027659713193767},
            16: {0: 2.8141748294925096e-18,
                 1: 2.4951754347816232e-22,
                 2: 0.0038000711599488657},
            17: {0: 2.506015280070554e-18,
                 1: 4.245061722784524e-23,
                 2: 0.000296449164158816},
            18: {0: 1.750498312039337e-18,
                 1: 3.088945843730333e-23,
                 2: 0.00031249996759436806},
            19: {0: 1.0523852055041567e-18,
                 1: 4.611682154473314e-23,
                 2: 0.0003559824434040993}},
 'noaa16': {1: {0: 7.887338738033841e-15,
                1: 9.973216477143139e-20,
                2: 0.002109908312000015},
            2: {0: 1.1354220324948965e-15,
                1: 1.2194779155454029e-20,
                2: 0.0007483551875314093},
            3: {0: 1.0929128151948022e-15,
                1: 7.45064694802213e-21,
                2: 0.000817878377423428},
            4: {0: 1.0112238948482279e-15,
                1: 3.2762255567420434e-21,
                2: 0.0006651740683694975},
            5: {0: 1.1995756190466258e-15,
                1: 1.6002238309298422e-21,
                2: 0.0003960901695369875},
            6: {0: 1.0615199670869723e-15,
                1: 1.1690042504810403e-21,
                2: 0.00021357041728806722},
            7: {0: 7.622949766920222e-16,
                1: 2.926770789734716e-22,
                2: 0.00015360861681818782},
            8: {0: 2.797002796190571e-16,
                1: 7.857007592305999e-23,
                2: 0.00010330090278553486},
            9: {0: 2.007826906667848e-16,
                1: 5.24761568586634e-22,
                2: 0.00018209802405052929},
            10: {0: 5.396310381897632e-16,
                 1: 2.523663319294303e-22,
                 2: 0.00014790953052547394},
            11: {0: 1.4578058333488474e-16,
                 1: 1.1446917012311816e-21,
                 2: 0.0004983610235617314},
            12: {0: 1.8230912821035624e-16,
                 1: 1.6534449314214193e-20,
                 2: 0.005538642084815475},
            13: {0: 1.8552182265808443e-18,
                 1: 2.8854770162605506e-23,
                 2: 0.0005370226768316628},
            14: {0: 1.8688590846253018e-18,
                 1: 3.7306589811928986e-23,
                 2: 0.0014078217537176298},
            15: {0: 1.6887073234400008e-18,
                 1: 4.913520057316077e-23,
                 2: 0.002072967496735395},
            16: {0: 1.689889701913189e-18,
                 1: 5.760079125995181e-23,
                 2: 0.002654502278094399},
            17: {0: 1.060976860741459e-18,
                 1: 7.701112578330644e-23,
                 2: 0.0001751163933268786},
            18: {0: 7.336584581895096e-19,
                 1: 2.8400054004979364e-23,
                 2: 0.00015276663594055776},
            19: {0: 4.208713959701027e-19,
                 1: 1.032138969996134e-23,
                 2: 0.00017022536149854153}},
 'noaa17': {1: {0: 7.684074015122254e-15,
                1: 3.764966477968967e-18,
                2: 0.0018895938510633346},
            2: {0: 6.016219952812267e-16,
                1: 6.058003119549481e-20,
                2: 0.0004458310603552681},
            3: {0: 5.709604423059101e-16,
                1: 2.3549075658833822e-20,
                2: 0.0004864058455685627},
            4: {0: 6.611882547099422e-16,
                1: 4.937438114526579e-21,
                2: 0.00036057003153525444},
            5: {0: 6.274218899824388e-16,
                1: 2.3641355329003332e-21,
                2: 0.00021206535670100464},
            6: {0: 5.062574902397102e-16,
                1: 1.32263942947896e-21,
                2: 8.003222712369166e-05},
            7: {0: 4.3454581235444835e-16,
                1: 3.295520718722706e-22,
                2: 8.242885878261725e-05},
            8: {0: 2.0737798061072327e-16,
                1: 1.608123909820402e-22,
                2: 7.657625738303217e-05},
            9: {0: 1.1861087694126792e-16,
                1: 1.0854168963138995e-21,
                2: 0.0001562797622558252},
            10: {0: 3.1348934356290365e-16,
                 1: 1.8421921475138616e-22,
                 2: 8.639397880703674e-05},
            11: {0: 5.381518516413548e-17,
                 1: 5.921608779686174e-22,
                 2: 0.0002610434189963746},
            12: {0: 5.142588720444228e-17,
                 1: 6.946965146764744e-21,
                 2: 0.0018878329843954836},
            13: {0: 1.400943306563545e-18,
                 1: 5.513705454857404e-23,
                 2: 0.0005028971676526634},
            14: {0: 1.1706502730792429e-18,
                 1: 2.984469578801014e-23,
                 2: 0.0005045363076907305},
            15: {0: 1.4020890245995469e-18,
                 1: 8.621050557440985e-23,
                 2: 0.0017476539874638447},
            16: {0: 1.4712948357687177e-18,
                 1: 1.1893099003310688e-22,
                 2: 0.002655307333828915},
            17: {0: 9.418519761011791e-19,
                 1: 5.710607642282545e-23,
                 2: 0.00017213730074223352},
            18: {0: 6.259416896664401e-19,
                 1: 2.2003439048958052e-23,
                 2: 0.00014731507548686556},
            19: {0: 3.7270090733607074e-19,
                 1: 8.614534760144136e-24,
                 2: 0.0001743831511248506}},
 'noaa18': {1: {0: 1.072532654871602e-14,
                1: 9.771287566899883e-20,
                2: 0.0015218422354598663},
            2: {0: 1.4408947222566703e-15,
                1: 3.45487326482016e-20,
                2: 0.000975530609733566},
            3: {0: 8.859737578117099e-16,
                1: 3.544190184606925e-21,
                2: 0.0006845187304606757},
            4: {0: 1.4710501241845845e-15,
                1: 4.770406796568958e-21,
                2: 0.0009937798085144138},
            5: {0: 2.5038931778041966e-15,
                1: 5.777619981746453e-21,
                2: 0.0013736181441387574},
            6: {0: 1.757842462090335e-15,
                1: 3.2764032575358673e-21,
                2: 0.0005227800844882361},
            7: {0: 1.5535014966207414e-15,
                1: 1.957133585056275e-21,
                2: 0.00038650697585628234},
            8: {0: 6.680020099855045e-16,
                1: 1.086528312622766e-21,
                2: 0.0002821994086293035},
            9: {0: 3.987662585904829e-16,
                1: 6.52214786062796e-21,
                2: 0.0007879887803960354},
            10: {0: 1.1314392397577144e-15,
                 1: 1.4165742672400478e-21,
                 2: 0.0002999092064790327},
            11: {0: 2.2130170076537815e-16,
                 1: 6.490431841394769e-21,
                 2: 0.001824742686802475},
            12: {0: 2.130429970797048e-16,
                 1: 3.100101845764849e-20,
                 2: 0.008832323190336654},
            13: {0: 2.8271986076195815e-18,
                 1: 7.069845186817596e-23,
                 2: 0.0014227765349056206},
            14: {0: 2.5186696984887434e-18,
                 1: 7.720224938630361e-23,
                 2: 0.0018968420937200208},
            15: {0: 2.0935364954330238e-18,
                 1: 8.027552304886763e-23,
                 2: 0.0025186993264696305},
            16: {0: 1.8291607891193844e-18,
                 1: 7.937980198046449e-23,
                 2: 0.0026178408335791018},
            17: {0: 1.6049767182429488e-18,
                 1: 1.36989261435616e-22,
                 2: 0.00128652137603671},
            18: {0: 1.3538269423310276e-18,
                 1: 1.5807684387187733e-22,
                 2: 0.0011764018226179838},
            19: {0: 7.2879979983392385e-19,
                 1: 6.677256496542292e-23,
                 2: 0.0008887121526823892}},
 'noaa19': {1: {0: 2.5691757029661036e-14,
                1: 5.257556524272016e-19,
                2: 0.005053950350558746},
            2: {0: 2.5948907236836827e-15,
                1: 5.0155437750655886e-20,
                2: 0.0018368918931730212},
            3: {0: 2.3234085616326666e-15,
                1: 8.317052617640426e-21,
                2: 0.002422039720998642},
            4: {0: 2.0730556043754354e-15,
                1: 4.993788809908261e-21,
                2: 0.0014523843022741958},
            5: {0: 3.086067919787343e-15,
                1: 7.219217987087396e-21,
                2: 0.0013977755711762501},
            6: {0: 2.9697822078295316e-15,
                1: 3.870008138753692e-21,
                2: 0.0009089342168829202},
            7: {0: 2.406931614840094e-15,
                1: 2.578068335952541e-21,
                2: 0.0006305987834364491},
            8: {0: 1.0261787092222461e-15,
                1: 1.249466006881184e-21,
                2: 0.00047123079839719314},
            9: {0: 6.370599644737857e-16,
                1: 7.557778763591272e-21,
                2: 0.0014026181877499495},
            10: {0: 1.741412203662213e-15,
                 1: 1.59742388089523e-21,
                 2: 0.00048475876082295326},
            11: {0: 3.3754285935748535e-16,
                 1: 4.998006049469389e-21,
                 2: 0.0033545564428691618},
            12: {0: 2.61128656826116e-16,
                 1: 2.876881803244123e-20,
                 2: 0.01635653282876478},
            13: {0: 5.1340557673518614e-18,
                 1: 1.859301521493986e-22,
                 2: 0.003206921528509003},
            14: {0: 4.192699774293116e-18,
                 1: 2.005489594334134e-22,
                 2: 0.00526168350486845},
            15: {0: 3.394469994872355e-18,
                 1: 1.5524797066152856e-22,
                 2: 0.0043339098906899996},
            16: {0: 4.22996852031195e-18,
                 1: 7.121080496037587e-22,
                 2: 0.008932949138083346},
            17: {0: 3.2459371611645e-18,
                 1: 2.6080648711861023e-22,
                 2: 0.002720509893080256},
            18: {0: 2.1888681057502777e-18,
                 1: 2.52738544985609e-22,
                 2: 0.0021490981033014445},
            19: {0: 1.1719874198200525e-18,
                 1: 8.380129116223354e-23,
                 2: 0.0016356937174842687}}}
