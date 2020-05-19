# Remove Duplicates from Sorted List

# Given a sorted linked list, delete all duplicates such that each element appear only once.
#


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head:
            pre = head
            current = pre.next
            while current:
                if pre.val == current.val:
                    current = current.next
                else:
                    pre.next = current
                    pre = current
                    current = current.next
            if pre.next:
                if pre.next != current:
                    pre.next = None
        return head


if __name__ == '__main__':
    s = Solution()
