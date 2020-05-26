Inserting in Trie takes O(n), where `n` is the number of characters in word.

Find takes also O(n); iterates through word characters and with every iteration moves the node pointer to it's children.

The `suffixes` method of TrieNode iterates through every key (character) of it's children dictionary and recursively call itself on every children node.
Time complexity is O(n * m), where `n` in the number of children of the node upon the method is called, and `m` is the average number of children of every child.

Time complexity:
- Trie.insert: O(n)
- Trie.find: O(n)
- TrieNode.suffixes: O(n * m)

Space complexity:
- Trie.insert: O(n)
- TrieNode.suffixes: O(n * m), space of recursive call stack; O(n + m), space of all_suffixes array returned.

