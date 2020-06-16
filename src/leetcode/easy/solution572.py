#  Subtree of Another Tree

# Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with
# a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s
# could also be considered as a subtree of itself.
#
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree1(self, s: TreeNode, t: TreeNode) -> bool:
        def inner_order(node: TreeNode, p: str) -> str:
            if node:
                if node.left:
                    p = inner_order(node.left, p)
                p += str(node.val)
                if node.right:
                    p = inner_order(node.right, p)
                return p

        def pre_order(node: TreeNode, p: str) -> str:
            if node:
                p += str(node.val)
                if node.left:
                    p = pre_order(node.left, p)
                if node.right:
                    p = pre_order(node.right, p)
                return p

        def tail_order(node: TreeNode, p: str) -> str:
            if node:
                if node.left:
                    p = tail_order(node.left, p)
                if node.right:
                    p = tail_order(node.right, p)
                p += str(node.val)
                return p

        s1 = ""
        s2 = ""
        s1 = inner_order(s, s1)
        s2 = inner_order(t, s2)
        if s1.__contains__(s2):
            s1 = ""
            s2 = ""
            s1 = pre_order(s, s1)
            s2 = pre_order(t, s2)
            if s1.__contains__(s2):
                s1 = ""
                s2 = ""
                s1 = tail_order(s, s1)
                s2 = tail_order(t, s2)
                return s1.__contains__(s2)

        return False

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if self.isSame(s, t):
            return True
        if s:
            left = self.isSubtree(s.left, t)
            if left:
                return True
            right = self.isSubtree(s.right, t)
            return right
        return False

    def isSame(self, s: TreeNode, t: TreeNode) -> bool:
        if s and t:
            if s.val == t.val:
                return self.isSame(s.left, t.left) and self.isSame(s.right, t.right)
            return False
        if s and not t:
            return False
        if not s and t:
            return False
        if not s and not t:
            return True


def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


if __name__ == '__main__':
    l1 = "[3,4,5,1,2,null,null,0]"
    l2 = "[4,1,2]"
    s = stringToTreeNode(l1)
    t = stringToTreeNode(l2)
    so = Solution()
    print(so.isSubtree(s, t))
