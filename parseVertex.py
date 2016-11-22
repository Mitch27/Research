#!/usr/bin/python
import numpy as np
from stl import mesh

f = open("triangles.txt", "r")
triangles = []
for line in f:
    if (line == '\n'):
        continue
    else:
        line = line.strip()
        a, b, c = line.split(",")
        c.strip('\n')
        a = int(a)
        b = int(b)
        c = int(c)
        # print("(" + str(a) + "," + str(b) + "," + str(c) + ")")

        triangles.append((a, b, c))
npTriangle = np.array(triangles)
print(npTriangle)

f = open("vertices.txt", "r")
vertices = []
readCount = 0
a = 0
b = 0
c = 0
for line in f:
    if (line == '\n'):
        readCount = 0
        continue
    elif readCount == 0:
        a = line.rstrip()
        a = float(a)
        readCount += 1
    elif readCount == 1:
        b = line.rstrip()
        b = float(b)
        readCount += 1
    elif readCount == 2:
        c = line.rstrip()
        c = float(c)
        readCount += 1
        vertices.append((a, b, c))

npVertex = np.array(vertices)
print(npVertex)

cube = mesh.Mesh(np.zeros(npTriangle.shape[0], dtype=mesh.Mesh.dtype))
for i, f in enumerate(npTriangle):
    for j in range(3):
        cube.vectors[i][j] = npVertex[f[j],:]

# Write the mesh to file "cube.stl"
cube.save('cube.stl')
