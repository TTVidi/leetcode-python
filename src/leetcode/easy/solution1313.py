# Decompress Run-Length Encoded List
# We are given a list nums of integers representing a list compressed with run-length encoding.
#
# Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).  For each such pair,
# there are freq elements with value val concatenated in a sublist. Concatenate all the sublists from left to right
# to generate the decompressed list.
#
# Return the decompressed list.
#
#
from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        i = 0
        li = []
        while i < len(nums):
            li.extend([nums[i + 1]] * nums[i])
            i += 2
        return li


if __name__ == '__main__':
    s = Solution()
    print(s.decompressRLElist([1, 2, 3, 4]))
