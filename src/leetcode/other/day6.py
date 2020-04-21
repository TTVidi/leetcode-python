# Group Anagrams
# Given an array of strings, group anagrams together.
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        di = {}
        for s in strs:
            temp = self.sortedStr(s)
            li = []
            if di.__contains__(temp):
                li = di[temp]
            li.append(s)
            di[temp] = li
        return list(di.values())

    def sortedStr(self, s: str) -> str:
        arr = [0] * 26
        for c in s:
            arr[ord(c) - 97] = arr[ord(c) - 97] + 1
        result = ""
        i = 0
        while i < len(arr):
            while arr[i] > 0:
                result += chr(97 + i)
                arr[i] = arr[i] - 1
            i += 1
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
