# H-Index II
# Given an array of citations sorted in ascending order (each citation is a non-negative integer) of a
# researcher, write a function to compute the researcher's h-index.
#
# According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at
# least h citations each, and the other N − h papers have no more than h citations each."
#
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left, right = 0, len(citations) - 1
        N = len(citations)
        while left <= right:
            H = left + (right - left) // 2
            if citations[H] >= N - H:
                right = H - 1
            else:
                left = H + 1
        return N - left
