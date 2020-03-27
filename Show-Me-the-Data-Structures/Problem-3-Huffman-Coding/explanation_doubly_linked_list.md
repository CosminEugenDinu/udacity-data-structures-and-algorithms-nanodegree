Class `Doubly_linked_list` at instantiation creates `header` and `trailer` nodes, which does not stores values; are used for fast lookup and insert at head or trail of linked list.

Defines method `insert` which takes `element` to be inserted, `predecessor` node and `successor` node references from the corresponding linked list.
Time complexity of `insert` method is O(1). Space complexity is O(1).

Defines method `delete` which takes node reference as argument, deletes that node from linked list and returns the `element` property of that node.
Time complexity of `delete` method is O(1).

