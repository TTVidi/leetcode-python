# Rank Transform of an Array

# Given an array of integers arr, replace each element with its rank.
#
# The rank represents how large the element is. The rank has the following rules:
#
# Rank is an integer starting from 1.
# The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
# Rank should be as small as possible.
#
from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if arr:
            temp = sorted(arr)
            sort_index = 1
            _dict = {}
            pre = temp[0]
            for c in temp:
                if c != pre:
                    sort_index += 1
                _dict[c] = sort_index
                pre = c
            for i in range(len(arr)):
                arr[i] = _dict[arr[i]]
        return arr


if __name__ == '__main__':
    s = Solution()
    print(s.arrayRankTransform([37, 12, 28, 9, 100, 56, 80, 5, 12]))
