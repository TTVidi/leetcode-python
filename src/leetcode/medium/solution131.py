# Palindrome Partitioning


# Given a string s, partition s such that every substring of the partition is a palindrome.
#
# Return all possible palindrome partitioning of s.
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def check(check_str: str) -> bool:
            return check_str == check_str[::-1]

        res = []

        def helper(rest: str, path: List[str]):
            if rest == "":
                res.append(path)
                return
            for i in range(len(rest)):
                sub = rest[:i + 1]
                if check(sub):
                    copy = path.copy()
                    copy.append(sub)
                    helper(rest[i + 1:], copy)

        helper(s, [])
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.partition("aab"))
