# Convert Sorted List to Binary Search Tree

# Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
#
# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees
# of every node never differ by more than 1.
#
#
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if head:
            li = []
            while head:
                li.append(head.val)
                head = head.next

            def build_tree(node: TreeNode, left: int, right: int):
                if 0 <= left <= right < len(li):
                    middle = (left + right) >> 1
                    c = TreeNode(li[middle])
                    if c.val > node.val:
                        node.right = c
                    else:
                        node.left = c
                    if left != right:
                        build_tree(c, left, middle - 1)
                        build_tree(c, middle + 1, right)

            l = 0
            r = len(li) - 1
            mi = r >> 1
            root = TreeNode(li[mi])
            build_tree(root, l, mi - 1)
            build_tree(root, mi + 1, r)
            return root

    def sortedListToBST2(self) -> TreeNode:
        li = [-10, -3, 0, 5, 9]

        def build_tree(node: TreeNode, left: int, right: int):
            if 0 <= left <= right < len(li):
                middle = (left + right) >> 1
                c = TreeNode(li[middle])
                if c.val > node.val:
                    node.right = c
                else:
                    node.left = c
                if left != right:
                    build_tree(c, left, middle - 1)
                    build_tree(c, middle + 1, right)

        l = 0
        r = len(li) - 1
        mi = r >> 1
        root = TreeNode(li[mi])
        build_tree(root, l, mi - 1)
        build_tree(root, mi + 1, r)
        return root


if __name__ == '__main__':
    s = Solution()
    head = ListNode(-10)
    head1 = ListNode(-3)
    head2 = ListNode(0)
    head3 = ListNode(5)
    head4 = ListNode(9)
    head.next = head1
    head1.next = head2
    head2.next = head3
    head3.next = head4
    r = s.sortedListToBST(head)
    print(1)
