# Binary Tree Level Order Traversal

# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
# Accepted.


# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        rs = []
        queue = []
        helper = []
        queue.append(root)
        tp = []
        while queue:
            node = queue.pop(0)
            if node:
                tp.append(node.val)
                if node.left:
                    helper.append(node.left)
                if node.right:
                    helper.append(node.right)
            if not queue:
                queue = helper
                helper = []
                if tp:
                    rs.append(tp)
                tp = []
        return rs
