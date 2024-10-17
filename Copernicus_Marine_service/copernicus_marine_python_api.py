"""
This script allows to download a recurring period over several years via the Copernicus Marine Python API
"""

import os
from datetime import datetime
import getpass
import copernicusmarine

# Work directory
out_dir = r'path/to/working_directory'
os.chdir(out_dir)

# Copernicus Marine Credentials 
USERNAME = input("Enter your username: ")
PASSWORD = getpass.getpass("Enter your password: ")
copernicusmarine.login( username = USERNAME, password = PASSWORD)

# product and dataset IDs (Take from https://data.marine.copernicus.eu/viewer/expert)
productID = "cmems_mod_ibi_bgc_my_0.083deg-3D_P1M-m"

# coordinates
lon = (-12 , -5)
lat = (35 , 38)

# variables 
variables = ["chl", "nppv", "o2", "no3", "po4", "nh4", "ph"]
variable_name = "Biogeochemical"

# depths:
min_depth = 0
max_depth = 200

# Boundary dates
start_date = datetime(1993, 1, 1, 0)
end_date = datetime(2020, 11, 30, 23)

# Query:
copernicusmarine.subset(
  dataset_id = productID,
  variables = variables,
  minimum_longitude = lon[0],
  maximum_longitude = lon[1],
  minimum_latitude = lat[0],
  maximum_latitude = lat[1],
  start_datetime = start_date,
  end_datetime = end_date,
  minimum_depth = min_depth,
  maximum_depth = max_depth,
  output_filename = f"{variable_name}_{start_date.year}_{start_date.month}_{start_date.day}_to_{end_date.year}_{end_date.month}_{end_date.day}"
)