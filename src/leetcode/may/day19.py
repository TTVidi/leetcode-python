# Kth Smallest Element in a BST

# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        li = []

        def iterate(node: TreeNode):
            if node:
                iterate(node.left)
                li.append(node.val)
                if len(li) < k:
                    iterate(node.right)

        iterate(root)
        return li[k - 1]


if __name__ == '__main__':
    s = Solution()
    print(s.kthSmallest())
