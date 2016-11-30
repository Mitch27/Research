#!/usr/bin/python
import numpy as np
from stl import mesh
id = [18742,18805,18803,18637,18638,18640,18641,18642,18644,18645,18646,18647,18648,18649,18650,18652,18654,18655,18656,18658,18659,18660,18661,18662,18663,18664,18701,18702,18703,18704,18705,18706,18707,18708,18709,18710,18711,18712,18713,18714,18715,18716,18717,18718,18735,18739,18786,18787,18789,18793,18804,18798,18740,18741,18751,18743,18745,18757,18752,18756,18755,18759,18760,18754,18761,18772,18773,18782,18774,18758,18775,18794,18776,18790,18777,18753,18762,18763,18764,18720,18721,18723,18725,18726,18727,18728,18729,18730,18731,18732,18733,18734,18736,18737,18738,18747,18748,18973,18749,18768,18769,18778,18770,18771,18780,18781,18795,18806,18801,18802,18666,18667,18668,18669,18670,18671,18672,18673,18674,18675,18676,18677,18678,18679,18680,18681,18682,18683,18685,18686,18687,18688,18689,18690,18692,18693,18695,18696,18697,18698,18700,18750,18767,18784,18785,18792,18746,18779,18765,18766,18783,18791,18796,18797,18799,18800,18807,18808,18809,18635,18657,18665,18684,18691,18699,18719,18724,18788,18812,18813,18814,18815,18816,18817,18818,18819,18820,18821,18822,18823,18824,18825,18826,18827,18828,18829,18830,18694,18722,18633,18744,18832,18928,18932,18934,18974,18936,18937,18938,18939,18940,18943,18944,18945,18946,18948,18951,18952,18953,18954,18955,18956,18957,18958,18959,18960,18961,18962,18949,18931,18930,18941,18942,18933,18929,18935,18947,18963,18964,18965,18966,18967,18968,18969,18970,18972,18975,18976,18977,18978,18979,18980]
g = open("18644.txt", "r")
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
            print "new part reached"
            part2 = 1
            d = line.rstrip()
            d = float(d)
            readCount += 1
        else:
            print(line)
            print(len(line.strip().split()))
            line = line.strip()
            a, b, c = line.split(",")
            c.strip('\n')
            a = int(a)
            b = int(b)
            c = int(c)
            # print("(" + str(a) + "," + str(b) + "," + str(c) + ")")
            triangles.append((a, b, c))
    else:
        print(readCount)
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
print(npTriangle)
npVertex = np.array(vertices)
print(npVertex)
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
cube.save('STL/18644.stl')
