#!/usr/bin/env python3
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


def get_longest_time(calls):

    phones_times = {}
    #First record
    max_key_value = ( calls[0][0], int(calls[0][3]) )

    # count = 0
    for rec in calls:

        caller = rec[0]
        receiver = rec[1]
        seconds = int(rec[3])
        

        if phones_times.get(caller):
            phones_times[caller] += seconds
        else:
            phones_times[caller] = seconds

        if phones_times.get(receiver):
            phones_times[receiver] += seconds
        else:
            phones_times[receiver] = seconds

        #Compare and add maximum value to max_key_value
        if phones_times[caller] > max_key_value[1]:
            max_key_value = ( caller, phones_times[caller] )
        if phones_times[receiver] > max_key_value[1]:
            max_key_value = ( caller, phones_times[receiver] )
        
    
    return {
        "number": max_key_value[0],
        "time": max_key_value[1]
        }

longest_time = get_longest_time(calls)

print(
f"{longest_time['number']} spent the longest time, {longest_time['time']} seconds, \
on the phone during September 2016."
)
