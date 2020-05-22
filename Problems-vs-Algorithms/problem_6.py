#! /usr/bin/env python3.8

# should run in O(n) time

def get_min_max(ints):

    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
        ints(list): list of integers containing one or more integers
    """
    min = ints[0]
    max = ints[0]

    for num in ints:
        if max < num:
            max = num
        if num < min:
            min = num

    print(min, max)
    return min, max

    



## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")


l = [i for i in range(2, 55)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((2, 54) == get_min_max(l)) else "Fail")

l = [i for i in range(-13, 44)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((-13, 43) == get_min_max(l)) else "Fail")

l = [i for i in range(0, 1)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((0, 0) == get_min_max(l)) else "Fail")