from displayMenu import displayMenu 
from dataload import load_measurements
#from dataStatistic import print_statistic
from agg import aggregate_measurements
#from agg import dataFrame
#from dataPlots import dataGraf
from dataPlots import dataPlot

import numpy as np
import pandas as pd

menuItems = np.array(["Indlaes data","Aggregér data", "Vis statestik",
"Visulisér elforbrug", "Afslut"])
menuItems2 = (["drop", 'forward fill', 'backward fill'])
menuItems3 = np.array(['Forbrug pr. minut (ingen aggregering)', 'Forbrug pr. time', 'Forbrug pr. dag', 'Forbrug pr. måned', 'Forbrug efter tid på dagen (timegennemsnit)'])
menuItems4 = np.array(["zone1","zone2","zone3","zone4","all","combined"])
print('Welcome to our script')
tekst = False


#
while True:
    print('\n')
    if tekst == False:
        print('No data has been read')
        print('\n')

     
    choice = displayMenu(menuItems)
    #Hvis man skriver 1 skal man indlæse data, filen skal ligge i program mappe
    if choice == 1:
        while True:
            try:
                fileName = input("Hvilken fil skal indlæses?: ")
                pd.read_csv(fileName)
                while True:
                    try: 
                        print("which fmode is wanted?:")
                        choice = displayMenu(menuItems2)
            
                        if choice == 1:
                            fmode = "drop"
                            
                        elif  choice == 2:
                            fmode = "forward fill"
                            
                        elif  choice ==3:
                            fmode = 'backward fill'
                            
                        elif any(choice != [1,2,3]):
                           raise ValueError
                        
                        [tvec,data] = load_measurements(fileName, fmode)
                        
                        tvec_a = tvec
                        data_a = data
                        tekst = True
                        break
                    except ValueError:
                        print('Not valid option, please choose again')
                        pass
                break
            except FileNotFoundError :
                print("Fil findes ikke, vælg venligst en gyldig fil")
                pass
        

    #Hvis man skriver 2 skal dataen aggregeres 
    elif choice == 2:
        while tekst == True:
            try:
                choice = displayMenu(menuItems3)
                if choice == 1:
                    data_a = data
                    tvec_a = tvec
                elif  choice == 2:
                    period = "hour"
                elif choice == 3 :
                    period = "day"
                elif choice == 4: 
                    period = "month"
                elif choice == 5: 
                    period= "hour_of_the_day"
                [tvec_a,data_a]= aggregate_measurements(tvec,data,period)
                break
            
            except:
                break
            

            


    #hvis man skriver 3 skal der vises statistik
    elif choice == 3:
            
        try:
            #print(menuitems2[/periode])
            print_statistic(tvec, data)
        except NameError:
            print("Indlaes først gyldig fil")

    
    #Hvis man skriver 4 vises plots for valgte data
    elif choice == 4:
        while tekst == True:
            try:
                choice = displayMenu(menuItems4)
                if choice == 1:
                    zone = "zone1"
                    tvec_a = tvec
                elif  choice == 2:
                    zone = "zone2"
                elif choice == 3 :
                    zone = "zone3"
                elif choice == 4: 
                    zone = "zone4"
                elif choice == 5: 
                    zone= "all"
                elif choice == 6: 
                    zone= "combined"
                dataPlot(data_a, tvec_a, zone)
            except :
                    break
     
    elif choice == 5:
        print("Tak for at bruge vores program! :-)")
        break
