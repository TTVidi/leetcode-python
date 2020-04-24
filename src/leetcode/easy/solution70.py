# Climbing Stairs

# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
# Note: Given n will be a positive integer.

class Solution:
    di = {1: 1, 2: 2}

    def climbStairs(self, n: int) -> int:
        if self.di.get(n):
            return self.di[n]
        self.di[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.di[n]

    def climbStairs2(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2
        li = [1, 2]
        i = 2
        while i < n:
            li.append(li[i - 1] + li[i - 2])
            i += 1
        return li.pop()


if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs2(6))
