#! /usr/bin/env python3.8


class Node:
    def __init__(self, key, value):
        self.value = value
        self.key = key
        self.next = None
        self.prev = None
    
    def __repr__(self):
        prev = self.prev and self.prev.value
        next = self.next and self.next.value
        return f'{prev}<-{self.value}->{next}'
    
    def __str__(self):
        return f'{self.value}'

class LRU_Cache:

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.hash = {}
        self.head = None
        self.tail = None

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        node = self.hash.get(key)
        if not node:
            print(f'get({key})=>{-1}')
            return -1
        if node is self.head:
            print(f'get({key})=>{node.value}')
            return node.value
        if node is self.tail:
            self.tail = node.prev
            self.tail.next = None
            node.prev.next = None
            node.next = self.head
            node.prev = None
            self.head.prev = node
            self.head = node
            print(f'get({key})=>{node.value}')
            return node.value

        # move the requested node to head
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = self.head
        self.head.prev = node
        self.head = node
        print(f'get({key})=>{node.value}')
        return node.value


    def set(self, key, value):
        print(f'set({key}, {value})')
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if len(self.hash) == 0:
            new_node = Node(key, value)
            self.hash[key] = new_node
            self.head = new_node
            self.tail = new_node
            return

        node = self.hash.get(key)
        if node:
            node.value = value
            if node is self.head:
                return
            if node is self.tail:
                head = self.head
                head.prev = node
                node.next = head
                self.head = node
                return
            node.prev.next = node.next
            node.next.prev = node.prev
            self.head.prev = node
            node.next = self.head
            self.head = node

        else:
            new_node = Node(key, value)
            self.hash[key] = new_node
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

        if len(self.hash) > self.capacity:
            # remove the oldest node
            oldest = self.tail
            oldest.prev.next = None 
            self.tail = oldest.prev
            del self.hash[oldest.key]
    
    def __repr__(self):
        l_list = []
        node = self.head
        while node:
            l_list.append(repr(node))
            node = node.next
        return f'head-{self.head.value}-IN>>>' + repr(l_list) + f'>>>tail-{self.tail.value}-OUT'

    def __str__(self):
        l_list = []
        node = self.head
        while node:
            l_list.append(node.value)
            node = node.next
        return f'>>>{str(l_list)}>>>'





our_cache = LRU_Cache(5)

our_cache.set(1, 1)
print(our_cache)
our_cache.set(2, 2)
print(our_cache)
our_cache.set(3, 3)
print(our_cache)
our_cache.set(4, 4)
print(our_cache)
our_cache.set(5, 5)
print(our_cache)
our_cache.set(6, 6)
print(our_cache)
our_cache.set(7, 7)
print(our_cache)
our_cache.get(3)
print(our_cache)



our_cache.set(3, 3)
print(our_cache)
our_cache.get(7)
print(our_cache)
our_cache.get(6)
print(our_cache)
our_cache.get(4)
print(our_cache)
our_cache.get(6)
print(our_cache)
our_cache.get(3)
print(our_cache)
our_cache.set(10, 10)
print(our_cache)
our_cache.set(11, 11)
print(our_cache)
