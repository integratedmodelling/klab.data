"""
This script allows to download a recurring period over several years via the Copernicus Marine MOTU Client
"""

import os
from datetime import datetime, timedelta
import getpass

# Copernicus Marine Credentials 
USERNAME = input("Enter your username: ")
PASSWORD = getpass.getpass("Enter your password: ")

# Work directory
out_dir = r'path/to/working_directory'

# product and dataset IDs (Take from https://data.marine.copernicus.eu/viewer/expert)
serviceID = "GLOBAL_ANALYSISFORECAST_WAV_001_027"
productID = "cmems_mod_glo_wav_anfc_0.083deg_PT3H"
variable_name = "Temperature"

#coordinates
lon = (-180 , 180)
lat = (-90 , 90)

# variable 
var = "VHM0_SW1"

# Boundary dates
start_date = datetime(2020, 1, 1, 3)
end_date = datetime(2020, 1, 31, 23)
delta_t=timedelta(days=1)
# Download loop 
while start_date <= end_date:

    # Output filename
    out_name = f"{variable_name}_{start_date.year}_{start_date.month}_{start_date.day}.nc"
    
    if start_date.month == 1:
        # Motuclient command line
        query = f'python -m motuclient --motu https://nrt.cmems-du.eu/motu-web/Motu \
        --service-id {serviceID}-TDS --product-id {productID}-i \
        --longitude-min {lon[0]} --longitude-max {lon[1]} --latitude-min {lat[0]} --latitude-max {lat[1]}\
        --date-min "{start_date}" --date-max "{start_date+delta_t}" \
        --variable {var} \
        --out-dir {out_dir} --out-name {out_name} --user {USERNAME} --pwd {PASSWORD}'        
    
        print(f"============== Running request on {start_date} ==============")
        print(query[:-30])
        
        # Run the command
        os.system(query)
        
        start_date=start_date.replace(day=start_date.day+1)
        
print(f"============== Download completed! All files are in your directory {out_dir} ==============")