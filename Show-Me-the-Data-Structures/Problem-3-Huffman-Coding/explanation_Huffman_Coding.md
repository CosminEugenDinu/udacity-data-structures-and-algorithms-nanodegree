Algorithm `huffman_encoding` has dependencies:
- `Doubly_linked_list`
- `Tree`
- `frequencies`

`Doubly_linked_list` and `Tree` has corresponding explanations files.

Function `frequencies` takes `string` as argument, iterates over characters in `string`, stores them as keys in `chars_frqs` dict; values are number of occurrences. Time complexity is O(n), where `n` is len(`string`). Space complexity is O(n) in case every character is different.

Algorithm `huffman_encoding` takes `data` string as argument and returns tuple (`encoded_str`, `tree`). `tree` has `leaves_dict` property, a dict having key->`leaf_node_reference`: value->`character_from_data`. Tree leaf nodes stores character frequency at property `node.value`. Parent nodes stores sorted sum of frequencies.

Creates list `chars_frqs`, a sorted array (by frequencies) with tuples (`char`, `frq`). Time complexity is O(n log n), where `n` is number of characters in `data`.

Iterates over `chars_frqs`, add leaves nodes to doubly linked list `dll` (order is kept) and store leaf ref in `leaves_dict`; value is character.
Time complexity is O(n).

Iterates over `dll`. For every first two nodes (with first two minimum frequencies), delete them, add containing frequencies, create new `Tree.Node(added_frqs)`, call **find_position(new_TreeNode)** and insert it at corresponding position in `dll` (keeping order of frequencies). Time complexity of `find_position` is O(n*n). Deleting, inserting to `dll` and creation of `tree` takes O(1).

`get_chars_code(tree)` generates codes for every character. Time complexity is O(n).

The overall time complexity of `huffman_encoding` can be estimated to be O(n^2), where `n` is the number of characters in `data`.

Algorithm `huffman_decoding` takes `data` and `tree` as arguments, traverses the `tree`, constructs the code following the path to every leaf, get corresponding leaf character (from `leaves_dict`) and returns the decoded `chars`.
Time complexity is O(n).