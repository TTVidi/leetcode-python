# Prime Arrangements

# Return the number of permutations of 1 to n so that prime numbers are at prime indices (1-indexed.)
#
# (Recall that an integer is prime if and only if it is greater than 1, and cannot be written as a product of two
# positive integers both smaller than it.)
#
# Since the answer may be large, return the answer modulo 10^9 + 7.
#

class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        import math
        def checkprime(n, lis):
            for i in lis:
                if n % i == 0:
                    return False
            return True

        def numberofprime(n):
            count = 0
            lis = []
            for i in range(2, n + 1):
                if checkprime(i, lis):
                    lis.append(i)
                    count += 1

            return count

        count = numberofprime(n)

        return (math.factorial(count) * math.factorial(n - count)) % (10 ** 9 + 7)


if __name__ == '__main__':
    s = Solution()
    print(s.numPrimeArrangements(5))
