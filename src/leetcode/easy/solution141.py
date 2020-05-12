# Linked List Cycle

# Given a linked list, determine if it has a cycle in it.
#
# To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in
# the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head:
            slow = head
            fast = head
            while fast and slow:
                slow = slow.next
                fast = fast.next
                if fast:
                    fast = fast.next
                else:
                    return False
                if fast == slow:
                    return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.hasCycle())
