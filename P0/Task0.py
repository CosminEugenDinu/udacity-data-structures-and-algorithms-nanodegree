#!/usr/bin/env python3
"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
from datetime import datetime

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)


with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

def get_first_record(texts):

    format = '%d-%m-%Y %H:%M:%S'
    # Randomly chosen first record
    first_record = [
        texts[0][0], 
        texts[0][1], 
        datetime.strptime(texts[0][2], format)
        ]

    for rec in texts:
        curr_text_time = datetime.strptime(rec[2], format)
        if curr_text_time < first_record[2]:
            first_record = [rec[0], rec[1], curr_text_time]

    #Change type datetime to type str
    first_record[2] = first_record[2].strftime(format)
    return first_record

def get_last_record(calls):

    format = '%d-%m-%Y %H:%M:%S'

    last_record = calls[0][:]
    last_record[2] = datetime.strptime(last_record[2], format)

    for rec in calls:
        curr_time = datetime.strptime(rec[2], format)
        if curr_time > last_record[2]:
            last_record = [rec[0], rec[1], curr_time, rec[3]]

    #Change type datetime to type str
    last_record[2] = last_record[2].strftime(format)
    return last_record

#Test
def test():
    assert get_first_record(texts) == texts[0] 
    assert get_last_record(calls) == calls[5212]
test()


first_text_record = get_first_record(texts)
last_call_record = get_last_record(calls)

print(
f'First record of texts, {first_text_record[0]} \
texts {first_text_record[1]} at time {first_text_record[2]}'
)
print(
f'Last record of calls, \
{last_call_record[0]} calls {last_call_record[1]} \
at time {last_call_record[2]}, \
lasting {last_call_record[3]} seconds'
)
