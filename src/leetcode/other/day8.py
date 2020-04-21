# Middle of the Linked List
# Given a non-empty, singly linked list with head node head, return a middle node of linked list.
#
# If there are two middle nodes, return the second middle node.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        current = head
        current_index = 0
        size = 0
        while head is not None:
            head = head.next
            size += 1
            if current_index != (size // 2):
                current = current.next
                current_index += 1
        return current


if __name__ == '__main__':
    s = Solution()
    head1 = ListNode(1)
    head2 = ListNode(2)
    head3 = ListNode(3)
    head4 = ListNode(4)
    head5 = ListNode(5)
    head6 = ListNode(6)

    head5.next = head6
    head4.next = head5
    head3.next = head4
    head2.next = head3
    head1.next = head2

    result = s.middleNode(head1)
    while result is not None:
        print(result.val)
        result = result.next
