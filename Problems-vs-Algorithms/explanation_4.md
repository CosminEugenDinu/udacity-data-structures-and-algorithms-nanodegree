The algorithm iterates through array once, keeping track of 3 indexes. `low_i` index for values <= 1 (mid value), `scan_i` index for mid values (will not be swapped) and `high_i` index for values >= 1.

Time complexity is O(n).

Space complexity is O(n). Algorithm swaps elements in place.