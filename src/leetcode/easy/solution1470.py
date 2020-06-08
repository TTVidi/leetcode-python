# Shuffle the Array

# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
#
# Return the array in the form [x1,y1,x2,y2,...,xn,yn].
from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        i = 0
        li = []
        while i < n:
            li.append(nums[i])
            li.append(nums[i + n])
            i += 1
        return li


if __name__ == '__main__':
    s = Solution()
    print(s.shuffle())
