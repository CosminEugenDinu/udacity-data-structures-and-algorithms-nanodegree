#!/usr/bin/env python3.8

def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """

    mid_val = 1

    low_i = 0
    scan_i = 0
    high_i = len(input_list)
    

    while (scan_i < high_i):
        if input_list[scan_i] < mid_val:
            input_list[low_i], input_list[scan_i] = input_list[scan_i], input_list[low_i]
            low_i += 1
            scan_i += 1
        elif input_list[scan_i] > mid_val:
            high_i -= 1
            input_list[scan_i], input_list[high_i] = input_list[high_i], input_list[scan_i]
        else: # input_list[scan_i] == mid_val
            scan_i += 1

    return input_list
        


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])