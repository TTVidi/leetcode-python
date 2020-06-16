# Final Prices With a Special Discount in a Shop

# Given the array prices where prices[i] is the price of the ith item in a shop. There is a special discount for
# items in the shop, if you buy the ith item, then you will receive a discount equivalent to prices[j] where j is the
# minimum index such that j > i and prices[j] <= prices[i], otherwise, you will not receive any discount at all.
#
# Return an array where the ith element is the final price you will pay for the ith item of the shop considering the
# special discount.
#
#
#
from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        length = len(prices)

        def find(idx: int) -> int:
            v = prices[idx]
            idx += 1
            while idx < length:
                if prices[idx] <= v:
                    return prices[idx]
                idx += 1
            return 0

        for i, j in enumerate(prices):
            prices[i] = prices[i] - find(i)
        return prices
