from datetime import *

'''
Take two datetimes from user start_time and end_time. Calculates the difference between start_time and end_time by 
removing night intervals (12 AM to 6 AM). (Hint: You can use python intervals module)
'''

startdate_str = datetime(2023,1,10,3, 00, 00)
enddate_str = datetime(2023,1,15,3,00,00)
diff_date = enddate_str - startdate_str
intervals= timedelta(hours=6)*diff_date.days
print(diff_date-intervals)

