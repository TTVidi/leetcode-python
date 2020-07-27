# Median of Two Sorted Arrays

# There are two sorted arrays nums1 and nums2 of size m and n respectively.
#
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
#
# You may assume nums1 and nums2 cannot be both empty.
#
# Example 1:
#
# nums1 = [1, 3]
# nums2 = [2]
#
# The median is 2.0
# Example 2:
#
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# The median is (2 + 3)/2 = 2.5
import sys
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1 = len(nums1)
        l2 = len(nums2)
        l = l1 + l2
        even = l % 2 == 0
        if l1 > l2:
            nums1, nums2 = nums2, nums1
            l1, l2 = l2, l1
        low = 0
        high = l1
        while low <= high:
            x_middle = (low + high) >> 1
            x_left_max = 0
            x_right_min = 0
            if x_middle == 0:
                x_left_max = -sys.maxsize
            else:
                x_left_max = nums1[x_middle - 1]
            if x_middle == l1:
                x_right_min = sys.maxsize
            else:
                x_right_min = nums1[x_middle]

            y_middle = ((l + 1) >> 1) - x_middle
            y_left_max = 0
            y_right_min = 0
            if y_middle == 0:
                y_left_max = -sys.maxsize
            else:
                y_left_max = nums2[y_middle - 1]
            if y_middle == l2:
                y_right_min = sys.maxsize
            else:
                y_right_min = nums2[y_middle]

            if x_left_max <= y_right_min and y_left_max <= x_right_min:
                if even:
                    return (max(x_left_max, y_left_max) + min(y_right_min, x_right_min)) / 2
                else:
                    return max((x_left_max, y_left_max))

            elif x_left_max > y_right_min:
                high = x_middle - 1
            else:
                low = x_middle + 1
        return 0


if __name__ == '__main__':
    s = Solution()
    print(s.findMedianSortedArrays([5, 6, 7], [3, 4]))
