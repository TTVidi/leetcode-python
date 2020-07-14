# In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty.
#
# There is at least one empty seat, and at least one person sitting.
#
# Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized.
#
# Return that maximum distance to closest person.
#
# Example 1:
#
# Input: [1,0,0,0,1,0,1]
# Output: 2
# Explanation:
# If Alex sits in the second open seat (seats[2]), then the closest person has distance 2.
# If Alex sits in any other open seat, the closest person has distance 1.
# Thus, the maximum distance to the closest person is 2.
# Example 2:
#
# Input: [1,0,0,0]
# Output: 3
# Explanation:
# If Alex sits in the last seat, the closest person is 3 seats away.
# This is the maximum distance possible, so the answer is 3.
#
#
# Constraints:
#
# 2 <= seats.length <= 20000
# seats contains only 0s or 1s, at least one 0, and at least one 1.
from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        max_zero = 0
        zero_count = 0
        pre_zero = -1
        for i in range(len(seats)):
            if seats[i] == 0:
                zero_count += 1
                max_zero = max(max_zero, zero_count)
            else:
                if pre_zero == -1:
                    pre_zero = i
                zero_count = 0
        j = len(seats) - 1
        while j >= 0:
            if seats[j] == 1:
                break
            j -= 1
        return max((max_zero + 1) >> 1, pre_zero, len(seats) - 1 - j)


if __name__ == '__main__':
    s = Solution()
    print(s.maxDistToClosest([1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1]))
