#This scripts defines a projection for all the rasters in a single folder and then merges them.
#Can't be used with Python 2.7 (ArcMap python interpreter). To use with ArcMap change
#'arcpy.management.MosaicToNewRaster(...) with 'arcpy.MosaicToNewRaster_management(rasters_array,
# workspace, "raster_dataset_name_with_extension", coordinate_system_for_the_raster=projection, pixel_type= "32_BIT_FLOAT",
# cellsize=x, number_of_bands=x, mosaic_method="(FIRST or LAST)") and erase the brackets of 'print'.


#We import the neccessary modules:
import arcpy
import os;

#Set the path of the folder that contains the rasters:
arcpy.env.workspace = r"E:\DatosGIS\Datos_Globales\EMODNet\Europe_DTM_Bathymetry";
workspace = r"E:\DatosGIS\Datos_Globales\EMODNet\Europe_DTM_Bathymetry"

#We call the ListRasters function to list the rasters of a workspace (in this case E:\DatosGIS\Datos_Globales\EMODNet\Europe_DTM_Bathymetry
#workspace):
rasters = arcpy.ListRasters();

#We define the projection epsg:
projection = "4326"

#We define an empty array to store the rasters full path:
rasters_array = [];

#We add the rasters full path to the empty array:
for raster in rasters:
    rasters_array.append(os.path.join(workspace,raster))

#We define the projection of each raster in the folder:
for rast in rasters_array:
    arcpy.management.DefineProjection(rast, projection);

#We merge all the rasters from the folder ("europe.bathymetry.tif" is the name of the new raster with extension):
arcpy.management.MosaicToNewRaster(rasters_array, workspace, "europe_bathymetry.tif", number_of_bands="1", pixel_type= "32_BIT_FLOAT")
print(rasters_array)