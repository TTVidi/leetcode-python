# Path Sum III

# You are given a binary tree in which each node contains an integer value.
#
# Find the number of paths that sum to a given value.
#
# The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent
# nodes to child nodes).
#
# The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.
#

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root, sum):
        if root:
            return self.dfs(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
        return 0

    def dfs(self, root, sum):
        res = 0
        if not root: return res
        sum -= root.val
        if sum == 0:
            res += 1
        res += self.dfs(root.left, sum)
        res += self.dfs(root.right, sum)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.pathSum())
