import os
import glob
import pandas as pd

#changes the current directory to the specified path
os.chdir(r"C:\Users\ruben.crespo\Documents\03_tests\MODIS_burned_area\modis\2020")

extension = 'csv'
#We create a list. {}= takes the name of the file.csv in format extension
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])


#export to csv in working folder
combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')

print("congratulations, the script is over")