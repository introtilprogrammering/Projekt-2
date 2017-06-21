import matplotlib.pyplot as plt
from dataload import load_measurements
import pandas as pd
import numpy as np

"""[tvec,data] = load_measurements("2008.csv", "drop")
data_a = data
tvec_a = tvec
#For måneder
tvec_a =[None]*12
data_a = [None]*12
         
for i in range (12):
    someData = data[tvec.iloc[:,1] == i+1]
    someTvec = tvec[tvec.iloc[:,1] == i+1]
    data_a[i] = someData.sum(axis = 0)
    tvec_a[i] = someTvec.iloc[0]

data_a = pd.DataFrame(data_a)
tvec_a = pd.DataFrame(tvec_a)"""



#### HVIS IKKE DATA ER AGG SÆT DATA_A OG TVEC_A = DATA OG TVEC




def dataGraf(titel):
    plt.title(titel)
    plt.xlabel("Tid")
    plt.ylabel("El-forbrug")
    plt.ylim(ymin=0)
    plt.xlim(xmin=0)
    plt.legend(loc="upper right")
    plt.show()



def dataPlot(data_a,tvec_a,zone):
    if len(data_a) < 25:
        if zone == str("all"):
            ax = data_a[['zone1','zone2','zone3','zone4']].plot(kind='bar', title ="Consumption for all zones", figsize=(7, 5), legend=True, fontsize=9)
            
        elif zone == str("zone1"):
            ax = data_a[['zone1']].plot(kind='bar', title ="Consumption for zone 1", figsize=(7, 5), legend=True, fontsize=9)
        
        elif zone == str("zone2"):
            ax = data_a[['zone2']].plot(kind='bar', title ="Consumption for zone 2", figsize=(7, 5), legend=True, fontsize=9)
            
        elif zone == str("zone3"):
            ax = data_a[['zone3']].plot(kind='bar', title ="Consumption for zone 3", figsize=(7, 5), legend=True, fontsize=9)

        elif zone == str("zone4"):
            ax = data_a[['zone4']].plot(kind='bar', title ="Consumption for zone 4", figsize=(7, 5), legend=True, fontsize=9)

        elif zone == str("combined"):
            samlet_data = data_a.sum(axis=1)
            ax = samlet_data.plot(kind='bar', title ="Combined consumption ", figsize=(7, 5), legend=True,label="Combined", fontsize=9)
        ax.legend(ncol=2)
        ax.set_xlabel("Time", fontsize=9)
        ax.set_ylabel("Consumption", fontsize=9)
        plt.show()
        
        
    elif len(data_a) >= 25:
        if zone == str("all"):
            titel = "Consumption for all zones"
            plt.plot( np.arange(0,len(tvec_a)), data_a.iloc[:,3], 'r', label='Zone4')

            plt.plot(np.arange(0,len(tvec_a)), data_a.iloc[:,1], 'g' , label = 'Zone2')

            plt.plot(np.arange(0,len(tvec_a)), data_a.iloc[:,0], 'b', label = ' Zone1')  

            plt.plot(np.arange(0,len(tvec_a)), data_a.iloc[:,2], 'y', label = 'Zone3')
            dataGraf(titel)
        
        elif zone == str("zone1"):
            titel = "Consumption for zone 1"
            plt.plot(np.arange(0,len(tvec_a)), data_a.iloc[:,0], 'r', label='Zone1')
            dataGraf(titel)
        
        elif zone == str("zone2"):
            titel = "Consumption for zone 2"
            plt.plot(np.arange(0,len(tvec_a)), data_a.iloc[:,1], 'g', label='Zone2')
            dataGraf(titel)
            
        elif zone == str("zone3"):
            titel = "Consumption for zone 3"
            plt.plot(np.arange(0,len(tvec_a)), data_a.iloc[:,2], 'b', label='Zone3')
            dataGraf(titel)
        
        elif zone == str("zone4"):
            titel = "Consumption for zone 4"
            plt.plot(np.arange(0,len(tvec_a)), data_a.iloc[:,3], 'y', label='Zone4')
            dataGraf(titel)
        
        elif zone == str("combined"):
            titel = "Combined consumption"
            samlet_data = data_a.sum(axis=1)
            plt.plot(np.arange(0,len(tvec_a)), samlet_data, 'r', label='Combined data')
            dataGraf(titel)
                
""""dataPlot(data_a,tvec_a,"zone4")"""