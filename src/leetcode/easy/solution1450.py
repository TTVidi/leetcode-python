#  Number of Students Doing Homework at a Given Time
# Given two integer arrays startTime and endTime and given an integer queryTime.
#
# The ith student started doing their homework at the time startTime[i] and finished it at time endTime[i].
#
# Return the number of students doing their homework at time queryTime. More formally, return the number of students
# where queryTime lays in the interval [startTime[i], endTime[i]] inclusive.
#
from typing import List


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count = 0
        if startTime and endTime:
            for i in range(len(startTime)):
                if startTime[i] <= queryTime <= endTime[i]:
                    count += 1
        return count


if __name__ == '__main__':
    s = Solution()
    print(s.busyStudent([1, 2, 3], [3, 2, 7], 4))
