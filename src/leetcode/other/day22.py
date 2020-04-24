# Subarray Sum Equals K
#
# Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum
# equals to k.
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        map = {nums[0]: [0]}
        sum = nums[0]
        for i, v in enumerate(nums):
            if i > 0:
                sum += v
                if map.get(sum):
                    map[sum].append(i)
                else:
                    map[sum] = [i]

        for key, current_list in map.items():
            pre = key - k
            if map.get(pre):
                pre_list = map[pre]
                for c in current_list:
                    for v in pre_list:
                        if v < c:
                            count += 1
                        else:
                            break
        if map.get(k):
            count += len(map[k])
        return count

    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {0: 1}
        total = 0
        count = 0
        for num in nums:
            total += num
            if total - k in d:
                count += d[total - k]

            d[total] = d.get(total, 0) + 1

        return count


if __name__ == '__main__':
    s = Solution()
    print(
        s.subarraySum([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 4, 4, 4, -2, -2, -2, 0, 0, -2, 4, -2, 4, 2], 2))
    print(
        s.subarraySum([-1, -1, 1], 0))
