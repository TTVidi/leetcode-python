# Binary Tree Paths

# Given a binary tree, return all root-to-leaf paths.
#
# Note: A leaf is a node with no children.


# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root:
            if root.left and root.right:
                left = self.binaryTreePaths(root.left)
                right = self.binaryTreePaths(root.right)

                for i in range(len(left)):
                    left[i] = str(root.val) + "->" + left[i]

                for i in range(len(right)):
                    right[i] = str(root.val) + "->" + right[i]
                return left + right
            elif root.left:
                left = self.binaryTreePaths(root.left)
                for i in range(len(left)):
                    left[i] = str(root.val) + "->" + left[i]
                return left
            elif root.right:
                right = self.binaryTreePaths(root.right)
                for i in range(len(right)):
                    right[i] = str(root.val) + "->" + right[i]
                return right
            else:
                return [str(root.val)]
        return []


if __name__ == '__main__':
    s = Solution()
    # print(s.binaryTreePaths())
    li1 = [1, 2]
    li2 = [4, 4]
