# Surrounded Regions

# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
#
# A region is captured by flipping all 'O's into 'X's in that surrounded region.
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if board:
            i_l = len(board)
            j_l = len(board[0])

            def draw(i: int, j: int):
                if board[i][j] == "O":
                    board[i][j] = "Z"
                    if i - 1 >= 0:
                        draw(i - 1, j)
                    if i + 1 < i_l:
                        draw(i + 1, j)
                    if j - 1 >= 0:
                        draw(i, j - 1)
                    if j + 1 < j_l:
                        draw(i, j + 1)

            for i in range(i_l):
                for j in range(j_l):
                    if board[i][j] == "O":
                        if i == 0 or j == 0 or i == i_l - 1 or j == j_l - 1:
                            draw(i, j)

            for i in range(i_l):
                for j in range(j_l):
                    if board[i][j] == "O":
                        board[i][j] = "X"
                    elif board[i][j] == "Z":
                        board[i][j] = "O"


if __name__ == '__main__':
    s = Solution()
    print(s.solve([["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]))
