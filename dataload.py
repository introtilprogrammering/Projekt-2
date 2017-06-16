#Import datafil
import os
import pandas as pd
os.chdir('/Users/michael/documents/GitHub/Projekt-2')

def load_measurements(filename, fmode):
    #Ved at bruge pandas læses datafilen
    data = pd.read_csv(filename, header = None)
    
    #Laver header til datasættet
    data.columns = ["year", "month", "day", "hour", "minute", "second", "zone1", 
    "zone2", "zone3", "zone4"]
    
    if fmode == "forward fill":
        if any(data.iloc[0,:] == -1) == True:
            data = data[data.zone1 != -1]
            data = data[data.zone2 != -1]
            data = data[data.zone3 != -1]
            data = data[data.zone4 != -1]
            print("Warning! There was invalid measurements in the first row of the dataframe")
        
        else:
            for i in range(len(data)):
                if any(data.iloc[i,:] == -1) == True:
                    data.iloc[i,:] = data.iloc[i-1,:]
        
        
    if fmode == "backward fill":
        if any(data.iloc[-1,] == -1) == True:
            data = data[data.zone1 != -1]
            data = data[data.zone2 != -1]
            data = data[data.zone3 != -1]
            data = data[data.zone4 != -1]
            print("Warning! There was invalid measurements in the last row of the dataframe")

        
        else:
            for i in range(len(data)):
                if any(data.iloc[i,:] == -1) == True:
                    data.iloc[i,:] = data.iloc[i+1,:]
                
    if fmode == "drop":
        data = data[data.zone1 != -1]
        data = data[data.zone2 != -1]
        data = data[data.zone3 != -1]
        data = data[data.zone4 != -1]
    
    tvec = data.iloc[:,:6]
    data = data.iloc[:,6:]
    
    return (tvec, data)

[tvec,data] = load_measurements("2008.csv", "forward fill")

