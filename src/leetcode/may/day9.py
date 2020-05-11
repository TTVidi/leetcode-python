# Valid Perfect Square

# Given a positive integer num, write a function which returns True if num is a perfect square else False.
#
# Note: Do not use any built-in library function such as sqrt.

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 0 or num == 1:
            return True
        for i in range((num >> 1) + 1):
            if i * i == num:
                return True
            if i * i > num:
                return False
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.isPerfectSquare(2))
