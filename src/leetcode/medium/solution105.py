#  Construct Binary Tree from Preorder and Inorder Traversal

# Given preorder and inorder traversal of a tree, construct the binary tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return None


if __name__ == '__main__':
    s = Solution()
    print(s.buildTree())
