# Construct Binary Search Tree from Preorder Traversal
# Return the root node of a binary search tree that matches the given preorder traversal.
#
# (Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value <
# node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays
# the value of the node first, then traverses node.left, then traverses node.right.)
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        i = 1
        while i < len(preorder) and preorder[i] < preorder[0]:
            i += 1
        root.left = self.bstFromPreorder(preorder[1: i])
        root.right = self.bstFromPreorder(preorder[i:])
        return root


if __name__ == '__main__':
    s = Solution()
    root = s.bstFromPreorder([8, 5, 1, 7, 10, 12])
