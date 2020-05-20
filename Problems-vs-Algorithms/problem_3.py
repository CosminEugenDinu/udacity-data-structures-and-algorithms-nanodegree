#!/usr/bin/env python3.8

from functools import reduce

def parent(i):
    return (i - 1) // 2

def left(i):
    return i * 2 + 1

def right(i):
    return i * 2 + 2

def heap_insert(heap, elem):
    heap.append(elem)
    i = len(heap) - 1
    temp = elem

    while(i > 0 and elem > heap[parent(i)]):
        heap[i] = heap[parent(i)]
        i = parent(i)

    heap[i] = elem

    return heap

def heap_delete(heap):
    if len(heap) == 0:
        return None
    if len(heap) == 1:
        return heap.pop() 

    root = heap[0]
    last = heap.pop()
    heap[0] = last

    i = 0
    while(right(i) < len(heap)):
        current = i
        grater = i

        # find the child with grater value        
        if heap[left(i)] > heap[right(i)]:
            grater = left(i)
        else:
            grater = right(i)
        
        # swap current with the grater child if current is smaller
        if heap[current] < heap[grater]:
            heap[current], heap[grater] = heap[grater], heap[current]
            i = grater
        else:
            break

    return root

def tow_max_sum(arr_digits):
    heap = reduce(heap_insert, arr_digits, [])
    num1_digits = []
    num2_digits = []
    
    while(len(heap)):

        num1_digits.append(heap_delete(heap))

        if len(heap):
            num2_digits.append(heap_delete(heap))
    

    def num_from_digits(digits_array):
        return reduce(
            lambda num, digit: num * 10 + digit,
            digits_array, 0
            )
    num1 = num_from_digits(num1_digits)
    num2 = num_from_digits(num2_digits)

    return [num1, num2]



   
def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """

    return tow_max_sum(input_list)

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_cases = [
    [[1, 2, 3, 4, 5], [542, 31]],
    [[4, 6, 2, 5, 9, 8], [964, 852]],
    [[7, 7, 5, 5, 0], [750, 75]],
    [[1, 1, 1], [11, 1]],
    [[0, 0, 0, 0], [0, 0]],
]

def test(test_cases, test_function):
    for test_case in test_cases:
        test_function(test_case)

test(test_cases, test_function)

