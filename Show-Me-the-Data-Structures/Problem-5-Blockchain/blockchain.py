#! /usr/bin/env python3.8

import hashlib
import json
from datetime import datetime

class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
      
    def calc_hash(self):
        sha = hashlib.sha256()

        hash_str = json.dumps({
            "data": f"{self.data}",
            "previous_hash": f"{self.previous_hash}",
            "timestamp": f"{self.timestamp}"
        }, sort_keys=True).encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()


class Blockchain:

    class Node:
        def __init__(self, block):
            self.next = None
            self.block = block

    def __init__(self):
        initial_block = Block(datetime.now(), "initial block data", "0")
        self.head = self.Node(initial_block)
        self.tail = self.head

    def add_block(self, data):
        previous_hash = self.tail.block.hash
        block = Block(datetime.now(), data, previous_hash)
        self.tail.next = self.Node(block)
        self.tail = self.tail.next

    def __str__(self):
        node = self.head
        attr_to_print = 'data'
        for_print = ''
        while node:
            for_print +=f'[{node.block.__getattribute__(attr_to_print)}]--'
            node = node.next
        return for_print


BC = Blockchain()
BC.add_block('block_1 data')
BC.add_block('block_2 data')
BC.add_block('block_3 last added')
print(BC)

        

