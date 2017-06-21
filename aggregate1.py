from dataload import load_measurements
import pandas as pd
import numpy as np

[tvec,data] = load_measurements("2008.csv", "drop")


#For måneder
tvec_a =[None]*12
data_a = [None]*12
         
for i in range (12):
    someData = data[tvec.iloc[:,1] == i+1]
    someTvec = tvec[tvec.iloc[:,1] == i+1]
    data_a[i] = someData.sum(axis = 0)
    tvec_a[i] = someTvec.iloc[0]

data_a = pd.DataFrame(data_a)
tvec_a = pd.DataFrame(tvec_a)

#.reset_index(drop=True)


monthData  = [31,29,31,30,31,30,31,31,30,31,30,31]

#For dage
data_A = [None]*12
tvec_A =[None]*12
   
for i in range (12):
    someData = data[tvec.month == i+1]
    someTvec = tvec[tvec.month == i+1]
    tvec_aa =[None]*monthData[i]
    data_aa = [None]*monthData[i]
    for j in range(monthData[i]):
        someDataDay = someData[someTvec.day == j+1]
        someTvecDay = someTvec[someTvec.day == j+1]
        data_aa[j] = someDataDay.sum(axis = 0)
        tvec_aa[j] = someTvecDay.iloc[0]
    data_A[i] = data_aa
    tvec_A[i] = tvec_aa
data_A = pd.DataFrame(data = data_A)
tvec_A = pd.DataFrame(tvec_A)

data_a =np.array(data_A)
data_a = pd.DataFrame(data_a)

data_a = np.stack(np.array(data_A).flatten())
data_a = pd.DataFrame(data_a, columns = ["zone1","zone2","zone3","zone4"])
data_a = data_a.loc[~(data_a==0).all(axis=1)]
