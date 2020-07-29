# Sum of Subarray Minimums

# Given an array of integers A, find the sum of min(B), where B ranges over every (contiguous) subarray of A.
#
# Since the answer may be large, return the answer modulo 10^9 + 7.
#
#
#
# Example 1:
#
# Input: [3,1,2,4]
# Output: 17
# Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].
# Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.
#
#
# Note:
#
# 1 <= A.length <= 30000
# 1 <= A[i] <= 30000
from typing import List


class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        s = 0
        for i in range(len(A)):
            left = i - 1
            right = i + 1
            while left >= 0 and A[left] >= A[i]:
                left -= 1
            while right < len(A) and A[right] > A[i]:
                right += 1
            s += ((i - left) * (right - i) * A[i])
            s = s % (10 ** 9 + 7)
        return s

    def sumSubarrayMins2(self, A: List[int]) -> int:
        stack = []
        dp = [0] * len(A)
        for i, v in enumerate(A):
            while stack and A[stack[-1]] >= v:
                stack.pop()

            if stack:
                dp[i] = dp[stack[-1]] + v * (i - stack[-1])
            else:
                dp[i] = v * (i + 1)
            stack.append(i)
        return sum(dp) % (10 ** 9 + 7)


if __name__ == '__main__':
    s = Solution()
    print(s.sumSubarrayMins2([71, 55, 82, 55]))
