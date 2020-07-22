# Copy List with Random Pointer

# A linked list is given such that each node contains an additional random pointer which could point to any node in
# the list or null.
#
# Return a deep copy of the list.
#
# The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [
# val, random_index] where:
#
# val: an integer representing Node.val random_index: the index of the node (range from 0 to n-1) where random
# pointer points to, or null if it does not point to any node.
#
#
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Node) -> Node:
        node = head
        while node:
            copy = Node(node.val, node.next, node.random)
            node.next = copy
            node = copy.next
        node = head
        idx = 0
        res = None
        res_node = None
        while node:
            idx += 1
            if idx % 2 == 0:
                r = node.random
                if r:
                    node.random = r.next
                if res is None:
                    res = node
                    res_node = node
                else:
                    res_node.next = node
                    res_node = node
            node = node.next
        return res
