from typing import List


# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest
# sum and return its sum.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        i = 1
        min_sum = nums[0]
        while i < len(nums):
            if nums[i] > 0:
                sum = max_sum
                if min_sum < 0:
                    sum = nums[i]
                    min_sum = nums[i]
                    print()
                else:
                    sum = nums[i] + min_sum
                    min_sum += nums[i]
                max_sum = max(sum, max_sum)
            else:
                max_sum = max(nums[i], max_sum)
                min_sum += nums[i]
            i += 1
        return max_sum


if __name__ == '__main__':
    s = Solution()
    print(s.maxSubArray([-2, -1]))
