# Best Sightseeing Pair

# Given an array A of positive integers, A[i] represents the value of the i-th sightseeing spot, and two sightseeing
# spots i and j have distance j - i between them.
#
# The score of a pair (i < j) of sightseeing spots is (A[i] + A[j] + i - j) : the sum of the values of the
# sightseeing spots, minus the distance between them.
#
# Return the maximum score of a pair of sightseeing spots.
from typing import List


class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        length = len(A)
        pre = A[0]
        ma = 0
        for i in range(1, length):
            ma = max(ma, pre + A[i] - i)
            if A[i] + i > pre:
                pre = A[i] + i
        return ma


if __name__ == '__main__':
    s = Solution()
    print(s.maxScoreSightseeingPair([8, 1, 5, 2, 6]))
