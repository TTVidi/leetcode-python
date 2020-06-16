# Path Sum

# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values
# along the path equals the given sum.
#
# Note: A leaf is a node with no children.
#

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root:
            rest = sum - root.val
            if not root.left and not root.right:
                return rest == 0
            return self.hasPathSum(root.left, rest) or self.hasPathSum(root.right, rest)
        return False
