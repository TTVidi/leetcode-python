# Construct Binary Search Tree from Preorder Traversal

# Return the root node of a binary search tree that matches the given preorder traversal.
#
# (Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value <
# node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays
# the value of the node first, then traverses node.left, then traverses node.right.)
#
# It's guaranteed that for the given test cases there is always possible to find a binary search tree with the given
# requirements.
#


# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0])

        def construct_bst(node: TreeNode, val: int):
            if val > node.val:
                if node.right:
                    construct_bst(node.right, val)
                else:
                    node.right = TreeNode(val)
            elif val < node.val:
                if node.left:
                    construct_bst(node.left, val)
                else:
                    node.left = TreeNode(val)

        for i in range(1, len(preorder)):
            construct_bst(root, preorder[i])
        return root


if __name__ == '__main__':
    s = Solution()
    t = s.bstFromPreorder([8, 5, 1, 7, 10, 12])
    print(t)
