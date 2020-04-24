# Create Target Array in the Given Order

# Given two arrays of integers nums and index. Your task is to create target array under the following rules:
#
# Initially target array is empty.
# From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
# Repeat the previous step until there are no elements to read in nums and index.
# Return the target array.
#
# It is guaranteed that the insertion operations will be valid.
from typing import List


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        li = []
        for i, v in enumerate(index):
            if not li:
                li.append(nums[i])
            else:
                pre = li[:v]
                suf = li[v:]
                pre.append(nums[i])
                pre.extend(suf)
                li = pre
        return li

    def createTargetArray2(self, nums: List[int], index: List[int]) -> List[int]:
        li = []
        for i in range(len(index)):
            li.insert(index[i], nums[i])
        return li


if __name__ == '__main__':
    s = Solution()
    print(s.createTargetArray2([0, 1, 2, 3, 4], [0, 1, 2, 2, 1]))
