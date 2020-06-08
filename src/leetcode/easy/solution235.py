# Lowest Common Ancestor of a Binary Search Tree

# Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q
# as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
#
# Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]
#

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def find_parent(path: List[TreeNode], node: TreeNode, target: TreeNode) -> List[TreeNode]:
            if node:
                if node.val == target.val:
                    path.append(node)
                    return path
                path.append(node)
                if target.val > node.val:
                    right = find_parent(path, node.right, target)
                    if right:
                        return right
                else:
                    left = find_parent(path, node.left, target)
                    if left:
                        return left
                path.pop(-1)
            return None

        l1 = find_parent([], root, p)
        l2 = find_parent([], root, q)
        length = min(len(l1), len(l2))
        rs = None
        for i in range(length):
            if l1[i] == l2[i]:
                rs = l1[i]
            else:
                break
        return rs


if __name__ == '__main__':
    s = Solution()
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t1.left = t2
    t1.right = t3
    t = s.lowestCommonAncestor(t1, t1, t3)
    print(t)
