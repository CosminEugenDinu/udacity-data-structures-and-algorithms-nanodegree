## Algorithm description:
Uses a recursive algorithm `search` which takes: rotated list `in_list`, target value `number`, lower boundary index `low_i` and upper boundary `high_i`.

Base case: if `low_i` became `>` than `high_i` then target is not found (return -1).

Find the middle index `mid_i`. If target is found at mid_i, return `mid_i`.

Check if sequence from `low_i` to `mid_i` is sorted:

    if sorted:
        check if it contains number
            if contains number: binary search in that sequence (low_i to mid_i-1)
            if does not contains number: search in the other half

If sequence from `low_i` to `mid_i` is NOT sorted:

    then sequence from `mid_i` to `high_i` should be sorted, and then:
    check if it contains number:
        if contains number: binary search (mid_i+1 to high_i)
        else: repeat in the other half (low_i to mid_i-1)


Time complexity is O(log n) because with every call algorithm halves the input (n) with every function call.

Space complexity is also O(log n), corresponding with the call stack of recursion.