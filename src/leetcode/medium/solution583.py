# Delete Operation for Two Strings

# Given two words word1 and word2, find the minimum number of steps required to make word1 and word2 the same,
# where in each step you can delete one character in either string.
#
# Example 1:
# Input: "sea", "eat"
# Output: 2
# Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
# Note:
# The length of given words won't exceed 500.
# Characters in given words can only be lower-case letters.
import collections


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp1 = collections.Counter(word1)
        dp2 = collections.Counter(word2)
        step = 0
        for k, v in dp1.items():
            if k in dp2:
                if dp2[k] > v:
                    step += dp2[k] - v
            else:
                step += v

        for k, v in dp2.items():
            if k in dp1:
                if dp2[k] > v:
                    step += dp1[k] - v
            else:
                step += v

        return step

    def minDistance2(self, word1: str, word2: str) -> int:
        dp1 = collections.Counter(word1)
        dp2 = collections.Counter(word2)
        dp = {}
        for k, v in dp1.items():
            if k in dp2:
                dp[k] = min(dp2[k], v)

        
        return 1


if __name__ == '__main__':
    s = Solution()
    print(s.minDistance2("seac",
                         "atce"))
