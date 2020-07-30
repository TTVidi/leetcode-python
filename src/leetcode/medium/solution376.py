# Wiggle Subsequence

# A sequence of numbers is called a wiggle sequence if the differences between successive numbers strictly alternate
# between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence
# with fewer than two elements is trivially a wiggle sequence.
#
# For example, [1,7,4,9,2,5] is a wiggle sequence because the differences (6,-3,5,-7,3) are alternately positive and
# negative. In contrast, [1,4,7,2,5] and [1,7,4,5,5] are not wiggle sequences, the first because its first two
# differences are positive and the second because its last difference is zero.
#
# Given a sequence of integers, return the length of the longest subsequence that is a wiggle sequence. A subsequence
# is obtained by deleting some number of elements (eventually, also zero) from the original sequence, leaving the
# remaining elements in their original order.
#
# Example 1:
#
# Input: [1,7,4,9,2,5]
# Output: 6
# Explanation: The entire sequence is a wiggle sequence.
# Example 2:
#
# Input: [1,17,5,10,13,15,10,5,16,8]
# Output: 7
# Explanation: There are several subsequences that achieve this length. One is [1,17,10,13,10,16,8].
# Example 3:
#
# Input: [1,2,3,4,5,6,7,8,9]
# Output: 2
# Follow up:
# Can you do it in O(n) time?
from typing import List


class Solution:
    def wiggleMaxLength2(self, nums: List[int]) -> int:
        l = len(nums)
        if l <= 1:
            return l
        res = 1
        diff = nums[1] - nums[0]
        if diff != 0:
            res += 1

        for i in range(2, l):
            cDiff = nums[i] - nums[i - 1]
            if cDiff != 0:
                pro = cDiff * diff
                if pro <= 0:
                    res += 1
                    diff = cDiff
        return res

    def wiggleMaxLength1(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n
        prev_diff = nums[1] - nums[0]
        if prev_diff == 0:
            count = 1
        else:
            count = 2

        for i in range(2, n):
            print(nums[i - 1], nums[i], prev_diff, count)
            if (prev_diff <= 0 and nums[i] - nums[i - 1] > 0) or (prev_diff >= 0 and nums[i] - nums[i - 1] < 0):
                count += 1
                prev_diff = nums[i] - nums[i - 1]
        return count

    def wiggleMaxLength(self, nums: List[int]) -> int:
        if nums:
            dp = [[0] * 2 for i in range(len(nums))]
            dp[0][0] = 1
            dp[0][1] = 1

            def find(idx: int, smaller: bool) -> int:
                if idx == 0:
                    return 1
                elif idx < 0:
                    return 0
                else:
                    i = idx - 1
                    k = 0
                    if smaller:
                        if dp[idx][0] > 0:
                            return dp[idx][0]
                        while i >= 0 and nums[i] < nums[idx]:
                            k = max(k, find(i, False))
                            i -= 1
                        k += 1
                        dp[idx][0] = k
                    else:
                        if dp[idx][1] > 0:
                            return dp[idx][1]
                        while i >= 0 and nums[i] > nums[idx]:
                            k = max(k, find(i, True))
                            i -= 1
                        k += 1
                        dp[idx][1] = k
                    return k

            for i in range(len(nums)):
                idx = len(nums) - 1 - i
                if dp[idx][0] == 0:
                    find(idx, True)
                if dp[idx][1] == 0:
                    find(idx, False)
            mx = 0
            for i in range(len(nums)):
                mx = max(mx, dp[i][0], dp[i][1])
            return mx
        return 1


if __name__ == '__main__':
    s = Solution()
    print(s.wiggleMaxLength2([5, 5, 5]))
