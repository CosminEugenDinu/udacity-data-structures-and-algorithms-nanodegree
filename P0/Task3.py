#!/usr/bin/env python3
"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re
from functools import reduce

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


bangalore_re = re.compile(r'(\(080\))\d{7}')
fixed_re = re.compile(r'(\(0\d+\))\d+')
mobile_re = re.compile(r'([789]\d{3})\d{1}\s\d{5}')
telemarketer_re = re.compile(r'(140)\d+')

def get_code(num):
  
  is_bangalore = bangalore_re.match(num)
  if is_bangalore:
    return (is_bangalore.groups()[0], "bangalore")

  is_fixed = fixed_re.match(num)
  if is_fixed:
    return (is_fixed.groups()[0], "fixed")

  is_mobile = mobile_re.match(num)
  if is_mobile:
    return (is_mobile.groups()[0], "mobile")
  
  is_telemarketer = telemarketer_re.match(num)
  if is_telemarketer:
    return (is_telemarketer.groups()[0], "telemarketer")
  

def areas_called(caller_re, calls):
  areas_codes = dict()

  for call in calls:
    caller = call[0]
    receiver = call[1]

    if caller_re.match(caller):
      area_code_type = get_code(receiver)
      code = area_code_type[0]

      if areas_codes.get(code):
        areas_codes[code] += 1
      else:
         areas_codes[code] = 1

  return areas_codes

def one_line_item_str(items):
  str_new_line = ""
  for i in items:
    str_new_line += str(i) + '\n'
  return str_new_line


def test_re(): 
  bangalore = fixed = mobile = telemarketer = 1

  cases = (
    ("(080)64765396", (bangalore, fixed, 0, 0)),
    ("(022)38214945", (0, fixed, 0, 0)),
    ("78993 89387", (0, 0, mobile, 0)),
    ("1404787681", (0, 0, 0, telemarketer))
    )

  def find(num, re_obj):
    return 1 if re_obj.match(num) else 0

  re_objs = (bangalore_re, fixed_re, mobile_re, telemarketer_re)
  for case in cases:
    for i, _ in enumerate(case[1]):
      assert find(case[0], re_objs[i]) == case[1][i]
      

  print('All test_re passed!')

def test_get_code():
  cases = (
    ("(080)64765396", "(080)", "bangalore"),
    ("(022)38214945", "(022)", "fixed"),
    ("78993 89387", "7899", "mobile"),
    ("98453 94494", "9845", "mobile"),
    ("1404787681", "140", "telemarketer"),
    ("(0471)6537077", "(0471)", "fixed"),
    ("(04344)322628", "(04344)", "fixed")
    )
  for case in cases:
    try:
      assert get_code(case[0]) == (case[1], case[2])
    except AssertionError:
      print(f'test_get_code failed with (case[1], case[2]) {(case[1], case[2])}')
      return

  print('All test_get_code passed!')

def tests():
  test_re()
  test_get_code()
# tests()

codes_dict = areas_called(bangalore_re, calls)
codes = codes_dict.keys()
codes_sorted = sorted(codes)

print(
"The numbers called by people in Bangalore have codes: \n" +
one_line_item_str(codes_sorted)
)

total_calls = reduce(lambda acc, cur: acc + cur, codes_dict.values(), 0)
bangalore_calls = codes_dict['(080)']
per = bangalore_calls * 100 / total_calls


print(
"{val:.2f} percent of calls from fixed lines in Bangalore are calls \
to other fixed lines in Bangalore. \
".format(val=per))
