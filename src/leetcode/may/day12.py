#  Single Element in a Sorted Array

# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one
# element which appears exactly once. Find this single element that appears only once.
#
from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if nums:
            initial = 0
            pre = nums[0]
            for c in nums:
                if c == pre:
                    initial += 1
                else:
                    initial -= 1
                if initial == 0:
                    return pre
                pre = c
            return pre
        return 0

    def singleNonDuplicate2(self, nums: List[int]) -> int:
        begin = 0
        end = len(nums) - 1
        while begin < end:
            middle = (begin + end) >> 1
            left = middle - begin
            right = end - middle
            if nums[middle] == nums[middle - 1]:
                if (left + 1) % 2 == 0:
                    begin = middle + 1
                else:
                    end = middle
            elif nums[middle] == nums[middle + 1]:
                if (right + 1) % 2 == 0:
                    end = middle - 1
                else:
                    begin = middle
            else:
                return nums[middle]
        return nums[begin]


if __name__ == '__main__':
    s = Solution()
    print(s.singleNonDuplicate2([1, 1, 2, 2, 3, 4, 4]))
