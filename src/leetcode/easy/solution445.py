# Add Two Numbers II

# You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes
# first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Follow up:
# What if you cannot modify the input lists? In other words, reversing the lists is not allowed.
#
# Example:
#
# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def convert(node: ListNode) -> str:
            res = ""
            head = node
            while head:
                res += str(head.val)
                head = head.next
            return res

        n2 = int(convert(l2))
        n1 = int(convert(l1))
        r = str(n1 + n2)
        h = None
        length = len(r)
        for i in range(length):
            node = ListNode(val=int(r[length - 1 - i]))
            if not h:
                h = node
            else:
                node.next = h
                h = node

        return h
