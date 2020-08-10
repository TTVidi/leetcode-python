# All Elements in Two Binary Search Trees

# Given two binary search trees root1 and root2.
#
# Return a list containing all the integers from both trees sorted in ascending order.
#
#
#
# Example 1:
#
#
# Input: root1 = [2,1,4], root2 = [1,0,3]
# Output: [0,1,1,2,3,4]
# Example 2:
#
# Input: root1 = [0,-10,10], root2 = [5,1,7,0,2]
# Output: [-10,0,0,1,2,5,7,10]
# Example 3:
#
# Input: root1 = [], root2 = [5,1,7,0,2]
# Output: [0,1,2,5,7]
# Example 4:
#
# Input: root1 = [0,-10,10], root2 = []
# Output: [-10,0,10]
# Example 5:
#
#
# Input: root1 = [1,null,8], root2 = [8,1]
# Output: [1,1,8,8]
#
#
# Constraints:
#
# Each tree has at most 5000 nodes.
# Each node's value is between [-10^5, 10^5].

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def middle_order(node: TreeNode, l: List[int]):
            if node:
                middle_order(node.left, l)
                l.append(node.val)
                middle_order(node.right, l)

        res = []
        l1 = []
        l2 = []
        middle_order(root1, l1)
        middle_order(root2, l2)
        i = 0
        j = 0
        while i < len(l1) and j < len(l2):
            if l1[i] <= l2[j]:
                res.append(l1[i])
                i += 1
            else:
                res.append(l2[j])
                j += 1

        while i < len(l1):
            res.append(l1[i])
            i += 1

        while j < len(l2):
            res.append(l2[j])
            j += 1
        return res
