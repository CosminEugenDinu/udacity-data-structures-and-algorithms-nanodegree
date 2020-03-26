#! /usr/bin/env python3.8

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

        return node.next

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size
    
    def get_array(self):
        arr = []
        node = self.head
        while node:
            arr.append(node.value)
            node = node.next
        return arr

def union(llist_1, llist_2):
    union_llist = LinkedList()
    union_set_dict = {}
    
    node_1 = llist_1.head
    node_2 = llist_2.head

    while node_1 or node_2:
        if node_1:
            if not union_set_dict.get(node_1.value):
                union_set_dict[node_1.value] = node_1.value
                union_llist.append(node_1.value)
            node_1 = node_1.next
        if node_2:
            if not union_set_dict.get(node_2.value):
                union_set_dict[node_2.value] = node_2.value
                union_llist.append(node_2.value)
            node_2 = node_2.next

    return union_llist


def intersection(llist_1, llist_2):
    intersection_llist = LinkedList()
    intersection_set_dict = {}

    node_1 = llist_1.head
    while node_1:
        if not intersection_set_dict.get(node_1.value):
            intersection_set_dict[node_1.value] = node_1.value
        node_1 = node_1.next
    
    node_2 = llist_2.head
    while node_2:
        is_common_value = intersection_set_dict.get(node_2.value)
        if is_common_value:
            intersection_llist.append(is_common_value)
            del intersection_set_dict[is_common_value]
        node_2 = node_2.next

    return intersection_llist


# Test

def test_union(element_1, element_2):
    llist_1 = LinkedList()
    llist_2 = LinkedList()

    for i in element_1:
        llist_1.append(i)
    for i in element_2:
        llist_2.append(i)
    
    py_union_set = set(element_1).union(set(element_2))

    sorted_reference_union_array = sorted(list(py_union_set))
    sorted_test_union_array = sorted(union(llist_1, llist_2).get_array())

    # print(sorted(element_1))
    # print(sorted(element_2))
    # print(sorted_reference_union_array)
    # print(sorted_test_union_array)

    passed = sorted_reference_union_array == sorted_test_union_array
    
    if passed:
        print('union passed\n')
    else:
        print('union failed\n')

def test_intersection(element_1, element_2):
    llist_1 = LinkedList()
    llist_2 = LinkedList()

    for i in element_1:
        llist_1.append(i)
    for i in element_2:
        llist_2.append(i)
    
    py_intersection_set = set(element_1).intersection(set(element_2))

    sorted_reference_intersection_array = sorted(list(py_intersection_set))
    sorted_test_intersection_array = sorted(intersection(llist_1, llist_2).get_array())
    
    # print(sorted(element_1))
    # print(sorted(element_2))
    # print(sorted_reference_intersection_array)
    # print(sorted_test_intersection_array)

    passed = sorted_reference_intersection_array == sorted_test_intersection_array
    
    if passed:
        print('intersection passed\n')
    else:
        print('intersection failed\n')

    

# Test case 1

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

test_union(element_1, element_2)
test_intersection(element_1, element_2)


# Test case 2

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

test_union(element_1, element_2)
test_intersection(element_1, element_2)