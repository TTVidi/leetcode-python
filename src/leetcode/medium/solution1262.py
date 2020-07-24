# Greatest Sum Divisible by Three

# Given an array nums of integers, we need to find the maximum possible sum of elements of the array such that it is
# divisible by three.
#
#
#
# Example 1:
#
# Input: nums = [3,6,5,1,8]
# Output: 18
# Explanation: Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).
# Example 2:
#
# Input: nums = [4]
# Output: 0
# Explanation: Since 4 is not divisible by 3, do not pick any number.
# Example 3:
#
# Input: nums = [1,2,3,4,4]
# Output: 12
# Explanation: Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum divisible by 3).
#
#
# Constraints:
#
# 1 <= nums.length <= 4 * 10^4
# 1 <= nums[i] <= 10^4
from typing import List


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        d1 = []
        d2 = []
        res = 0
        for num in nums:
            res += num
            if num % 3 == 1:
                if len(d1) < 2:
                    d1.append(num)
                else:
                    v1 = d1.pop()
                    v2 = d1.pop()
                    mi = min(v1, v2, num)
                    mx = max(v1, v2, num)
                    d1.append(mi)
                    d1.append(v1 + v2 + num - mi - mx)
            elif num % 3 == 2:
                if len(d2) < 2:
                    d2.append(num)
                else:
                    v1 = d2.pop()
                    v2 = d2.pop()
                    mi = min(v1, v2, num)
                    mx = max(v1, v2, num)
                    d2.append(mi)
                    d2.append(v1 + v2 + num - mi - mx)
        if res % 3 == 0:
            return res
        elif res % 3 == 1:
            r1 = res
            r2 = res
            if d1:
                r1 = min(d1)

            if d2 and len(d2) == 2:
                r2 = sum(d2)
            res -= min(r1, r2)
        else:
            r1 = res
            r2 = res
            if d1 and len(d1) == 2:
                r1 = sum(d1)

            if d2:
                r2 = min(d2)
            res -= min(r1, r2)

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.maxSumDivThree([3, 6, 5, 1, 8]))
