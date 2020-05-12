#  Remove Nth Node From End of List

# Given a linked list, remove the n-th node from the end of list and return its head.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head:
            slow = head
            while n >= 0:
                slow = slow.next
                n -= 1
                if not slow and n >= 0:
                    return head.next
            cu = head
            while slow:
                slow = slow.next
                cu = cu.next
            ne = cu.next
            if ne:
                cu.next = ne.next
            else:
                cu.next = None
        return head


if __name__ == '__main__':
    s = Solution()
    head = ListNode(1)
    head1 = ListNode(2)
    head.next = head1
    print(s.removeNthFromEnd(head, 2).val)
