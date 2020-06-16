# Minimum Depth of Binary Tree

# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
#
# Note: A leaf is a node with no children.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root:
            left = self.minDepth(root.left) + 1
            right = self.minDepth(root.right) + 1
            if root.left and root.right:
                return min(left, right)
            if root.left:
                return left
            return right
        return 0


if __name__ == '__main__':
    s = Solution()
