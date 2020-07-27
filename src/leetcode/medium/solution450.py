# Delete Node in a BST

# Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node
# reference (possibly updated) of the BST.
#
# Basically, the deletion can be divided into two stages:
#
# Search for a node to remove.
# If the node is found, delete the node.
# Note: Time complexity should be O(height of tree).
#
# Example:
#
# root = [5,3,6,2,4,null,7]
# key = 3
#
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7
#
# Given key to delete is 3. So we find the node with value 3 and delete it.
#
# One valid answer is [5,4,6,2,null,null,7], shown in the following BST.
#
#     5
#    / \
#   4   6
#  /     \
# 2       7
#
# Another valid answer is [5,2,6,null,4,null,7].
#
#     5
#    / \
#   2   6
#    \   \
#     4   7

# Definition for a binary tree node.
import sys


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        # def delete1(node: TreeNode, parent: TreeNode, isLeft: bool):

        # Get in order successor node
        def getMin(root):
            if not root:
                return sys.maxsize
            if not root.left and not root.right:
                return root.val
            else:
                return min(root.val, getMin(root.left), getMin(root.right))

        # Base case
        if not root:
            return None

        # Found node to delete
        elif root.val == key:
            # Leaf node
            if not root.left and not root.right:
                return None

            # Has 2 children
            elif root.left and root.right:
                n = getMin(root.right)
                root.right = self.deleteNode(root.right, n)
                root.val = n
                return root

            # Has 1 child
            else:
                return root.left if root.left else root.right


        # Recursive Step
        else:
            if root.left and key < root.val:
                root.left = self.deleteNode(root.left, key)
            elif root.right and key > root.val:
                root.right = self.deleteNode(root.right, key)

        return root



        # def delete(node: TreeNode, parent: TreeNode, isLeft: bool):
        #     if node:
        #         if node.val == key:
        #             # leaf node   delete the node
        #             if not node.left and not node.right:
        #                 if isLeft:
        #                     parent.left = None
        #                 else:
        #                     parent.right = None
        #             elif node.left and node.right:
        #                 print(1)
        #             else:
        #                 if node.left:
        #                     if isLeft:
        #                         parent.left = node.left
        #                     else:
        #                         parent.right = node.left
        #                 else:
        #                     if isLeft:
        #                         parent.left = node.right
        #                     else:
        #                         parent.right = node.right
        #         elif node.val < key:
        #             delete(node.right, node, False)
        #         else:
        #             delete(node.left, node, True)
        #
        # delete(root, None, True)
        # delete(root, None, False)
        # return root
