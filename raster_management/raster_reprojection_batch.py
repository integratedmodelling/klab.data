"""This script goes for every tif file in a folder"""

import os
from sys import path
from osgeo import gdal


in_path=r"C:/Users/ruben.crespo/Desktop/nlc_reprojected"
out_path = "C:/Users/ruben.crespo/Desktop/out"

#This iterates for every file in the directory
for file in os.listdir(in_path):
    #we only take the ones ended with tif
    if file.endswith('.tif'):
        #print(path+"/"+file)
        path = in_path +"/"+ file
        out = out_path +"/WGS84_"+ file
        print(out)
        #here is the GDAL transformation
        gdal.Warp(out, path, dstSRS = "EPSG:4326")
    else:
        pass
print("It's over")
