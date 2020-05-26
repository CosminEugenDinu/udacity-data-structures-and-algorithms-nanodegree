`RouterTrie.insert` method `list` path_list and `str` handler and recursively iterates through items of path_list. With every recursion call traverses the Trie from current node to child node till reaches the end of the list (base case) and assigns handler to `handler` property of leaf node.

`RouterTrie.find` method has almost the same design as `insert`: recursively iterates through `path_list` looking for every path `path_item` (as key in `children` dict property of node) in traversed nodes. If it reaches the end of `path_list` and all keys exists, returns handler found at leaf node.

Time complexity:

- `insert` takes O(n)
- `find` takes O(n), where n is length of path

Space complexity:

- `insert` occupies O(n)
- `find` occupies O(n), n is length of path, corresponds with length of call stack of recursion.


