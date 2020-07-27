# Word Search

# Given a 2D board and a word, find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those
# horizontally or vertically neighboring. The same letter cell may not be used more than once.
#
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        l1 = len(board)
        l2 = len(board[0])
        lw = len(word)

        def search(idx: int, x: int, y: int, path: set) -> bool:
            if 0 <= x < l1 and 0 <= y < l2:
                k = (x, y)
                if k not in path:
                    path.add(k)
                    if word[idx] == board[x][y]:
                        if idx == lw - 1:
                            return True
                        idx += 1
                        left = search(idx, x, y - 1, path)
                        if left:
                            return True
                        else:
                            right = search(idx, x, y + 1, path)
                            if right:
                                return True
                            else:
                                top = search(idx, x - 1, y, path)
                                if top:
                                    return True
                                else:
                                    down = search(idx, x + 1, y, path)
                                    if down:
                                        return True
                    path.remove(k)

            return False

        for i, v in enumerate(board):
            for j, m in enumerate(v):
                if m == word[0]:
                    ex = search(0, i, j, set())
                    if ex:
                        return ex
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.exist([
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ], "ABCCED"))

