# Coin Change

# You are given coins of different denominations and a total amount of money amount. Write a function to compute the
# fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any
# combination of the coins, return -1.
#
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        return 1


if __name__ == '__main__':
    s = Solution()
    print(s.coinChange([1, 2, 5]))
