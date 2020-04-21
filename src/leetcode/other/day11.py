# Diameter of Binary Tree Given a binary tree, you need to compute the length of the diameter of the tree. The
# diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may
# not pass through the root.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    max_sum = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.treeDepth(root)
        return self.max_sum

    def treeDepth(self, root: TreeNode) -> int:
        left = 0
        if root.left is not None:
            left = self.treeDepth(root.left)

        right = 0
        if root.right is not None:
            right = self.treeDepth(root.right)

        self.max_sum = max(self.max_sum, left + right)
        return 1 + max(left, right)

    def deserialize(self, string) -> TreeNode:
        if string == '{}':
            return None
        nodes = [None if val == 'null' else TreeNode(int(val))
                 for val in string.strip('[]{}').split(',')]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids: node.left = kids.pop()
                if kids: node.right = kids.pop()
        return root

    def drawtree(self, root):
        def height(root):
            return 1 + max(height(root.left), height(root.right)) if root else -1

        def jumpto(x, y):
            t.penup()
            t.goto(x, y)
            t.pendown()

        def draw(node, x, y, dx):
            if node:
                t.goto(x, y)
                jumpto(x, y - 20)
                t.write(node.val, align='center', font=('Arial', 12, 'normal'))
                draw(node.left, x - dx, y - 60, dx / 2)
                jumpto(x, y - 20)
                draw(node.right, x + dx, y - 60, dx / 2)

        import turtle
        t = turtle.Turtle()
        t.speed(0);
        turtle.delay(0)
        h = height(root)
        jumpto(0, 30 * h)
        draw(root, 0, 30 * h, 40 * h)
        t.hideturtle()
        turtle.mainloop()


if __name__ == '__main__':
    s = Solution()
    root = s.deserialize('[4, -7, -3,null,null, -9, -3, 9, -4,null, 6,null, -6, -6,null,null, 0, 6]')
    print(s.diameterOfBinaryTree(root))
    print(s.drawtree(s.deserialize('[8,5,10,null,null,12,null,1,null,null,7]')))
