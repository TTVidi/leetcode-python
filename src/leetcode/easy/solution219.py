# Contains Duplicate II

# Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array
# such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
#
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        m = {}
        for i, v in enumerate(nums):
            if v in m:
                li = m[v]
                idx = li.pop(-1)
                if i - idx <= k:
                    return True
                li.append(idx)
                li.append(i)
            else:
                m[v] = [i]
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.containsNearbyDuplicate())
