# Restore IP Addresses
# Given a string containing only digits, restore it by returning all possible valid IP address combinations.
#
# A valid IP address consists of exactly four integers (each integer is between 0 and 255) separated by single points.
#
# Example:
#
# Input: "25525511135"
# Output: ["255.255.11.135", "255.255.111.35"]
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def helper(rest: str, level: int, path: str):
            if level == 0:
                if rest == "":
                    path = path[:-1]
                    res.append(path)
                    return
            mi = level
            mx = level * 3
            length = len(rest)
            if mi <= length <= mx:
                i = 0
                while i < length and i < 3:
                    sub = rest[:i + 1]
                    k = int(sub)
                    if 0 <= k <= 255 and str(k) == sub:
                        p = path + sub + "."
                        helper(rest[i + 1:], level - 1, p)
                        i += 1
                    else:
                        return

        helper(s, 4, "")

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.restoreIpAddresses("25525511035"))
