# Total Hamming Distance

# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
#
# Now your job is to find the total Hamming distance between all pairs of the given numbers.
from typing import List


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        def hamming_distance(x: int, y: int) -> int:
            return bin(x ^ y).count("1")

        length = len(nums)
        s = 0
        for i in range(length):
            for j in range(i + 1, length):
                s += (hamming_distance(nums[i], nums[j]))
        return s


if __name__ == '__main__':
    s = Solution()
    print(s.totalHammingDistance([4, 14, 2]))
