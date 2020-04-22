# Replace Elements with Greatest Element on Right Side

# Given an array arr, replace every element in that array with the greatest element among the elements to its right,
# and replace the last element with -1.
#
# After doing so, return the array.
from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_arr = []
        length = len(arr)
        l = length - 1
        current_max = arr[l]
        max_arr.append([l, current_max])
        while l >= 0:
            l -= 1
            if arr[l] >= current_max:
                current_max = arr[l]
                max_arr.append([l, current_max])
        print(max_arr)
        arr = []
        l = 0
        top = max_arr.pop()
        while l < length - 1:
            if l >= top[0]:
                top = max_arr.pop()
            arr.append(top[1])
            l += 1
        arr.append(-1)
        return arr


if __name__ == '__main__':
    s = Solution()
    print(s.replaceElements([17, 18, 5, 4, 6, 1]))
