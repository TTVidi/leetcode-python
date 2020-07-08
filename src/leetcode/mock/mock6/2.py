# Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique
# combinations in candidates where the candidate numbers sums to target.
#
# The same repeated number may be chosen from candidates unlimited number of times.
#
# Note:
#
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        result = []

        def combination(idx: int, rest: int, arr: List[int]):
            for i in range(idx, len(candidates)):
                candidate = candidates[i]
                if rest == candidate:
                    rs = arr.copy()
                    rs.append(candidate)
                    result.append(rs)
                    break
                if rest < candidate:
                    break
                if rest > candidate:
                    rs = arr.copy()
                    rs.append(candidate)
                    combination(i, rest - candidate, rs)

        combination(0, target, [])
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum([2, 3, 5], 8))
