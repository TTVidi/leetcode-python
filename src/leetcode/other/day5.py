# Best Time to Buy and Sell Stock II
# Say you have an array prices for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e.,
# buy one and sell one share of the stock multiple times).


# Note: You may not engage in multiple transactions at the same time
# (i.e., you must sell the stock before you buy again).
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sum = 0
        min_price = prices[0]
        for price in prices:
            if price > min_price:
                sum += (price - min_price)
                min_price = price
            else:
                min_price = price
        return sum


if __name__ == '__main__':
    s = Solution()
    arr = [7, 1, 5, 6]
    print(s.maxProfit(arr))
