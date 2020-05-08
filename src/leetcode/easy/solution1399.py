# Count Largest Group

# Given an integer n. Each number from 1 to n is grouped according to the sum of its digits.
#
# Return how many groups have the largest size.
import collections


class Solution:
    def countLargestGroup(self, n: int) -> int:
        res = []
        for i in range(1, n+1):
            res.append(sum(int(x) for x in str(i)))

        c = collections.Counter(res)
        x = [i for i in c.values() if i == max(c.values())]
        return len(x)


if __name__ == '__main__':
    s = Solution()
    print(s.countLargestGroup(10))
