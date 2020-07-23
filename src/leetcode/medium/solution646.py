# Maximum Length of Pair Chain

# You are given n pairs of numbers. In every pair, the first number is always smaller than the second number.
#
# Now, we define a pair (c, d) can follow another pair (a, b) if and only if b < c. Chain of pairs can be formed in
# this fashion.
#
# Given a set of pairs, find the length longest chain which can be formed. You needn't use up all the given pairs.
# You can select pairs in any order.
#
# Example 1:
# Input: [[1,2], [2,3], [3,4]]
# Output: 2
# Explanation: The longest chain is [1,2] -> [3,4]
# Note:
# The number of given pairs will be in the range [1, 1000].
from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda f: f[0])
        dp = []
        for pair in pairs:
            if not dp:
                dp.append(pair)
            else:
                last = dp.pop()
                if pair[0] > last[1]:
                    dp.append(last)
                    dp.append(pair)
                else:
                    if last[1] > pair[1]:
                        if pair[0] >= last[0]:
                            last = pair
                    dp.append(last)
        return len(dp)


if __name__ == '__main__':
    s = Solution()
    print(s.findLongestChain([[1, 2], [3, 4], [5, 20], [6, 7], [8, 9], [10, 30], [11, 19], [20, 21]]))
