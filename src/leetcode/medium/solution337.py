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
        d = {}

        def helper(root: TreeNode, parentUsed: bool) -> int:
            if not root: return 0
            if (root, parentUsed) in d:
                return d[(root, parentUsed)]
            res = 0
            if parentUsed:
                res = helper(root.left, False) + helper(root.right, False)
            else:
                res = max(root.val + helper(root.left, True) + helper(root.right, True),
                          helper(root.left, False) + helper(root.right, False))
            d[(root, parentUsed)] = res
            return res

        return helper(root, False)

    def rob1(self, root: TreeNode) -> int:
        _contains_dict = {}
        _not_contains_dict = {}

        def search(node: TreeNode, contains: bool) -> int:
            if node:
                if not node.left and not node.right:
                    _contains_dict[node] = node.val
                    _not_contains_dict[node] = node.val
                    return node.val
                if node in _contains_dict:
                    return _contains_dict[node]
                if node in _not_contains_dict:
                    return _not_contains_dict[node]
                if contains:
                    _contains_dict[node] = search(node.left, False) + search(node.right, False) + node.val
                    return _contains_dict[node]
                else:
                    _not_contains_dict[node] = max(search(node.left, True) + search(node.right, True),
                                                   search(node.left, False) + search(node.right, False) + node.val)
                    return _not_contains_dict[node]
            return 0

        print(search(root, False))
        print(search(root, True))
        return max(search(root, False), search(root, True))


if __name__ == '__main__':
    s = Solution()

    print(s.rob())
