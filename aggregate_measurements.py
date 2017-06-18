## Data aggregation function

#slettes
from dataload import load_measurements
[tvec,data] = load_measurements("testdata1.csv", "forward fill")



hour = ''
day = ''
month = 1
priode = [hour, day, month]



#def aggregate_measurements(tvec, data, period):
while True:
    month =int(input('Wich month do you want?:  '))
    if (month < 1) or (month > 12):
        print('Month {:d} does not exsist. Try again!'.format(month))
        pass
    elif any( tvec.month == month):
        data = data[tvec.month ==month]
        tvec = tvec[tvec.month == month]
        break
    elif month == 'all':
        break
    else: 
        print('Month {:d} is not in the data . Try another month.'.format(month))
        pass


if day != '':
    data = data[tvec.day ==day]
    tvec = tvec[tvec.day == day]

if hour !='':
    data = data[tvec.hour == hour]
    tvec = tvec[tvec.hour == hour]



any( tvec.month == 2)

#return (tvec_a, data_a)