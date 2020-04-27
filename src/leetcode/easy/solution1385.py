# Find the Distance Value Between Two Arrays

# Given two integer arrays arr1 and arr2, and the integer d, return the distance value between the two arrays.
#
# The distance value is defined as the number of elements arr1[i] such that there is not any element arr2[j] where
# |arr1[i]-arr2[j]| <= d.
from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        dist = []
        base = arr1[0]
        for c in arr2:
            dist.append(base - c)
        _sum = 0
        for c in arr1:
            distance = c - base
            temp = 1
            for k in dist:
                if abs(distance + k) <= d:
                    temp = 0
                    break
            _sum += temp
        return _sum


if __name__ == '__main__':
    s = Solution()
    print(s.findTheDistanceValue([1,4,2,3], [-4,-3,6,10,20,30], 3))
