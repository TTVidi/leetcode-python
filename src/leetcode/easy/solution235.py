# Lowest Common Ancestor of a Binary Search Tree

# Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q
# as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
#
# Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]
#

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        _set = set()

        def find_common_parent(node: TreeNode) -> TreeNode:
            if node:
                left = None
                right = None
                if node.left:
                    left = find_common_parent(node.left)
                if node.right:
                    right = find_common_parent(node.right)
                if not left and not right:
                    _set.add(node.val)
                if _set.__contains__(p.val) and _set.__contains__(q.val):
                    return node

        return find_common_parent(root)


if __name__ == '__main__':
    s = Solution()
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t1.left = t2
    t1.right = t3
    t = s.lowestCommonAncestor(t1, t1, t3)
    print(t)
