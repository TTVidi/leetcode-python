# Non-overlapping Intervals

# Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the
# intervals non-overlapping.
#
#
#
# Example 1:
#
# Input: [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
# Example 2:
#
# Input: [[1,2],[1,2],[1,2]]
# Output: 2
# Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
# Example 3:
#
# Input: [[1,2],[2,3]]
# Output: 0
# Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
#
#
# Note:
#
# You may assume the interval's end point is always bigger than its start point.
# Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.
#
#
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda l: l[0])
        stack = []
        res = 0
        for interval in intervals:
            if stack:
                last = stack.pop(-1)
                if interval[0] >= last[1]:
                    stack.append(last)
                    stack.append(interval)
                else:
                    res += 1
                    if last[1] > interval[1]:
                        stack.append(interval)
                    else:
                        stack.append(last)
            else:
                stack.append(interval)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.eraseOverlapIntervals([[1,2],[4,9],[3,5],[6,7]]))
