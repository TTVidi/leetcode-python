# House Robber II


# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money
# stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last
# one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two
# adjacent houses were broken into on the same night.
#
# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount
# of money you can rob tonight without alerting the police.
#
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if nums:
            _l = len(nums)
            if _l <= 2:
                return max(nums)

            def count_max(list: List[int], n: int, _dict: dict) -> int:
                if n in _dict:
                    return _dict[n]
                if n == 1:
                    _dict[n] = list[0]
                    return _dict[n]
                if n == 2:
                    _dict[n] = max(list[0], list[1])
                    return _dict[n]
                r = max(count_max(list, n - 1, _dict), count_max(list, n - 2, _dict) + list[n - 1])
                _dict[n] = r
                return r

            return max(count_max(nums[1:], _l - 1, {}), count_max(nums[:-1], _l - 1, {}))
        return 0


if __name__ == '__main__':
    s = Solution()
    print(s.rob([2, 3, 2]))
