# Students are asked to stand in non-decreasing order of heights for an annual photo.
#
# Return the minimum number of students that must move in order for all students to be standing in non-decreasing
# order of height.
#
# Notice that when a group of students is selected they can reorder in any possible way between themselves and the
# non selected students remain on their seats.
#
from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        temp = heights.copy()
        temp.sort()
        s = 0
        for i in range(len(heights)):
            if heights[i] != temp[i]:
                s += 1
        return s
