"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
from collections import defaultdict
from datetime import datetime

telephone_time = defaultdict(int)
for caller, reciever, timestamp, duration in calls:
    date = datetime.strptime(timestamp, "%d-%m-%Y %H:%M:%S")
    if date.year == 2016 and date.month == 9:
        telephone_time[caller] += int(duration)
        telephone_time[reciever] += int(duration)

    max_call_time = 0
    max_telephone_num = ''
    for tel in telephone_time:
        if telephone_time[tel] >= max_call_time:
            max_call_time = telephone_time[tel]
            max_telephone_num = tel

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(max_telephone_num, max_call_time))