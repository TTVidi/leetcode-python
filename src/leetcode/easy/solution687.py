# Longest Univalue Path

# Given a binary tree, find the length of the longest path where each node in the path has the same value. This path
# may or may not pass through the root.
#
# The length of path between two nodes is represented by the number of edges between them.
#
#
#
# Example 1:
#
# Input:
#
#               5
#              / \
#             4   5
#            / \   \
#           1   1   5
# Output: 2
#
#
#
# Example 2:
#
# Input:
#
#               1
#              / \
#             4   5
#            / \   \
#           4   4   5
# Output: 2
#
#
#
# Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        res = [0]

        def helper(node: TreeNode) -> int:
            if node:
                l = 0
                r = 0
                if node.left:
                    l = helper(node.left)
                    if node.val == node.left.val:
                        l += 1
                    else:
                        l = 0
                if node.right:
                    r = helper(node.right)
                    if node.val == node.right.val:
                        r += 1
                    else:
                        r = 0
                res.append(l + r)
                return max(l, r)

            return 0

        helper(root)
        return max(res)
