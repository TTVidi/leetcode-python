# The K Weakest Rows in a Matrix
#
# Given a m * n matrix mat of ones (representing soldiers) and zeros (representing civilians), return the indexes of
# the k weakest rows in the matrix ordered from the weakest to the strongest.
#
# A row i is weaker than row j, if the number of soldiers in row i is less than the number of soldiers in row j,
# or they have the same number of soldiers but i is less than j. Soldiers are always stand in the frontier of a row,
# that is, always ones may appear first and then zeros.
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        n = len(mat[0])

        def count_one(v: List[int], begin: int, end: int) -> int:
            if v[end] == 1:
                return end + 1
            if v[begin] == 0:
                return begin
            mid = (begin + end) >> 1
            if v[mid] == 1:
                return count_one(v, mid + 1, end)
            return count_one(v, begin, mid - 1)

        dict = {}
        for i, v in enumerate(mat):
            num = count_one(v, 0, n - 1)
            if num not in dict:
                dict[num] = [i]
            else:
                dict[num].append(i)
        li = []
        for i in range(n + 1):
            if i in dict:
                size = len(dict[i])
                if size >= k:
                    li.extend(dict[i][:k])
                    break
                else:
                    li.extend(dict[i])
                    k -= size
        return li


if __name__ == '__main__':
    s = Solution()
    print(s.kWeakestRows([[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]], 1))
