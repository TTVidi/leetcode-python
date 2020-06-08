# Coin Change 2

# You are given coins of different denominations and a total amount of money. Write a function to compute the number
# of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.
#
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}

        def find(m: int, c: List[int]) -> int:
            if m < 0:
                return 0
            if m == 0:
                return 1
            if c:
                x = c[len(c) - 1]
                key = (m, x)
                if key in dp:
                    return dp[key]
                if len(c) == 1:
                    if x > m:
                        dp[key] = 0
                    elif x == m:
                        dp[key] = 1
                    else:
                        dp[key] = find(m - x, c)
                    return dp[key]

                s = 0
                l = m
                l -= x
                if l == 0:
                    s += 1
                else:
                    while l > 0:
                        s += find(l, c)
                        l -= x
                temp = c.copy()
                temp.pop(-1)
                s += find(m, temp)
                dp[key] = s
                return s
            return 0

        return find(amount, coins)

    def change1(self, amount: int, coins: List[int]) -> int:
        dp = {}

        def find(m: int, c: List[int]) -> int:
            print(dp)
            idx = len(c) - 1
            current = c[idx]
            key = (current, m)
            if key in dp:
                return dp[key]
            if m < 0:
                dp[key] = 0
            elif m == 0:
                dp[key] = 1
            else:
                if c:
                    if idx == 0:
                        if m % current == 0:
                            dp[key] = 1
                        else:
                            dp[key] = 0
                        return dp[key]

                    # not contains current
                    temp = c.copy()
                    temp.pop(-1)
                    s = 0
                    if len(temp) > 0:
                        print("rest: ", m, temp)
                        s += find(m, temp)

                    # contains current
                    if m >= current:
                        m -= current
                        while m >= 0:
                            print(m, c)
                            s += find(m, c)
                            m -= current
                    dp[key] = s
                else:
                    dp[key] = 0
            return dp[key]

        return find(amount, coins)


if __name__ == '__main__':
    s = Solution()
    print(s.change1(5, [1, 2, 5]))
