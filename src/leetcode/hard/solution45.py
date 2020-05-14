#  Jump Game II

# Given an array of non-negative integers, you are initially positioned at the first index of the array.
#
# Each element in the array represents your maximum jump length at that position.
#
# Your goal is to reach the last index in the minimum number of jumps.
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1:
            return 0
        pos = 0
        count = 1
        while pos + nums[pos] < l - 1:
            count += 1
            mi = pos
            for i in range(pos + 1, pos + nums[pos] + 1):
                if nums[i] + i >= l - 1:
                    return count
                if nums[i] + i > nums[mi] + mi:
                    mi = i
            pos = mi
        return count


if __name__ == '__main__':
    s = Solution()
    print(s.jump([2, 3, 1, 1, 4, 1, 2, 1, 2, 3, 5]))
    print(s.jump([1, 2]))
    print(s.jump([0]))
    print(s.jump([1, 1, 1, 1, 1, 1, 1]))
