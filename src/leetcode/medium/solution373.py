#  Find K Pairs with Smallest Sums

# You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.
#
# Define a pair (u,v) which consists of one element from the first array and one element from the second array.
#
# Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        return None


if __name__ == '__main__':
    s = Solution()
    print(s.kSmallestPairs([1, 7, 11], [2, 4, 6], 3))
