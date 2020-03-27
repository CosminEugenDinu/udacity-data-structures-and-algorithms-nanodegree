
The LRU_Cache class is implemented with a doubly linked list for keeping track of nodes order and a `hash` dictionary for storing references to nodes.

Method `get` takes `key` as argument and return associated node.value, accessing `hash` dictionary by the key provided and moves the requested node to head of linked list.
Time complexity of `get` method is O(1).
Space complexity of `get` method is O(1).

Method `set` takes `key` and `value` as arguments, get node reference from `hash` dict by accessing key, if key exists rewrite node.value and move node to head, otherwise creates node, append to linked list head, store node reference in `hash` dict at key `key` and delete last accessed node from tail of linked list and corresponding ref from hash if `capacity` is exceeded.
Time complexity of `set` method is O(1).
Space complexity of `set` method is O(1).
