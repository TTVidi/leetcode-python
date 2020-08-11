# Remove Covered Intervals

# Given a list of intervals, remove all intervals that are covered by another interval in the list. Interval [a,
# b) is covered by interval [c,d) if and only if c <= a and b <= d.
#
# After doing so, return the number of remaining intervals.
# Example 1:
#
# Input: intervals = [[1,4],[3,6],[2,8]]
# Output: 2
# Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
#
#
# Constraints:
#
# 1 <= intervals.length <= 1000
# 0 <= intervals[i][0] < intervals[i][1] <= 10^5
# intervals[i] != intervals[j] for all i != j
from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        length = len(intervals)
        skip = set()

        for i in range(length):
            if i not in skip:
                interval = intervals[i]
                j = i + 1
                c = True
                while j < length and c:
                    temp = intervals[j]
                    if interval[0] <= temp[0] and interval[1] >= temp[1]:
                        skip.add(j)
                    elif temp[0] <= interval[0] and temp[1] >= interval[1]:
                        skip.add(i)
                        c = False
                    j += 1

        return length - len(skip)


if __name__ == '__main__':
    s = Solution()
    print(s.removeCoveredIntervals([[1, 4], [3, 6], [2, 8]]))
