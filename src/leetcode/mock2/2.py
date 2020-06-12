# Your friend is typing his name into a keyboard.  Sometimes, when typing a character c, the key might get long
# pressed, and the character will be typed 1 or more times.
#
# You examine the typed characters of the keyboard.  Return True if it is possible that it was your friends name,
# with some characters (possibly none) being long pressed.
#
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        j = 0
        c = name[0]
        while i < len(name) and j < len(typed):
            if name[i] != typed[j]:
                return False
            c_i = i
            c_j = j
            while i < len(name) and name[i] == c:
                i += 1
            while j < len(typed) and typed[j] == c:
                j += 1
            if i - c_i > j - c_j:
                return False
            if i < len(name):
                c = name[i]

        if i < len(name) or j < len(typed):
            return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isLongPressedName("alex",
                              "alexxr"))
