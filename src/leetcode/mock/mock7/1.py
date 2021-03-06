# You have a set of tiles, where each tile has one letter tiles[i] printed on it.  Return the number of possible
# non-empty sequences of letters you can make.
#
#
#
# Example 1:
#
# Input: "AAB"
# Output: 8
# Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
# Example 2:
#
# Input: "AAABBC"
# Output: 188

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        s = set()
        for tile in tiles:
            if s:
                ts = s.copy()
                for v in s:
                    print(1)
                s = ts
            s.add(tile)
        return len(s)


if __name__ == '__main__':
    s = Solution()
    print(s.numTilePossibilities("AAB"))
