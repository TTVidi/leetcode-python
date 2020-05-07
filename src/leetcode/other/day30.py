# Check If a String Is a Valid Sequence from Root to Leaves Path in a Binary Tree

# Given a binary tree where each path going from the root to any leaf form a valid sequence, check if a given string
# is a valid sequence in such binary tree.
#
# We get the given string from the concatenation of an array of integers arr and the concatenation of all values of
# the nodes along a path results in a sequence in the given binary tree.


# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        if arr:
            if root:
                _l = len(arr)
                if _l == 1:
                    return root is not None and root.val == arr[0] and root.left is None and root.right is None
                if root.val == arr[0]:
                    rest = arr[1:]
                    left = self.isValidSequence(root.left, rest)
                    right = self.isValidSequence(root.right, rest)
                    return left or right
            return False
        else:
            return root is None


if __name__ == '__main__':
    s = Solution()
    print(s.isValidSequence())
