# Insert Delete GetRandom O(1)

# Design a data structure that supports all following operations in average O(1) time.
#
# insert(val): Inserts an item val to the set if not already present. remove(val): Removes an item val from the set
# if present. getRandom: Returns a random element from current set of elements. Each element must have the same
# probability of being returned.


class RandomizedSet:

    def __init__(self):
        self.map = dict()
        self.se = set()
        """
        Initialize your data structure here.
        """

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if not self.map.__contains__(val):
            self.map[val] = 1
            self.se.add(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if self.map.__contains__(val):
            self.map.pop(val)
            self.se.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        k = self.se.pop()
        self.se.add(k)
        return self.map[k]


if __name__ == '__main__':
    r = RandomizedSet()
    print(r.insert(1))
    print(r.insert(2))
    print(r.insert(2))
    print(r.remove(1))
    print(r.getRandom())
