## Algorithm description:
Uses a recursive algorithm `search` which takes: rotated list `in_list`, target value `number`, lower boundary index `low_i` and upper boundary `high_i`.

Base case: if `low_i` became `>` than `high_i` then target is not found (return -1).

Find the middle index `mid_i`. If target is found at mid_i, return `mid_i`.

Check if sequence from `low_i` to `mid_i` is sorted:

    if sorted:
        check if it contains number