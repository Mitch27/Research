#!/usr/bin/python
import numpy as np
from stl import mesh
id = [18742,18805,18803,18637,18638,18640,18641,18642,18644,18645,18646,18647,18648,18649,18650,18652,18654,18655,18656,18658,18659,18660,18661,18662,18663,18664,18701,18702,18703,18704,18705,18706,18707,18708,18709,18710,18711,18712,18713,18714,18715,18716,18717,18718,18735,18739,18786,18787,18789,18793,18804,18798,18740,18741,18751,18743,18745,18757,18752,18756,18755,18759,18760,18754,18761,18772,18773,18782,18774,18758,18775,18794,18776,18790,18777,18753,18762,18763,18764,18720,18721,18723,18725,18726,18727,18728,18729,18730,18731,18732,18733,18734,18736,18737,18738,18747,18748,18973,18749,18768,18769,18778,18770,18771,18780,18781,18795,18806,18801,18802,18666,18667,18668,18669,18670,18671,18672,18673,18674,18675,18676,18677,18678,18679,18680,18681,18682,18683,18685,18686,18687,18688,18689,18690,18692,18693,18695,18696,18697,18698,18700,18750,18767,18784,18785,18792,18746,18779,18765,18766,18783,18791,18796,18797,18799,18800,18807,18808,18809,18635,18657,18665,18684,18691,18699,18719,18724,18788,18812,18813,18814,18815,18816,18817,18818,18819,18820,18821,18822,18823,18824,18825,18826,18827,18828,18829,18830,18694,18722,18633,18744,18832,18928,18932,18934,18974,18936,18937,18938,18939,18940,18943,18944,18945,18946,18948,18951,18952,18953,18954,18955,18956,18957,18958,18959,18960,18961,18962,18949,18931,18930,18941,18942,18933,18929,18935,18947,18963,18964,18965,18966,18967,18968,18969,18970,18972,18975,18976,18977,18978,18979,18980]
id_map = {18742:"085.06.0082" , 18805:"orange juice jug" , 18803:"shaving_foam_can_small" , 18637:"001.324.25" , 18638:"001.324.49" , 18640:"001.334.82" , 18641:"100.151.24" , 18642:"100.302.09" , 18644:"100.919.00-saucer" , 18645:"100.919.00-cup" , 18646:"100.922.16" , 18647:"101.236.56-saucer" , 18648:"101.236.56-cup" , 18649:"101.328.92" , 18650:"200.572.55" , 18652:"200.847.15" , 18654:"300.834.71" , 18655:"200.921.07" , 18656:"201.327.78" , 18658:"201.323.68" , 18659:"201.324.48" , 18660:"201.416.26saucer" , 18661:"201.416.26cup" , 18662:"300.151.23" , 18663:"300.631.28saucer" , 18664:"300.63.28cup" , 18701:"301.333.91saucer" , 18702:"301.333.91cup" , 18703:"401.324.52" , 18704:"401.463.45" , 18705:"501.161.78" , 18706:"600.572.58" , 18707:"600.632.97" , 18708:"600.817.34" , 18709:"600.832.62sm" , 18710:"600.832.62lrg" , 18711:"601.317.05" , 18712:"700.580.64" , 18713:"701.323.99saucer" , 18714:"701.323.99cup" , 18715:"701.333.94cup" , 18716:"800.817.33" , 18717:"800.921.09" , 18718:"800.921.14" , 18735:"200.01.0168" , 18739:"200.01.0426-brown-smallest" , 18786:"242.11.4180" , 18787:"242.07.2123" , 18789:"242.09.6219-pitcher" , 18793:"242.02.5746" , 18804:"red_mug" , 18798:"tennis_ball_can" , 18740:"9099KCAB" , 18741:"GC180AW" , 18751:"tilex_spray" , 18743:"Atlantis" , 18745:"fructis_shampoo_bottle" , 18757:"Tide" , 18752:"Pantene" , 18756:"Arm & Hammer" , 18755:"Mop&Glo" , 18759:"clorox" , 18760:"all" , 18754:"CR-6000" , 18761:"OB36/OB03" , 18772:"megabloks1x3_tall_yellow" , 18773:"megabloks1x4_short_blue" , 18782:"kleenex_box" , 18774:"megabloks1x4_tall_red" , 18758:"Downy ultra" , 18775:"megabloks2x2_tall_blue" , 18794:"simple_green" , 18776:"megabloks2x4_yellow" , 18790:"sterile_pads" , 18777:"megabloks_single_yellow" , 18753:"Pledge" , 18762:"milk-1gal" , 18763:"orange_juice" , 18764:"All-small" , 18720:"900.444.86cup" , 18721:"901.163.79" , 18723:"200.03.1152" , 18725:"200.01.3598" , 18726:"200.01.3345" , 18727:"200.01.3346" , 18728:"200.01.3477" , 18729:"200.01.0773" , 18730:"200.01.0169" , 18731:"200.01.0422" , 18732:"200.01.4266" , 18733:"200.01.0271" , 18734:"200.01.3463" , 18736:"200.01.0426-green-large" , 18737:"200.01.0426-orange-med" , 18738:"200.01.0426-blue-small" , 18747:"solo_plastic_bowl" , 18748:"solo_plastic_cup" , 18973:"big_plate" , 18749:"dixie_paper_bowl" , 18768:"milk-carton" , 18769:"megabloks1x2_countour_yellow" , 18778:"megabloks2x2_short_red" , 18770:"megabloks1x2_short_yellow" , 18771:"megabloks1x2_tall_green" , 18780:"Oatmeal_crisp" , 18781:"shredded_wheat" , 18795:"power_scissors" , 18806:"organic chai" , 18801:"Dove_bar" , 18802:"hydrogen_peroxide_bottle" , 18666:"000.921.13" , 18667:"001.172.98" , 18668:"001.327.79" , 18669:"100.572.51" , 18670:"200.580.66" , 18671:"200.919.28" , 18672:"210.327.78" , 18673:"300.814.67" , 18674:"300.919.23" , 18675:"301.334.90" , 18676:"400.580.65" , 18677:"401.376.90" , 18678:"401.431.44" , 18679:"463.156.00" , 18680:"500.151.22" , 18681:"500.302.12" , 18682:"500.312.83" , 18683:"500.919.41" , 18685:"501.245.12" , 18686:"501.330.69" , 18687:"601.349.35" , 18688:"700.302.11" , 18689:"701.330.68" , 18690:"763.305.00" , 18692:"800.919.49" , 18693:"801.327.80" , 18695:"801.348.21" , 18696:"801.463.53" , 18697:"901.256.99" , 18698:"901.317.04" , 18700:"963.111.00" , 18750:"VF_papaer_bowl" , 18767:"Country_Crock15" , 18784:"242.07.6610" , 18785:"242.07.6602" , 18792:"travel_mug" , 18746:"mach3_gel" , 18779:"odwalla_bottle" , 18765:"coffee-mate" , 18766:"suave-kids-3in1" , 18783:"izze_can" , 18791:"v8_bottle" , 18796:"Chaibaby_tea" , 18797:"rishi_tea_jas" , 18799:"Clearasil_jar" , 18800:"contact lens cleaner" , 18807:"campbell_soup_can" , 18808:"campbell_soup_handheld" , 18809:"cylinder_radius_0.02785_height_0.315" , 18635:"000.919.29" , 18657:"301.290.30" , 18665:"000.580.67" , 18684:"501.161.83" , 18691:"800.572.57" , 18699:"901.334.73" , 18719:"900.444.86saucer" , 18724:"200.03.1301" , 18788:"242.09.6219-glass" , 18812:"book" , 18813:"cell_phone" , 18814:"cordless_phone" , 18815:"fork" , 18816:"eyeglasses" , 18817:"lighter" , 18818:"medicine_pill" , 18819:"mug" , 18820:"pen" , 18821:"prescription_bottle" , 18822:"soap" , 18823:"spoon" , 18824:"straw" , 18825:"toothbrush" , 18826:"toothpaste" , 18827:"tv_remote" , 18828:"walking_cane" , 18829:"wallet" , 18830:"wrist_watch" , 18694:"801.334.78" , 18722:"901.125.07" , 18633:"sports water bottle" , 18744:"Coke_classic" , 18832:"plate" , 18928:"Amys bowls country cheddar" , 18932:"face mug someother" , 18934:"hotel card" , 18974:"little_bowl" , 18936:"Mop and Glo" , 18937:"Nantucket Watermelon Strawberry" , 18938:"Nature's Path Organic Peanut Butter Granola" , 18939:"Oi Ocha" , 18940:"Remote Control" , 18943:"ROS PHD Comic" , 18944:"soup spaghettio" , 18945:"sphaghetti" , 18946:"Tecate" , 18948:"Trader Joe's Paneer Tikka Masala" , 18951:"sour cream" , 18952:"small cup" , 18953:"tall glass" , 18954:"boss bottle" , 18955:"valentino ball" , 18956:"wine glass" , 18957:"boss box" , 18958:"yellow cup" , 18959:"small glass" , 18960:"curved bottle" , 18961:"small mug" , 18962:"glass bowl" , 18949:"ziplock" , 18931:"Eggo" , 18930:"Egg Carton" , 18941:"Robot Cards" , 18942:"Robot Power" , 18933:"Honey Bunches" , 18929:"Clorox" , 18935:"Mini Mouse Bank" , 18947:"Tide 2x" , 18963:"arm and hammer" , 18964:"black pepper" , 18965:"french's mustard" , 18966:"pledge" , 18967:"woolite" , 18968:"Bon Ami" , 18969:"Pam" , 18970:"Kona Coffee Can" , 18972:"big_bowl" , 18975:"little_sushi_bowl" , 18976:"big_sushi_bowl" , 18977:"little_sushi_cup" , 18978:"big_sushi_cup" , 18979:"little_sushi_plate" , 18980:"big_sushi_plate" }
for elem in id:
	open_name = str(elem) + ".txt"
	save_name = "STL/" + id_map[elem] + ".stl"
	g = open(open_name, "r")
	triangles = []
	part2 = 0
	vertices = []
	readCount = 0
	d = 0
	e = 0
	f = 0
	for line in g:
	    if (part2 == 0):
	        if (line == '\n'):
	            continue
	        elif len(line.strip().split()) == 0:
	            continue
	        elif len(line.strip().split()) == 1:
	            # print "new part reached"
	            part2 = 1
	            d = line.rstrip()
	            d = float(d)
	            readCount += 1
	        else:
	            # print(line)
	            # print(len(line.strip().split()))
	            line = line.strip()
	            a, b, c = line.split(",")
	            c.strip('\n')
	            a = int(a)
	            b = int(b)
	            c = int(c)
	            # print("(" + str(a) + "," + str(b) + "," + str(c) + ")")
	            triangles.append((a, b, c))
	    else:
	        # print(readCount)
	        # print(line)
	        if (line == '\n'):
	            readCount = 0
	            continue
	        if (len(line.rstrip()) == 0):
	            readCount = 0
	            continue
	        elif readCount == 0:
	            d = line.rstrip()
	            d = float(d)
	            readCount += 1
	        elif readCount == 1:
	            e = line.rstrip()
	            e = float(e)
	            readCount += 1
	        elif readCount == 2:
	            # print("printing f")
	            f = line.rstrip()
	            # print(f)
	            f = float(f)
	            readCount += 1
	            vertices.append((d, e, f))
	npTriangle = np.array(triangles)
	# print(npTriangle)
	npVertex = np.array(vertices)
	# print(npVertex)
	# f = open("vertices.txt", "r")
	# vertices = []
	# readCount = 0
	# d = 0
	# e = 0
	# f = 0
	# for line in f:
	#     if (line == '\n'):
	#         readCount = 0
	#         continue
	#     elif readCount == 0:
	#         d = line.rstrip()
	#         d = float(d)
	#         readCount += 1
	#     elif readCount == 1:
	#         e = line.rstrip()
	#         e = float(e)
	#         readCount += 1
	#     elif readCount == 2:
	#         f = line.rstrip()
	#         f = float(f)
	#         readCount += 1
	#         vertices.append((d, e, f))

	# npVertex = np.array(vertices)
	# print(npVertex)
	#
	cube = mesh.Mesh(np.zeros(npTriangle.shape[0], dtype=mesh.Mesh.dtype))
	for i, f in enumerate(npTriangle):
	    for j in range(3):
	        cube.vectors[i][j] = npVertex[f[j],:]
	#
	g.close()
	# # Write the mesh to file "cube.stl"
	cube.save(save_name)
