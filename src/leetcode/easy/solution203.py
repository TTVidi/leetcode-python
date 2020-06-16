# Remove Linked List Elements

# Remove all elements from a linked list of integers that have value val.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head:
            c = head
            while c and c.val == val:
                c = c.next
            head = c
            if head:
                ne = c.next
                while ne:
                    if ne.val == val:
                        c.next = ne.next
                    else:
                        c = ne
                    ne = ne.next
        return head
