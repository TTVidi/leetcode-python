# Merge Intervals

# Given a collection of intervals, merge all overlapping intervals.
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        i = 0
        li = []
        while i < len(intervals):
            current = intervals[i]
            if li:
                last = li.pop(-1)
                if current[0] > last[1]:
                    li.append(last)
                    li.append(current)
                if current[0] <= last[1]:
                    last[1] = max(last[1], current[1])
                    li.append(last)
            else:
                li.append(current)
            i += 1

        return li


if __name__ == '__main__':
    s = Solution()
    print(s.merge([[1, 4], [4, 5]]))
