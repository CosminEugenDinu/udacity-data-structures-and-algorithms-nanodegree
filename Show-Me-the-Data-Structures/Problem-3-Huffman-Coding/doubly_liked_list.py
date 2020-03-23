#! /usr/bin/env python3.8

class DoublyLinkedList:

    class Node:
        def __init__(self, element, prev, next):
            self.element = element
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
            prev = node.prev and node.prev.element
            next = node.next and node.next.element
            element = node.element
            if node.prev is self.header:
                prev = 'HEADER'
            if node.next is self.trailer:
                next = 'TRAILER'
            for_print += f' ({prev}<-{element}->{next}) '
            node = node.next
        return for_print
    
    def __str__(self):
        for_print = ''
        node = self.header.next
        while node is not self.trailer:
            prev = node.prev and node.prev.element
            next = node.next and node.next.element
            element = node.element
            if node.prev is self.header:
                prev = 'HEADER'
            if node.next is self.trailer:
                next = 'TRAILER'
            for_print += f'_({prev}<-{element}->{next})_'
            node = node.next
        return for_print


    def is_empty(self):
        return self.size == 0
    
    def insert(self, element, predecessor, successor):
        if predecessor is self.trailer:
            raise "Predecessor cannot be self.trailer"
        if successor is self.header:
            raise "Successor cannot be self.header"
        newest = self.Node(element, predecessor, successor)
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
        element = node.element
        node.prev = node.next = node.element = None
        return element

# dl = DoublyLinkedList()
# a = dl.insert('A', dl.header, dl.trailer)
# b = dl.insert('B', dl.header, a)
# c = dl.insert('C', a, dl.trailer)
# print(dl)

    

