#! /usr/bin/env python3.8

from collections import deque

def Q():
    q = deque()
    def enqueue(val):
        nonlocal q
        q.appendleft(val)
        return True
    def dequeue():
        nonlocal q
        if len(q):
            return q.pop()
    def q_empty():
        nonlocal q
        return len(q) == 0
    return enqueue, dequeue, q_empty


class Tree:

    class Node:
        def __init__(self, value=None):
            self.value = value
            self.left = None
            self.right = None

        def __add__(self, other):
            return Tree.Node(self.value + other.value)
 
        def __lt__(self, other):
            return True if self.value < other.value else False
        def __le__(self, other):
            return True if self.value <= other.value else False

        def __repr__(self):
            return f'({self.left}<-{self.value}->{self.right})' 
        def __str__(self):
            return f'{self.value}'

    def __init__(self, root_node):
        self.root = root_node
        # maps leaf_node_ref with an associated value
        self.leaves_dict = {}

    def __repr__(self):
        enqueue, dequeue, q_empty = Q()
        levels = []

        node = self.root
        level = 0
        node and enqueue((node, level))

        while not q_empty(): 
            node, level = dequeue()

            # append a new level list if does not exits
            (0 <= level < len(levels)) or levels.append([])

            levels[level].append(node)

            # add left or right to queue if exists
            node.left and enqueue((node.left, level + 1))
            node.right and enqueue((node.right, level + 1))

        for_print = ''
        for level in levels:
            for n in level:
                left = n.left and n.left.value
                right = n.right and n.right.value
                for_print += f'({left}<-{n.value}->{right})'
            for_print += '\n'
        return for_print

    def __str__(self):
        return f'T({self.root.value})' 

# t = Tree('A')
# t.root.left = t.Node('B')
# t.root.right = t.Node('C')
# t.root.left.left = t.Node('D')
# t.root.left.right = t.Node('E')
# t.root.right.left = t.Node('F')

# print(t)









    
