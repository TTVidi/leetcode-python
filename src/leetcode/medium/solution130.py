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
        if not board:
            return []
        i_l = len(board)
        j_l = len(board[0])

        def draw(i: int, j: int):
            if i < 0 or j < 0 or i >= i_l or j >= j_l:
                return
            if board[i][j] == "O":
                board[i][j] = "W"
                draw(i - 1, j)
                draw(i + 1, j)
                draw(i, j - 1)
                draw(i, j + 1)

        for i, v in enumerate(board):
            for j, k in enumerate(v):
                if k == "O":
                    if i == 0 or j == 0 or i == i_l - 1 or j == j_l - 1:
                        draw(i, j)

        for i, v in enumerate(board):
            for j, k in enumerate(v):
                if k == "O":
                    board[i][j] = "X"
                if k == "W":
                    board[i][j] = "O"
        print(board)


if __name__ == '__main__':
    s = Solution()
    s.solve([]
            )
