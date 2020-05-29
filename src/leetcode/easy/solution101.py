# Symmetric Tree

# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        li = []
        queue = []
        queue2 = []
        queue.append(root)

        def check() -> bool:
            length = len(li)
            for i in range(length >> 1):
                if li[i] != li[length - i - 1]:
                    return False
            return True

        while queue:
            while queue:
                node = queue.pop(0)
                if node:
                    li.append(node.val)
                    queue2.append(node.left)
                    queue2.append(node.right)
                else:
                    li.append(-1)
            print(li)
            if check():
                queue = queue2
                li = []
                queue2 = []
            else:
                return False

        return True

    def isSymmetric2(self, root: TreeNode) -> bool:
        if root:
            def check(left: TreeNode, right: TreeNode) -> bool:
                if left and right:
                    if left.val == right.val:
                        if check(left.left, right.right) and check(left.right, right.left):
                            return True
                    return False
                if not left and not right:
                    return True

            return check(root.left, root.right)
        return True


if __name__ == '__main__':
    s = Solution()
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(2)
    t4 = TreeNode(3)
    t5 = TreeNode(3)
    t1.left = t2
    t1.right = t3
    t2.right = t4
    t3.right = t5

    print(s.isSymmetric(t1))
