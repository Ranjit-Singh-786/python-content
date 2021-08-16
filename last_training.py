# this syntex use for concate multiple csv file in single csv file
import numpy as np
import os
import pandas as pd
import matplotlib.pylot as plt
path =".sales_data"
files = [file for file in os.listdir(path)]
all_month_data = pd
for file in false:
    current_datA = pd.concat([all_month_data,current_datA])
all_month_data,to_csv("all_data.csv",index=false)
print("all csv merge in single csv file")


# ,,,,,,,,, clean up the data
all_data.isnull().sum()           #for chek missing value in dataset
#,,,,,,,,,,and now we drop the row that contain a missing value or null
all_data = all_data.dropna(how='all')      #for drop all missing or 