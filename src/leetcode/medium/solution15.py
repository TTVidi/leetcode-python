# 3Sum

# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique
# triplets in the array which gives the sum of zero.
#
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        counter = {}
        for i in range(len(nums)):
            k = nums[i]
            if k in counter:
                counter[k].append(i)
            else:
                counter[k] = [i]
        res = []
        st = set()

        def find(idx_arr: List[int], idx: int) -> bool:
            length = len(idx_arr)
            for i in range(length):
                if idx_arr[length - 1 - i] > idx:
                    return True
            return False

        l = len(nums)
        for i in range(l - 2):
            for j in range(i + 1, l - 1):
                rest = -(nums[i] + nums[j])
                if rest in counter:
                    arr = counter[rest]
                    if find(arr, j):
                        mx = max(nums[i], nums[j], rest)
                        mi = min(nums[i], nums[j], rest)
                        keys = str(mi) + "," + str(mx)
                        if keys not in st:
                            res.append([nums[i], nums[j], rest])
                            st.add(keys)

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))
