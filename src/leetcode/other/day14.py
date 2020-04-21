# Perform String Shifts You are given a string s containing lowercase English letters, and a matrix shift,
# where shift[i] = [direction, amount]:
#
# direction can be 0 (for left shift) or 1 (for right shift).
# amount is the amount by which string s is to be shifted.
# A left shift by 1 means remove the first character of s and append it to the end.
# Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.
# Return the final string after all operations.
from typing import List


class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        li = list(s)
        for op in shift:
            amount = op[1]
            if op[0] == 1:
                while amount > 0:
                    pop = li.pop(-1)
                    li.insert(0, pop)
                    amount -= 1
            else:
                while amount > 0:
                    pop = li.pop(0)
                    li.append(pop)
                    amount -= 1
            print(li)
        return "".join(li)


if __name__ == '__main__':
    s = Solution()
    print(s.stringShift("abcdefg", [[1,1],[1,1],[0,2],[1,3]]))
