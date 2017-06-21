
from dataload import load_measurements
import pandas as pd
import numpy as np

[tvec,data] = load_measurements("testdata1.csv", "drop")


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


#For dage
data_a = [None]*366
tvec_a = [None]*366
current_day = 0

for i in range (12):
    someData = data[tvec.iloc[:,1] == i+1]
    someTvec = tvec[tvec.iloc[:,1] == i+1]
    for j in range(31):
        someDataDay = someData[someTvec.iloc[:,2] == j+1]
        someTvecDay = someTvec[someTvec.iloc[:,2] == j+1]
        if not someTvecDay.empty:
            data_a[current_day] = someDataDay.sum(axis = 0)
            tvec_a[current_day] = someTvecDay.iloc[0]
            current_day = current_day + 1
            
data_a = np.array(data_a)
tvec_a = np.array(tvec_a)
tvec_a = pd.DataFrame(tvec_a, columns = ['year','month','day','hour','minut','seconds'])
data_a = pd.DataFrame(data_a, columns = ['zone1','zone2','zone3','zone4'])



#For timer 
data_aa = [None]*366
tvec_aa = [None]*366
data_a = [None]*366*24
tvec_a = [None]*366*24
current_hour = 0
         
for i in range (12):
    someData = data[tvec.iloc[:,1] == i+1]
    someTvec = tvec[tvec.iloc[:,1] == i+1]
    for j in range(31):
        someDataDay = someData[someTvec.iloc[:,2] == j+1]
        someTvecDay = someTvec[someTvec.iloc[:,2] == j+1]       
        if not someTvecDay.empty:
            for k in range(24):
                someDataHour = someDataDay[someTvecDay.iloc[:,3] == k]
                someTvecHour = someTvecDay[someTvecDay.iloc[:,3] == k]
                data_a[current_hour] = someDataHour.sum(axis = 0)
                tvec_a[current_hour] = someTvecHour.iloc[0]
                current_hour = current_hour + 1
          
data_a = np.array(data_a)
tvec_a = np.array(tvec_a)
tvec_a = pd.DataFrame(tvec_a, columns = ['year','month','day','hour','minut','seconds'])
data_a = pd.DataFrame(data_a, columns = ['zone1','zone2','zone3','zone4'])




#For hour of the day 
data_a = [None]*24
tvec_a = [None]*24

for i in range(24):
    someDataHourOfDay = data[tvec.iloc[:,3] == i]
    someTvecHourOfDay = tvec[tvec.iloc[:,3] == i]
    data_a[i] = someDataHourOfDay.mean(axis = 0)
    tvec_a[i] = someTvecHourOfDay.iloc[0]

data_a = np.array(data_a)
tvec_a = np.array(tvec_a)
tvec_a = pd.DataFrame(tvec_a, columns = ['year','month','day','hour','minut','seconds'])
data_a = pd.DataFrame(data_a, columns = ['zone1','zone2','zone3','zone4'])    






