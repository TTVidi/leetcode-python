# Validate Binary Search Tree
# Given a binary tree, determine if it is a valid binary search tree (BST).
#
# Assume a BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST1(self, root: TreeNode) -> bool:
        def inOrderTraversal(root):
            if not root:
                return 0
            inOrderTraversal(root.left)
            stack.append(root.val)
            inOrderTraversal(root.right)

        stack = []
        inOrderTraversal(root)
        return stack == sorted(stack) and stack == sorted(list(set(stack)))

    def isValidBST(self, root: TreeNode) -> bool:
        def valid(node: TreeNode, isLeft: bool) -> (int, bool):
            if node:
                left = (None, True)
                right = (None, True)
                if node.left:
                    if node.left.val >= node.val:
                        return None, False
                    left = valid(node.left, True)
                if node.right:
                    if node.right.val <= node.val:
                        return None, False
                    right = valid(node.right, False)
                if left[1] and right[1]:
                    if left[0] and right[0]:
                        if left[0] < node.val < right[0]:
                            if isLeft:
                                return right[0], True
                            else:
                                return left[0], True
                        return None, False
                    if left[0]:
                        if node.val > left[0]:
                            return node.val, True
                        return None, False
                    if right[0]:
                        if node.val < right[0]:
                            return node.val, True
                        return None, False
                    return node.val, True
                else:
                    return None, False
            return None, True

        if root:
            leftv = valid(root.left, True)
            rightv = valid(root.right, False)
            if leftv[1] and rightv[1]:
                if leftv[0] is not None and rightv[0] is not None:
                    return leftv[0] < root.val < rightv[0]
                elif leftv[0] is not None:
                    return leftv[0] < root.val
                elif rightv[0] is not None:
                    return root.val < rightv[0]
                else:
                    return True
            else:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t3.left = t2
    t2.left = t1
    print(s.isValidBST(t3))
