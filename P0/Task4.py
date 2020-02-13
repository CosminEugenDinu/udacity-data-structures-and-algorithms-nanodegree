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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""



def find_telemarketers(calls, texts):
    telemarketers = set()
    non_telemarketers = set()
    # callers comprise non_telemarketers and telemarketers numbers
    callers = set() 

    for call in calls:
        caller = call[0]
        receiver = call[1]
        
        callers.add(caller)
        non_telemarketers.add(receiver)
    
    for text in texts:
        sender = text[0]
        receiver = text[1]

        non_telemarketers.add(sender)
        non_telemarketers.add(receiver)
    
    telemarketers = callers.difference(non_telemarketers)

    return telemarketers
    
def print_result():
    telemarketers_sorted = sorted(find_telemarketers(calls, texts))
    telemarketers_str = ''
    for t in telemarketers_sorted:
        telemarketers_str += str(t) + '\n'
    print(
    "These numbers could be telemarketers: \n" +
    telemarketers_str
    )
print_result()

