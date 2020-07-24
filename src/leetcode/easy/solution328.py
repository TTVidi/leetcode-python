# Odd Even Linked List

# Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are
# talking about the node number and not the value in the nodes.
#
# You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.
#
# Example 1:
#
# Input: 1->2->3->4->5->NULL
# Output: 1->3->5->2->4->NULL
# Example 2:
#
# Input: 2->1->3->5->6->4->7->NULL
# Output: 2->3->6->7->1->5->4->NULL
#
#
# Constraints:
#
# The relative order inside both the even and odd groups should remain as it was in the input.
# The first node is considered odd, the second node even and so on ...
# The length of the linked list is between [0, 10^4].


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head:
            o_head = None
            e_head = None
            odd = None
            even = None
            idx = 1
            while head:
                if idx % 2 == 1:
                    if o_head == None:
                        o_head = head
                        odd = head
                    else:
                        odd.next = head
                        odd = head
                else:
                    if e_head == None:
                        e_head = head
                        even = head
                    else:
                        even.next = head
                        even = head
                idx += 1
                head = head.next
            odd.next = e_head
            if even:
                even.next = None
            return o_head

