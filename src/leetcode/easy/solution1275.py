# Find Winner on a Tic Tac Toe Game

# Tic-tac-toe is played by two players A and B on a 3 x 3 grid.
#
# Here are the rules of Tic-Tac-Toe:
#
# Players take turns placing characters into empty squares (" "). The first player A always places "X" characters,
# while the second player B always places "O" characters. "X" and "O" characters are always placed into empty
# squares, never on filled ones. The game ends when there are 3 of the same (non-empty) character filling any row,
# column, or diagonal. The game also ends if all squares are non-empty. No more moves can be played if the game is
# over. Given an array moves where each element is another array of size 2 corresponding to the row and column of the
# grid where they mark their respective character in the order in which A and B play.
#
# Return the winner of the game if it exists (A or B), in case the game ends in a draw return "Draw", if there are
# still movements to play return "Pending".
#
# You can assume that moves is valid (It follows the rules of Tic-Tac-Toe), the grid is initially empty and A will
# play first.
#
#
#
from typing import List


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [['' for x in range(3)] for y in range(3)]
        for index, move in enumerate(moves):
            i, j = move
            if index % 2 == 0:
                board[i][j] = 'A'
            else:
                board[i][j] = 'B'

        winning_lines = [[[0, 0], [0, 1], [0, 2]],
                         [[1, 0], [1, 1], [1, 2]],
                         [[2, 0], [2, 1], [2, 2]],
                         [[0, 0], [1, 0], [2, 0]],
                         [[0, 1], [1, 1], [2, 1]],
                         [[0, 2], [1, 2], [2, 2]],
                         [[0, 0], [1, 1], [2, 2]],
                         [[0, 2], [1, 1], [2, 0]]]

        def checkWinner(s):
            return any(all(board[i][j] == s for i, j in line) for line in winning_lines)

        if checkWinner('A'):
            return "A"
        elif checkWinner('B'):
            return "B"
        elif len(moves) == 9:
            return "Draw"
        return "Pending"


if __name__ == '__main__':
    s = Solution()
    print(s.tictactoe([[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]]))
