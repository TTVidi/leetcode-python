# Build an Array With Stack Operations

# Given an array target and an integer n. In each iteration, you will read a number from  list = {1,2,3..., n}.
#
# Build the target array using the following operations:
#
# Push: Read a new element from the beginning list, and push it in the array.
# Pop: delete the last element of the array.
# If the target array is already built, stop reading more elements.
# You are guaranteed that the target array is strictly increasing, only containing numbers between 1 to n inclusive.
#
# Return the operations to build the target array.
#
# You are guaranteed that the answer is unique.
from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        li = []
        idx = 1
        i = 0
        while i < len(target):
            if target[i] == idx:
                li.append("Push")
                i += 1
            else:
                li.append("Push")
                li.append("Pop")
            idx += 1
        return li


if __name__ == '__main__':
    s = Solution()
    print(s.buildArray([2, 3, 4], 4))
