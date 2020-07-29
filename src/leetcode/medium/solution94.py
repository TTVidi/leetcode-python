# Binary Tree Inorder Traversal

# Given a binary tree, return the inorder traversal of its nodes' values.
#
# Example:
#
# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# Output: [1,3,2]
# Follow up: Recursive solution is trivial, could you do it iteratively?

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        def inorder(node: TreeNode):
            if node:
                inorder(node.left)
                res.append(node.val)
                inorder(node.right)

        inorder(root)
        return res

    def inorderTraversal2(self, root: TreeNode) -> List[int]:
        # inorder is left, root, right
        # runs in O(N) space and time, space for the height of the tree on the stack
        stack = []
        res = []

        while True:
            # keep going left until we cant
            if root:
                stack.append(root)
                root = root.left

            # done going left, still nodes on stack, do root, go right
            if not root and stack:
                root = stack.pop()
                res.append(root.val)
                root = root.right

            # if empty return
            if not root and not stack:
                return res
