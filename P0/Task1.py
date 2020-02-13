#!/usr/bin/env python3
"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
def find_unique_num(calls, texts):
    numbers_set = set()

    for text_rec in texts:
        numbers_set.add(text_rec[0])
        numbers_set.add(text_rec[1])

    for call_rec in calls:
        numbers_set.add(call_rec[0])
        numbers_set.add(call_rec[1])

    return numbers_set


numbers = find_unique_num(calls, texts)
print(
f'There are {len(numbers)} different telephone numbers in the records.'
)