# Validate Stack Sequences

# Given two sequences pushed and popped with distinct values, return true if and only if this could have been the
# result of a sequence of push and pop operations on an initially empty stack.
#
#
#
# Example 1:
#
# Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
# Output: true
# Explanation: We might do the following sequence:
# push(1), push(2), push(3), push(4), pop() -> 4,
# push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
# Example 2:
#
# Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
# Output: false
# Explanation: 1 cannot be popped before 2.
#
#
# Constraints:
#
# 0 <= pushed.length == popped.length <= 1000
# 0 <= pushed[i], popped[i] < 1000
# pushed is a permutation of popped.
# pushed and popped have distinct values.
from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        l1 = len(pushed)
        l2 = len(popped)
        if l1 == l2:
            pid1 = 0
            pid2 = 0
            while pid1 < l1:
                if stack:
                    last = stack[-1]
                    if last == popped[pid2]:
                        stack.pop(-1)
                        pid2 += 1
                        continue
                stack.append(pushed[pid1])
                pid1 += 1

            if stack:
                while stack:
                    last = stack.pop(-1)
                    if last != popped[pid2]:
                        return False
                    pid2 += 1
            return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.validateStackSequences([1, 2, 3, 4, 5],
                                   [4, 3, 5, 2, 1]))
