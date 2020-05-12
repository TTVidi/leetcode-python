# Largest Rectangle in Histogram

# Given n non-negative integers representing the histogram's bar height where the width of each bar is 1,
# find the area of largest rectangle in the histogram.
#
from typing import List


class Solution:
    def largestRectangleArea1(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for i, bar in enumerate(heights):
            ind = i
            while stack and stack[-1][0] >= bar:
                val, ind = stack.pop()
                maxArea = max(maxArea, val * (i - ind))
            stack.append((bar, ind))

        while stack:
            val, ind = stack.pop()
            maxArea = max(maxArea, val * (len(heights) - ind))

        return maxArea

    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        _length = len(heights)
        for i, v in enumerate(heights):
            idx = i
            while stack and stack[-1][1] >= v:
                idx, val = stack.pop()
                max_area = max(max_area, val * (i - idx))
            stack.append((idx, v))

        while stack:
            sv = stack.pop()
            max_area = max(max_area, sv[1] * (_length - sv[0]))
        return max_area


if __name__ == '__main__':
    s = Solution()
    print(s.largestRectangleArea([1, 1]))
