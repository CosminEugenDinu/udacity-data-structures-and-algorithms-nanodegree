#! /usr/bin/env python3.8

# %%
import sys
from doubly_liked_list import DoublyLinkedList
from tree import Tree

# %%
def frequencies(string):
    size = len(string)
    chars_frqs = {}
    for c in string:
        chars_table = chars_frqs.get(c)
        if chars_table:
            chars_frqs[c] += 1
        else:
            chars_frqs[c] = 1

    # def get_frequency(character):
    #     return chars_frqs[character]

    return chars_frqs

s = "abracadabbra"
# chars_frqs = frequencies(s)
# print(chars_frqs)

# %%


def huffman_encoding(data):
    # frequencies of characters table as list of tuples
    chars_frqs = frequencies(data).items()
    print(chars_frqs)
    dl_list = DoublyLinkedList()
    # keys are characters from chars_frqs table and values are leaves tree_nodes with frequencies
    leaves_refs = {}
    # insert tree_nodes(char_frq) in doubly linked list from lowest to highest frequency
    # for char in chars_frqs:
    #     frq = chars_frqs[char]
    #     leaf = Tree.Node(frq)
    #     leaves_refs[frq]
    # T = Tree(leaves[0].value + leaves[1].value)
    # T.root.left = leaves[0]
    # T.root.right = leaves[1]
    # for i in range(2, len(leaves)):



    return 'ret from huffman_encoding(data)' 

huffman_encoding(s)



# %%
def huffman_decoding(data,tree):

    return "decoded_data"

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
