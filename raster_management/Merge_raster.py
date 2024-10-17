#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Link: https://www.youtube.com/watch?v=sBBMKbAj8XE
from osgeo import gdal
import glob
import os
import subprocess #spans new processes

os.chdir(r"C:\Users\ruben.crespo\Documents\03_tests\MODIS_burned_area\test")
#I want a list of the files
modisList=glob.glob("modis_MCD64A1*.tif")
# print(modisList)

#we have to run gdal_merge as a command
cmd = "gdal_merge.py -o merged_MODIS.tif"
subprocess.call(cmd.split()+modisList)

#this is a virtualraster, not a raster, it indicates the data

# vrt = gdal.BuildVRT("merged.vert", modisList)
# gdal.Translate("merged2.tif", vrt, xRes = 0.002297718814582349299, yRed = -0.002297718814582349299)