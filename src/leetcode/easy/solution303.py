from typing import List


class NumArray:
    sums = {}

    def __init__(self, nums: List[int]):
        current_sum = 0
        for i in range(len(nums)):
            current_sum += nums[i]
            self.sums[i] = current_sum
            i += 1

    def sumRange(self, i: int, j: int) -> int:
        if i == 0:
            return self.sums[j]
        return self.sums[j] - self.sums[i - 1]


if __name__ == '__main__':
    s = NumArray([-2, 0, 3, -5, 2, -1])
