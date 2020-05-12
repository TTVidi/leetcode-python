# Unique Paths

# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
#
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right
# corner of the grid (marked 'Finish' in the diagram below).
#
# How many possible unique paths are there?
#


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        _dict = {(0, 1): 1, (1, 0): 1}

        def find(i: int, j: int) -> int:
            k = (i, j)
            if i == 0 or j == 0:
                _dict[k] = 1
                return 1
            if k in _dict:
                return _dict[k]
            top = 0
            left = 0
            if i - 1 >= 0:
                top = find(i - 1, j)
            if j - 1 >= 0:
                left = find(i, j - 1)
            _dict[k] = top + left
            return top + left

        return find(m - 1, n - 1)

    def uniquePaths1(self, m: int, n: int) -> int:
        temp = [[0] * n for i in range(m)]
        for i in range(n):
            temp[0][i] = 1

        for i in range(m):
            temp[i][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                temp[i][j] = temp[i - 1][j] + temp[i][j - 1]
        return temp[m - 1][n - 1]

    def uniquePaths3(self, m: int, n: int) -> int:
        temp = [[0] * n] * m
        for i in range(m):
            for j in range(n):
                if i == 0:
                    temp[i][j] = 1
                elif j == 0:
                    temp[i][j] = 1
                else:
                    temp[i][j] = temp[i - 1][j] + temp[i][j - 1]
        return temp[m - 1][n - 1]


if __name__ == '__main__':
    s = Solution()
    print(s.uniquePaths3(7, 3))
