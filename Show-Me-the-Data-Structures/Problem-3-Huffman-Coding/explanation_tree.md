The `Tree` class has inner class `Node`.
`Tree.Node` defines methods `__add__`, `__lt__`, `__le__` such that node instances cat be directly sorted and added with operators `+ < <=`.

Class `Tree` creates `leaves_dict` property on instances, a dict for storing references of leaves nodes and map them to corresponding keys (such as characters from `data` in `huffman_encoding`).

