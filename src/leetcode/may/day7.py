# Cousins in Binary Tree

# In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.
#
# Two nodes of a binary tree are cousins if they have the same depth, but have different parents.
#
# We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.
#
# Return true if and only if the nodes corresponding to the values x and y are cousins.
#
#

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:

        def find(node: TreeNode, v: int, d: int) -> [int]:
            left = []
            right = []
            if node.left:
                if node.left.val == v:
                    return [node.val, d + 1]
                else:
                    left = find(node.left, v, d + 1)
            if node.right:
                if node.right.val == v:
                    return [node.val, d + 1]
                else:
                    right = find(node.right, v, d + 1)
            if left:
                return left
            if right:
                return right

        left = find(root, x, 0)
        right = find(root, y, 0)
        if left and right:
            if left[0] != right[0] and left[1] == right[1]:
                return True
        return False


if __name__ == '__main__':
    s = Solution()
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t6 = TreeNode(6)
    t7 = TreeNode(7)
    t1.right = t2
    t2.left = t3
    t3.right = t4
    t4.right = t5
    print(s.isCousins(t1, 1, 3))
