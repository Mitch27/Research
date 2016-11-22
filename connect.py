import psycopg2
import numpy
from stl import mesh
from struct import *
import base64
import binascii

try:
    conn = psycopg2.connect("dbname='household_objects-0.2' user='willow' host='0.0.0.0' password='willow' port='5432'")
    print "I am able to connect to the database"
    c = conn.cursor()
    c.execute('select original_model.original_model_model, mesh.mesh_vertex_list, mesh_triangle_list FROM public.original_model, public.mesh WHERE original_model.original_model_id = mesh.original_model_id')
    row = c.fetchall()[0]
#for row in c.fetchall():
    name = row[0]
    vertexLen = len(row[1])
    triangleLen = len(row[2])
    vertexString = str(row[1])
    base64_data =binascii.b2a_base64(vertexString)
    print(base64_data)
    # base64_data.decode('utf-8')
    # print(base64_data.decode('utf-32'))

    #vertexString.decode('base64','strict');
    # vertexString = struct.unpack('ddd', vertexString[])
    # print(vertexString[:12])
    #vertexList = np.frombuffer(row[1])
    #triangleList = np.frombuffer(row[2])
except:
    print "I am unable to connect to the database"
