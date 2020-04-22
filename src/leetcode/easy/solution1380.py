# Lucky Numbers in a Matrix
# Given a m * n matrix of distinct numbers, return all lucky numbers in the matrix in any order.
#
# A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.
from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        min_row = []
        max_column = []
        result = []
        # find min in each row
        for i, row in enumerate(matrix):
            min_idx = 0
            for j, column in enumerate(row):
                if column < row[min_idx]:
                    min_idx = j
            min_row.append(min_idx)

        # find max in each column
        j = 0
        while j < len(matrix[0]):
            max_idx = 0
            i = 0
            while i < len(matrix):
                if matrix[i][j] > matrix[max_idx][j]:
                    max_idx = i
                i += 1
            max_column.append(max_idx)
            j += 1
        # find intersect number
        for i, j in enumerate(min_row):
            if i == max_column[j]:
                result.append(matrix[i][j])
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.luckyNumbers([[7,8],[1,2]]))
