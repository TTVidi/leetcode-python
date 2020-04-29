# Binary Tree Maximum Path Sum

# Given a non-empty binary tree, find the maximum path sum.
#
# For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along
# the parent-child connections. The path must contain at least one node and does not need to go through the root.
#
import sys


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    count = -sys.maxsize - 1

    def maxPathSum(self, root: TreeNode) -> int:
        def maxSum(root: TreeNode) -> int:
            if not root:
                return 0
            left = maxSum(root.left)
            right = maxSum(root.right)
            if left < 0:
                left = 0
            if right < 0:
                right = 0
            self.count = max(self.count, left + right + root.val)
            return max(left, right) + root.val

        maxSum(root)
        return self.count


if __name__ == '__main__':
    s = Solution()
    t7 = TreeNode(7)
    t9 = TreeNode(9)
    t10 = TreeNode(10)
    t15 = TreeNode(15)
    t20 = TreeNode(20)
    t10.left = t9
    t10.right = t20
    t20.left = t15
    t20.right = t7
    print(s.maxPathSum(t10))
