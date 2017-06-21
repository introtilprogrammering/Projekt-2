import pandas as pd
import numpy as np
from makeDataFrame import dataFrame
from dataload import load_measurements


#[tvec,data] = load_measurements("2008.csv", "drop")
[tvec,data] = load_measurements("testdata1.csv", "drop")




if period == "hour of the day":
    #For hour of the day 
    data_a = [None]*24
    tvec_a = [None]*24
    
    for i in range(24):
        someDataHourOfDay = data[tvec.iloc[:,3] == i]
        someTvecHourOfDay = tvec[tvec.iloc[:,3] == i]
        if len(someTvecHourOfDay) > 0:
            data_a[i] = someDataHourOfDay.mean(axis = 0)
            tvec_a[i] = someTvecHourOfDay.iloc[0]
    
    [data_a,tvec_a] = dataFrame(data_a,tvec_a)  






if period == "day":
    #For dage
    data_a = [None]*366
    tvec_a = [None]*366
    current_day = 0
    
    for i in range (12):
        someData = data[tvec.iloc[:,1] == i+1]
        someTvec = tvec[tvec.iloc[:,1] == i+1]
        if len(someTvec) > 0:
            for j in range(31):
                someDataDay = someData[someTvec.iloc[:,2] == j+1]
                someTvecDay = someTvec[someTvec.iloc[:,2] == j+1]
                if len(someTvecDay) >0:
                    data_a[current_day] = someDataDay.sum(axis = 0)
                    tvec_a[current_day] = someTvecDay.iloc[0]
                    current_day = current_day + 1
                    
                    
    [data_a,tvec_a] = dataFrame(data_a,tvec_a)