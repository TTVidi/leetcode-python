# Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value
# sequence.
#
#
#
# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
#
# Two binary trees are considered leaf-similar if their leaf value sequence is the same.
#
# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
#
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def find_leaf(node: TreeNode, seq: List[int]):
            if node.left:
                find_leaf(node.left, seq)
            if node.right:
                find_leaf(node.right, seq)
            if not node.left and not node.right:
                seq.append(node.val)

        l1 = []
        l2 = []
        find_leaf(root1, l1)
        find_leaf(root2, l2)
        print(l1, l2)
        return True


if __name__ == '__main__':
    li1 = [6, 7, 4, 9, 8]
    li2 = [6, 7, 4, 9, 8]
    print(li1 == li2)
    print(li1 is li2)
