# Partition Equal Subset Sum

# Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets
# such that the sum of elements in both subsets is equal.
#
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        length = len(nums)
        if length <= 1:
            return False
        _sum = sum(nums)
        if _sum % 2 == 0:
            # check if sum of some nums[i] equals to total
            def canSum(nums: List[int], total: int) -> bool:
                _set = set()
                for num in nums:
                    if num == total:
                        return True
                    _temp = set()
                    _temp.add(num)
                    for v in _set:
                        if v + num == total:
                            return True
                        _temp.add(v + num)
                    _set = _set.union(_temp)
                return False

            return canSum(nums, _sum >> 1)


if __name__ == '__main__':
    s = Solution()
    print(s.canPartition([23, 13, 11, 7, 6, 5, 5]))
