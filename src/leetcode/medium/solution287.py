# Find the Duplicate Number


# Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at
# least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.
#
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = 2 ** (len(nums)) - 1
        for x in nums:
            p = 2 ** x
            if ((p & s) == 0):
                return x
            s = s - p
        return s

    def findDuplicate1(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        # 快慢指针
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if (slow == fast): break
        slow = nums[0]
        while (slow != fast):
            slow = nums[slow]
            fast = nums[fast]
        return slow

    """
    [1, 3, 4, 2, 2]
     1 -3 -4 -2 -2
     
     [3, 1, 3, 4, 2]
      3 -1     -4
    """

    def findDuplicate2(self, nums: List[int]) -> int:
        dup = -1
        for i in range(len(nums)):
            idx = abs(nums[i])
            if nums[idx] < 0:
                return idx
            else:
                nums[idx] *= -1
        return -1

    def findDuplicate3(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        fast = nums[0]
        while slow != fast:
            fast = nums[fast]
            slow = nums[slow]
        return slow

    def findDuplicate4(self, nums: List[int]) -> int:
        right = len(nums)
        left = 1
        while left < right:
            middle = (left + right) >> 1
            count = 0
            for c in nums:
                if c <= middle:
                    count += 1
            if count <= middle:
                left = middle + 1
            else:
                right = middle
        return right


if __name__ == '__main__':
    s = Solution()
    print(s.findDuplicate4([1, 3, 4, 2, 2]))
