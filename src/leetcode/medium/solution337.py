# House Robber III

# The thief has found himself a new place for his thievery again. There is only one entrance to this area,
# called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief
# realized that "all houses in this place forms a binary tree". It will automatically contact the police if two
# directly-linked houses were broken into on the same night.
#
# Determine the maximum amount of money the thief can rob tonight without alerting the police.
#

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: TreeNode) -> int:
        return 1


if __name__ == '__main__':
    s = Solution()
    print(s.rob())
