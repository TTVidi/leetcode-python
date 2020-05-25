# Advantage Shuffle

# Given two arrays A and B of equal size, the advantage of A with respect to B is the number of indices i for which
# A[i] > B[i].
#
# Return any permutation of A that maximizes its advantage with respect to B.
#
#
#
import collections
from typing import List


class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        """
       :type A: List[int]
       :type B: List[int]
       :rtype: List[int]
       """
        res = [-1] * len(A)
        A = collections.deque(sorted(A))
        B = collections.deque(sorted((b, i) for i, b in enumerate(B)))
        for i in range(len(A)):
            a = A.popleft()
            b = B[0]
            if a > b[0]:
                B.popleft()
            else:
                b = B.pop()
            res[b[1]] = a
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.advantageCount([12, 24, 8, 32], [13, 25, 32, 11]))
