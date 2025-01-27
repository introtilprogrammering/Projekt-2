## Data aggregation function

#slettes
from dataload import load_measurements
[tvec,data] = load_measurements("2008.csv", "forward fill")


# Function allow user to aggregate data
def aggregate_measurements(tvec, data):
    tvec_a = tvec
    data_a = data

    # While loope allow user to selct with month he/she wants to aggregate. 
    while True:
        try:
            # Allow user to input the number of the month or all
            month =input('Wich month do you want?:  ')
            month =month.lower()
            # If user write all then there will not be sorted in the months
            if month == 'all':
                break
            # If user write a word other than all then the string is being tranform to a a integred number  
            else:
                month = int(month)
            if (month < 1) or (month > 12):
                print('Month {:d} does not exsist. Try again!'.format(month))
                pass
            elif any( tvec.month == month):
                data_a = data_a[tvec_a.month ==month]
                tvec_a = tvec_a[tvec_a.month == month]
                break
            else: 
                print('Month {:d} is not in the data . Try another month.'.format(month))
                pass
        except ValueError:
            pass


    while True:
        try:
            day = input('Which day do you want?:  ')
            day =day.lower()
            if day == 'all':
                break
            else:
                day = int(day)
            if ( day < 1) or ( day > 31):
                print('Day {:d} does not exsist. Try again!'.format(day))
                pass
            elif any ( tvec_a.day == day ):
                data_a = data_a[tvec_a.day == day]
                tvec_a = tvec_a[tvec_a.day == day]
                break
            else: 
                print('Day {:d} is not in the data . Try another month.'.format(day))
                pass
        except ValueError:
            pass


    while True:
        try:
            hour = input('Which hour do you want?:  ')
            hour =hour.lower()
            if hour == 'all':
                break
            else:
                hour = int(hour)
            if ( hour < 0) or ( hour > 23):
                print('Hour {:d} does not exsist. Try again!'.format(hour))
                pass
            elif any ( tvec_a.hour == hour ):
                data_a = data_a[tvec_a.hour == hour]
                tvec_a = tvec_a[tvec_a.hour == hour]
                break
            else: 
                print('Day {:d} is not in the data . Try another month.'.format(day))
                pass
        except ValueError:
            pass

    return (tvec_a, data_a)