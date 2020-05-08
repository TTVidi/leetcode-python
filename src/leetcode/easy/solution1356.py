# Sort Integers by The Number of 1 Bits

# Given an integer array arr. You have to sort the integers in the array in ascending order by the number of 1's in
# their binary representation and in case of two or more integers have the same number of 1's you have to sort them
# in ascending order.
#
# Return the sorted array.
#
from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        _dict = {0: 0, 1: 1}
        arr.sort()

        # count bit one count
        def count_one(num: int) -> int:
            if num in _dict:
                return _dict[num]
            return num % 2 + count_one(num >> 1)

        _temp = {}
        for n in arr:
            c = count_one(n)
            if c in _temp:
                _temp[c].append(n)
            else:
                _temp[c] = [n]
        li = []
        for i in range(15):
            if i in _temp:
                li.extend(_temp[i])
        return li


if __name__ == '__main__':
    s = Solution()
    print(s.sortByBits([1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]))
