# Increasing Decreasing String

# Given a string s. You should re-order the string using the following algorithm:
#
# Pick the smallest character from s and append it to the result. Pick the smallest character from s which is greater
# than the last appended character to the result and append it. Repeat step 2 until you cannot pick more characters.
# Pick the largest character from s and append it to the result. Pick the largest character from s which is smaller
# than the last appended character to the result and append it. Repeat step 5 until you cannot pick more characters.
# Repeat the steps from 1 to 6 until you pick all characters from s. In each step, If the smallest or the largest
# character appears more than once you can choose any occurrence and append it to the result.
#
# Return the result string after sorting s with this algorithm.

class Solution:
    def sortString(self, s: str) -> str:
        result = ""
        map = {}
        for c in s:
            if map.get(c):
                map[c] = map[c] + 1
            else:
                map[c] = 1
        count = 0
        while count != len(s):
            i = 0
            while i < 26:
                c = chr(int(i) + 97)
                if map.get(c) and map[c] > 0:
                    map[c] = map[c] - 1
                    count += 1
                    result += c
                i += 1

            while i >= 0:
                c = chr(int(i) + 97)
                if map.get(c) and map[c] > 0:
                    map[c] = map[c] - 1
                    count += 1
                    result += c
                i -= 1
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.sortString("aaaabbbbcccc"))
