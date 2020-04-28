# First Unique Number

# You have a queue of integers, you need to retrieve the first unique integer in the queue.
#
# Implement the FirstUnique class:
#
# FirstUnique(int[] nums) Initializes the object with the numbers in the queue. int showFirstUnique() returns the
# value of the first unique integer of the queue, and returns -1 if there is no such integer. void add(int value)
# insert value to the queue.
#
#
from collections import OrderedDict
from typing import List


class FirstUnique:

    def __init__(self, nums: List[int]):
        self._list = nums
        self._set = set(nums)
        self._unique = OrderedDict()
        temp = {}
        for v in nums:
            if temp.get(v):
                temp[v] = temp[v] + 1
            else:
                temp[v] = 1

        for v in nums:
            if temp[v] == 1:
                self._unique[v] = 1

    def showFirstUnique(self) -> int:
        if self._unique:
            for k in self._unique.keys():
                return k
        return -1

    def add(self, value: int) -> None:
        if self._set.__contains__(value):
            if self._unique.get(value):
                self._unique.pop(value)
        else:
            self._unique[value] = 1
            self._set.add(value)
        return None


if __name__ == '__main__':
    f = FirstUnique([7, 7, 7, 7, 7, 7])
    print(f.showFirstUnique())
    f.add(7)
    f.add(3)
    f.add(3)
    f.add(7)
    f.add(17)
    print(f.showFirstUnique())
