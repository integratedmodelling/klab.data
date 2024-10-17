"""This code takes the fields of a shp, and makes a String
out of two columns"""

import geopandas as pg

path_to_data = r"C:\Users\ruben.crespo\Documents\03_tests\administrative_unit\global_countries.shp"
gdf = pg.read_file(path_to_data)

chain = "geography:" + gdf['english'] + ' if "' + gdf['iso3'] + '",' #we concatenate the string
print(type(chain)) #is a pandas type series
unique_chain = chain.unique #lets take unique values
chain.to_csv('out.csv',index=False) #we export the data into a csv
