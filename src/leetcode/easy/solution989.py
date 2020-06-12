# Add to Array-Form of Integer

# For a non-negative integer X, the array-form of X is an array of its digits in left to right order.  For example,
# if X = 1231, then the array form is [1,2,3,1].
#
# Given the array-form A of a non-negative integer X, return the array-form of the integer X+K.
#
from typing import List


class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        more = 0
        s = str(K)
        length = len(s)
        li = []
        for i in range(length):
            li.append(int(s[length - 1 - i]))
        A.reverse()
        i = 0
        rs = []
        while i < length and i < len(A):
            current = A[i] + li[i] + more
            more = 0
            if current > 9:
                current -= 10
                more = 1
            rs.append(current)
            i += 1

        while i < length:
            current = li[i] + more
            more = 0
            if current > 9:
                current -= 10
                more = 1
            rs.append(current)
            i += 1

        while i < len(A):
            current = A[i] + more
            more = 0
            if current > 9:
                current -= 10
                more = 1
            rs.append(current)
            i += 1

        if more == 1:
            rs.append(1)
        rs.reverse()
        return rs


if __name__ == '__main__':
    s = Solution()
    print(s.addToArrayForm([9,9,9,9,9,9,9,9,9,9], 1))
