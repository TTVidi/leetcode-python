# Longest ZigZag Path in a Binary Tree

# Given a binary tree root, a ZigZag path for a binary tree is defined as follow:
#
# Choose any node in the binary tree and a direction (right or left).
# If the current direction is right then move to the right child of the current node otherwise move to the left child.
# Change the direction from right to left or right to left.
# Repeat the second and third step until you can't move in the tree.
# Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).
#
# Return the longest ZigZag path contained in that tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        def zigzag(node: TreeNode, isLeft: bool, length: int) -> int:
            if node:
                left = 0
                right = 0
                if node.left:
                    if isLeft:
                        left = zigzag(node.left, True, 1)
                    else:
                        left = zigzag(node.left, True, length + 1)
                if node.right:
                    if isLeft:
                        right = zigzag(node.right, False, length + 1)
                    else:
                        right = zigzag(node.right, False, 1)
                return max(left, right, length)
            return length

        if root:
            left = 0
            right = 0
            if root.left:
                left = zigzag(root.left, True, 1)
            if root.right:
                right = zigzag(root.right, False, 1)
            return max(left, right)
        return 0


if __name__ == '__main__':
    s = Solution()
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    print(s.longestZigZag(t1))
