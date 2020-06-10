# You are given a string representing an attendance record for a student. The record only contains the following
# three characters: 'A' : Absent. 'L' : Late. 'P' : Present. A student could be rewarded if his attendance record
# doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).
#
# You need to return whether the student could be rewarded according to his attendance record.

class Solution:
    def checkRecord(self, s: str) -> bool:
        a_c = 0
        l_c = 0
        for c in s:
            if c == 'A':
                l_c = 0
                a_c += 1
                if a_c > 1:
                    return False
            if c == 'P':
                l_c = 0
            if c == 'L':
                l_c += 1
                if l_c > 2:
                    return False
        return True
