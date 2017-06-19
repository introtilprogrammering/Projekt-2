## Data aggregation function

#slettes

from dataload import load_measurements
import pandas as pd
import numpy as np

[tvec,data] = load_measurements("2008.csv", "drop")
priode = 'month'



tvec_a = []


if priode == 'month':
    tvec_a =[None]*12
    data_a = [None]*12
    for i in range (12):
        someData = data[tvec.month == i+1]
        
        
        
        someTvec = tvec[tvec.month == i+1]
                
        someData = someData.sum(axis=0)
        someData = np.array([someData])
        data_a[i] = someData
        a = pd.DataFrame(columns=[ 'Zone1','Zone2','Zone3','Zone4'])
        a[i] = someData
        


