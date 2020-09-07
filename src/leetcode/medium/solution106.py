# Construct Binary Tree from Inorder and Postorder Traversal

# Given inorder and postorder traversal of a tree, construct the binary tree.
#
# Note:
# You may assume that duplicates do not exist in the tree.
#
# For example, given
#
# inorder = [9,3,15,20,7]
# postorder = [9,15,7,20,3]
# Return the following binary tree:
#
#     3
#    / \
#   9  20
#     /  \
#    15   7


# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if inorder:

            def findIdx(idx: int, left: int, right: int) -> int:
                v = postorder[idx]
                base = (left + right) >> 1
                if inorder[base] == v:
                    return base
                if base - 1 >= 0:
                    if inorder[base - 1] == v:
                        return base - 1

                if inorder[base + 1] == v:
                    return base + 1

            def build(left: int, right: int, pIdx: int, Iidx: int) -> TreeNode:
                if left > right:
                    return None
                if left == right:
                    return TreeNode(inorder[Iidx])
                parent = TreeNode(inorder[Iidx])
                rightRest = right - Iidx
                parent.left = build(left, Iidx - 1, pIdx - rightRest - 1, findIdx(pIdx - rightRest - 1, left, Iidx - 1))
                parent.right = build(Iidx + 1, right, pIdx - 1, findIdx(pIdx - 1, Iidx + 1, right))
                return parent

            return build(0, len(inorder) - 1, len(inorder) - 1, findIdx(len(inorder) - 1, 0, len(inorder) - 1))

        return None


if __name__ == '__main__':
    s = Solution()
    print(s.buildTree([2, 1],
                      [2, 1]))
