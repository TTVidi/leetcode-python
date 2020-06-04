# Target Sum

# You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -.
# For each integer, you should choose one from + and - as its new symbol.
#
# Find out how many ways to assign symbols to make sum of integers equal to target S.
#
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        def initial(x: int, di: dict) -> dict:
            temp = {}
            for k in di.keys():
                next = k + x
                pre = k - x
                if next in temp:
                    temp[next] = temp[next] + di[k]
                else:
                    temp[next] = di[k]
                if pre in temp:
                    temp[pre] = temp[pre] + di[k]
                else:
                    temp[pre] = di[k]
            return temp

        di = {nums[0]: 1, -nums[0]: 1}
        if nums[0] == 0:
            di = {0: 2}

        for i in range(1, len(nums)):
            di = initial(nums[i], di)

        if S in di:
            return di[S]
        return 0


if __name__ == '__main__':
    s = Solution()
    print(s.findTargetSumWays([0, 0, 0, 0, 0, 0, 0, 0, 1]
                              , 1))
