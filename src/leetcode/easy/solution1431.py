# Kids With the Greatest Number of Candies

# Given the array candies and the integer extraCandies, where candies[i] represents the number of candies that the
# ith kid has.
#
# For each kid check if there is a way to distribute extraCandies among the kids such that he or she can have the
# greatest number of candies among them. Notice that multiple kids can have the greatest number of candies.
#
#
#
from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        _max = max(candies)
        _li = []
        for candy in candies:
            if candy + extraCandies >= _max:
                _li.append(True)
            else:
                _li.append(False)
        return _li


if __name__ == '__main__':
    s = Solution()
    print(s.kidsWithCandies([4, 2, 1, 1, 2], 1))
