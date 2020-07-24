# Combinations

# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
#
# Example:
#
# Input: n = 4, k = 2
# Output:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def helper(begin: int, path: List[int]):
            length = len(path)
            if length == k:
                res.append(path)
                return
            for i in range(begin + 1, n + 1):
                if k - length > n - i + 1:
                    break
                copy = path.copy()
                copy.append(i)
                helper(i, copy)

        helper(0, [])

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.combine(4, 2))
