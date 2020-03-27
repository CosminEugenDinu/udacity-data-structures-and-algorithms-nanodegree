Algorithm `union` takes two linked lists as arguments and returns a third linked list containing union set of values from the first two lists.
Iterates in the same time over `llist_1` and `llist_2` and continue until the finish of longest one. With every iteration stores values as keys in `union_set_dict` once and append to `union_llist`.
Time complexity in case that all elements from `llist_1` are different from those in `llist_2` is O(n), where `n` is the sum of elements from both linked lists.
Space complexity is O(n).

Algorithm `intersection` takes tow linked lists as arguments and returns a third linked list containing a intersection set of values from first two lists.
Iterates in order over `llist_1`, then `llist_2`, store common values as keys in `intersection_set_dict` and append nodes with common values to `intersection_llist`.
Time complexity is O(n), where `n` is the sum of elements from `llist_1` and `llist_2`.
Space complexity is O(n/2) => O(n), worst case being when `llist_1` and `llist_2` contains only common values.
