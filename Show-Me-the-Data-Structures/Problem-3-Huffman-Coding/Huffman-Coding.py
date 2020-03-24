#! /usr/bin/env python3.8

import sys
from doubly_liked_list import DoublyLinkedList
from tree import Tree

def frequencies(string):
    size = len(string)
    chars_frqs = {}
    for c in string:
        chars_table = chars_frqs.get(c)
        if chars_table:
            chars_frqs[c] += 1
        else:
            chars_frqs[c] = 1
    return chars_frqs

def huffman_encoding(data):
    # frequencies of characters table as a sorted list of tuples
    chars_frqs = sorted(frequencies(data).items(), key=lambda t: t[1])

    # key: leaf_node_ref, value: character from data
    leaves_dict = {}

    dll = DoublyLinkedList()
    # insert tree_nodes(char_frq) in doubly linked list from lowest to highest frequency
    for char, frq in chars_frqs:
        leaf = Tree.Node(frq)
        leaves_dict[leaf] = char
        dll.insert(leaf, dll.trailer.prev, dll.trailer)
    
    def find_position(tree_node, dll):
        dll_node = dll.header.next
        while dll_node is not dll.trailer:
            if tree_node <= dll_node.element:
                return dll_node.prev, dll_node
            dll_node = dll_node.next
        return dll.trailer.prev, dll.trailer

    while len(dll) > 1:
        min_1 = dll.delete(dll.header.next)
        min_2 = dll.delete(dll.header.next)
        root_node = min_1 + min_2
        root_node.left = min_1
        root_node.right = min_2
        predecessor, successor = find_position(root_node, dll)
        dll.insert(root_node, predecessor, successor)

    tree = Tree(dll.header.next.element)
    tree.leaves_dict = leaves_dict

    def get_chars_codes(tree):

        chars_codes = {}
        t_node = tree.root

        def _traverse(t_node, code=''):

            # if current node is key in leaves_dict then it is a leaf
            char_at_leaf = tree.leaves_dict.get(t_node)
            if char_at_leaf:
                chars_codes[char_at_leaf] = code
                return 
            
            _traverse(t_node.left, code + '0')
            _traverse(t_node.right, code + '1')

        _traverse(t_node)
        return chars_codes

    chars_codes = get_chars_codes(tree)
    
    encoded_data = ''
    for char in data:
        encoded_data += chars_codes[char]

    return encoded_data, tree


def huffman_decoding(data, tree):

    def get_chars(data, tree):
        chars = ''
        t_node = tree.root

        for bit in data:
            if bit == '0':
                t_node = t_node.left
            elif bit == '1':
                t_node = t_node.right
            if t_node in tree.leaves_dict:
                chars += tree.leaves_dict[t_node]
                t_node = tree.root 
        
        return chars

    return get_chars(data, tree)


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
