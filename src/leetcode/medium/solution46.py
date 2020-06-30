# Permutations

# Given a collection of distinct integers, return all possible permutations.
#
# Example:
#
# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        li = []

        def back(arr: List[int], current: List[int]):
            if arr:
                for i in range(len(arr)):
                    k = arr.pop(i)
                    current.append(k)
                    back(arr, current)
                    current.pop(-1)
                    arr.insert(i, k)
            else:
                li.append(current.copy())
        back(nums, [])
        return li


if __name__ == '__main__':
    s = Solution()
    print(s.permute([1,1,2]))
