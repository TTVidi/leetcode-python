# Find Largest Value in Each Tree Row

# Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).
#
#
#
#
#
# Example 1:
#
#
# Input: root = [1,3,2,5,3,null,9]
# Output: [1,3,9]
# Example 2:
#
# Input: root = [1,2,3]
# Output: [1,3]
# Example 3:
#
# Input: root = [1]
# Output: [1]
# Example 4:
#
# Input: root = [1,null,2]
# Output: [1,2]
# Example 5:
#
# Input: root = []
# Output: []
#
#
# Constraints:
#
# The number of nodes in the tree will be in the range [0, 104].
# -231 <= Node.val <= 231 - 1

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if root:
            l1 = []
            l2 = []
            res = []

            l1.append(root)
            while l1:
                mx = l1[0].val
                for v in l1:
                    if v.left:
                        l2.append(v.left)
                    if v.right:
                        l2.append(v.right)
                    mx = max(mx, v.val)

                l1 = l2
                l2 = []
                res.append(mx)
            return res

        return []
