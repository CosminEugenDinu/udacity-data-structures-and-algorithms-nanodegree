#!/usr/bin/env python3.8

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    rec_count = 0

    def search(in_list, number, low_i, high_i):
        nonlocal rec_count
        rec_count += 1

        if low_i > high_i:
            return -1
        
        mid_i = (low_i + high_i) // 2

        if number == in_list[mid_i]:
            return mid_i

        # if seq from low_i to mid_i is sorted
        if in_list[low_i] <= in_list[mid_i]:    
            if in_list[low_i] <= number < in_list[mid_i]:
                return search(in_list, number, low_i, mid_i-1)
            else:
                return search(in_list, number, mid_i+1, high_i)

        # if seq from low_i to mid_i is not sorted, then seq from mid_i
        # to high_i should be sorted
        else:
            if in_list[mid_i+1] <= number < in_list[high_i]:
                return search(in_list, number, mid_i+1, high_i)
            else:
                return search(in_list, number, low_i, mid_i-1)

        







    
    found_i = search(input_list, number, 0, len(input_list)-1)
    print(found_i)
    print("rec_count", rec_count)
    return found_i


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

