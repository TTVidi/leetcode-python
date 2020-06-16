# Find Smallest Letter Greater Than Target

# Given a list of sorted characters letters containing only lowercase letters, and given a target letter target,
# find the smallest element in the list that is larger than the given target.
#
# Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.
from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        def find_idx(left: int, right: int):
            if target < letters[left]:
                return left
            if target > letters[right]:
                return right + 1
            if left == right:
                return left + 1
            middle = (left + right) >> 1
            if letters[middle] > target:
                return find_idx(left, middle - 1)
            if letters[middle] <= target:
                return find_idx(middle + 1, right)

        idx = find_idx(0, len(letters) - 1)
        if idx < len(letters):
            return letters[idx]
        return letters[0]


if __name__ == '__main__':
    s = Solution()
    print(s.nextGreatestLetter(["c", "f", "j"], "k"))
