# Balanced Binary Tree

# Given a binary tree, determine if it is height-balanced.
#
# For this problem, a height-balanced binary tree is defined as:
#
# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
#
#

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def find_depth(node: TreeNode, depth: int) -> int:
            if node:
                left = find_depth(node.left, depth + 1)
                right = find_depth(node.right, depth + 1)
                return max(left, right)
            return depth

        def isB(node: TreeNode) -> bool:
            if node:
                if isB(node.left) and isB(node.right):
                    l = find_depth(node.left, 0)
                    r = find_depth(node.right, 0)
                    return abs(l - r) <= 1
                return False
            return True

        if root:
            return isB(root)
        return True
