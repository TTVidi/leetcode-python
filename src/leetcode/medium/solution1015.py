# Sum of Nodes with Even-Valued Grandparent

# Given a binary tree, return the sum of values of nodes with even-valued grandparent.  (A grandparent of a node is
# the parent of its parent, if it exists.)
#
# If there are no nodes with an even-valued grandparent, return 0.
#
#

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        return 1


if __name__ == '__main__':
    s = Solution()
    print(s.sumEvenGrandparent())
