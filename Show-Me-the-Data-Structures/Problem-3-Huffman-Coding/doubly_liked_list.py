#! /usr/bin/env python3.8

class DoublyLinkedList:

    class Node:
        def __init__(self, value, prev, next):
            self.value = value
            self.prev = prev
            self.next = next
        
    def __init__(self):
        self.size = 0
        self.header = self.Node(None, None, None)
        self.trailer = self.Node(None, None, None)
        self.header.next = self.trailer
        self.trailer.prev = self.header
    
    def __len__(self):
        return self.size
    
    def __repr__(self):
        for_print = ''
        node = self.header
        while node is not None:
            prev = node.prev and node.prev.value
            next = node.next and node.next.value
            value = node.value
            if node.prev is self.header:
                prev = 'HEADER'
            if node.next is self.trailer:
                next = 'TRAILER'
            for_print += f' ({prev}<-{value}->{next}) '
            node = node.next
        return for_print


    def is_empty(self):
        return self.size == 0
    
    def insert(self, value, predecessor, successor):
        if predecessor is self.trailer:
            raise "Predecessor cannot be self.trailer"
        if successor is self.header:
            raise "Successor cannot be self.header"
        newest = self.Node(value, predecessor, successor)
        predecessor.next = newest
        successor.prev = newest
        self.size += 1
        return newest
    
    def delete(self, node):
        predecessor = node.prev
        successor = node.next
        predecessor.next = successor
        successor.prev = predecessor
        self.size -= 1
        value = node.value
        node.prev = node.next = node.value = None
        return value

# dl = DoublyLinkedList()
# a = dl.insert('A', dl.header, dl.trailer)
# b = dl.insert('B', dl.header, a)
# c = dl.insert('C', a, dl.trailer)
# print(dl)

    

