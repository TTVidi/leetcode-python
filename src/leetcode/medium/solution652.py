# Find Duplicate Subtrees

# Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return
# the root node of any one of them.
#
# Two trees are duplicate if they have the same structure with same node values.
#
# Example 1:
#
#         1
#        / \
#       2   3
#      /   / \
#     4   2   4
#        /
#       4
# The following are two duplicate subtrees:
#
#       2
#      /
#     4
# and
#
#     4
# Therefore, you need to return above trees' root in the form of a list.

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        his = {}

        res = []

        def search(node: TreeNode) -> str:
            if node:
                s = "("
                s += search(node.left)
                s += str(node.val)
                s += search(node.right)
                s += ")"

                if s in his:
                    if his[s] == 1:
                        res.append(node)
                    his[s] += 1
                else:
                    his[s] = 1
                return s
            return " "

        search(root)

        return res
