# Find the sum of all left leaves in a given binary tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root:
            def left_sum(node: TreeNode, isLeft: bool) -> int:
                if node:
                    left = 0
                    right = 0
                    if node.left:
                        left = left_sum(node.left, True)
                    if node.right:
                        right = left_sum(node.right, False)
                    if not node.left and not node.right:
                        if isLeft:
                            return node.val
                        return 0
                    return left + right
                return 0

            return left_sum(root.left, True) + left_sum(root.right, False)
        return 0
