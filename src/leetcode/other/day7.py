# Counting Elements

# Given an integer array arr, count element x such that x + 1 is also in arr.
#
# If there're duplicates in arr, count them seperately.
from typing import List


class Solution:
    def countElements(self, arr: List[int]) -> int:
        s = set()
        for a in arr:
            s.add(a)
        result = 0
        for a in arr:
            if s.__contains__(a+1):
                result += 1
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.countElements([1, 2, 3]))
