## Data aggregation function

#slettes
import matplotlib.pyplot as plt
from dataload import load_measurements
import pandas as pd
import numpy as np

[tvec,data] = load_measurements("2008.csv", "drop")
periode = 'day'




if periode == 'month':
    tvec_a =[None]*12
    data_a = [None]*12
    for i in range (12):
        someData = data[tvec.month == i+1]
        someTvec = tvec[tvec.month == i+1]
        data_a[i] = someData.sum(axis = 0)
        tvec_a[i] = someTvec.iloc[0].values.tolist()

    data_a = pd.DataFrame(data = data_a)
    tvec_a = pd.DataFrame(tvec_a)


if periode == 'day':
    data_A = [None]*12
    tvec_a =[None]*31
    data_aa = [None]*31
    tvec_aa =  [None]*31
    for i in range (12):
        someData = data[tvec.month == i+1]
        someTvec = tvec[tvec.month == i+1]
        tvec_A =[None]*31
        data_aa = [None]*31
        for j in range(31):
            someDataDay = someData[someTvec.day == j+1].values
            someTvecDay = someTvec[someTvec.day == j+1].values
            someTvecDay  = pd.DataFrame(someTvecDay)
            data_aa[j] = someDataDay.sum(axis = 0)
            tvec_aa[j] = someTvecDay.iloc[0]
        data_A[i] = data_aa
        tvec_A[i] = tvec_aa
    data_A = pd.DataFrame(data = data_A)
    tvec_A = pd.DataFrame(tvec_a)
    
    data_a = np.stack(np.array(data_A).flatten())
    data_a = pd.DataFrame(data = data_a, columns = ["zone1","zone2","zone3","zone4"])
    data_a = data_a.loc[~(data_a==0).all(axis=1)]
