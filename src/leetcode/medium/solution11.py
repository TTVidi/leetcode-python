# Container With Most Water

# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical
# lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with
# x-axis forms a container, such that the container contains the most water.
#
# Note: You may not slant the container and n is at least 2.
#
#
#
#
#
# The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue
# section) the container can contain is 49.
#
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        ma = 0
        i = 0
        length = len(height)
        while i < length - 1:
            j = i + 1
            while j < length:
                s = min(height[i], height[j]) * (j - i)
                ma = max(ma, s)
                j += 1
            i += 1
        return ma

    def maxArea2(self, height: List[int]) -> int:
        ma = 0
        left, right = 0, len(height) - 1
        while left < right:
            ma = max(ma, min(height[left], height[right]) * (right - left))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return ma


if __name__ == '__main__':
    s = Solution()
    print(s.maxArea2([1, 8, 6, 2, 5, 4, 8, 3, 7]))
