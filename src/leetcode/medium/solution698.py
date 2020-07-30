# Partition to K Equal Sum Subsets

# Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k
# non-empty subsets whose sums are all equal.
#
#
#
# Example 1:
#
# Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
# Output: True
# Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
#
#
# Note:
#
# 1 <= k <= len(nums) <= 16.
# 0 < nums[i] < 10000.
from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        s = sum(nums)

        if s % k != 0:
            return False

        used = [0] * len(nums)

        avg = s // k

        def search(index: int, subSum: int, rest: int) -> bool:
            if rest <= 1:
                return True

            if subSum == avg:
                return search(0, 0, rest - 1)

            for i in range(index, len(nums)):
                if used[i] == 0 and subSum + nums[i] <= avg:
                    used[i] = 1
                    if search(i + 1, subSum + nums[i], rest):
                        return True
                    used[i] = 0
            return False

        return search(0, 0, k)


if __name__ == '__main__':
    s = Solution()
    print(s.canPartitionKSubsets([2, 2, 2, 2, 3, 4, 5],
                                 4))
