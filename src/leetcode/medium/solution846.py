# Hand of Straights

# Alice has a hand of cards, given as an array of integers.
#
# Now she wants to rearrange the cards into groups so that each group is size W, and consists of W consecutive cards.
#
# Return true if and only if she can.
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if hand:
            l = len(hand)
            if W * W == l:
                return 1
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.isNStraightHand([1, 2, 3, 4, 5, 3, 4, 2, 3, ], 3))
