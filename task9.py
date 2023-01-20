from datetime import *
import portion as p
from collections import *
'''
Take two datetimes from user start_time and end_time. Calculates the difference between start_time and end_time by 
removing night intervals (12 AM to 6 AM). (Hint: You can use python intervals module)
'''

start_date = datetime(2023,1,10,3, 00, 00)
end_date = datetime(2023,1,15,3,00,00)
diff_date = end_date - start_date
intervals = timedelta(hours = 6) * diff_date.days
print(diff_date - intervals)


#take two datetimes input
start_date_time = input('Enter start time DD-MM-YYYY H:M:S format:~ ')
end_date_time = input('Enter end time DD-MM-YYYY H:M:S in 24 hours format:~ ')

start_date_time = datetime.strptime(start_date_time,'%d-%m-%Y %H:%M:%S')
end_date_time = datetime.strptime(end_date_time,'%d-%m-%Y %H:%M:%S')

#find difference between two dates
date_difference = end_date_time - start_date_time

#find interval between start date and end date
start_end_interval = p.closed(start_date_time,end_date_time)

#find night interval
night_times = []
while start_date_time <= end_date_time:
    night_times.append(p.closed(datetime.combine(start_date_time,time()),datetime.combine(start_date_time,time()) + timedelta(hours=6)))
    start_date_time += timedelta(days=1)

night_intervals = [start_end_interval&nights for nights in night_times]
remove_time = timedelta(0)

for i in range(len(night_intervals)):
    if not night_intervals[i].empty:
        tmp = night_intervals[i].upper - night_intervals[i].lower
        remove_time += tmp
print('Total time between two dates without night intervals:~ ',date_difference - remove_time) 