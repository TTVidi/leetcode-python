# Permutations II

# Given a collection of numbers that might contain duplicates, return all possible unique permutations.
#
# Example:
#
# Input: [1,1,2]
# Output:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        _set = set()

        def back(arr: List[int], current: str):
            if arr:
                for i in range(len(arr)):
                    k = arr.pop(i)
                    temp = current + str(k) + ","
                    back(arr, temp)
                    arr.insert(i, k)
            else:
                _set.add(current[0:-1])

        back(nums, "")
        li = []
        for v in _set:
            arr = v.split(",")
            for i, k in enumerate(arr):
                arr[i] = int(k)
            li.append(arr)
        return li


if __name__ == '__main__':
    s = Solution()
    print(s.permuteUnique([1, 1, 2]))
