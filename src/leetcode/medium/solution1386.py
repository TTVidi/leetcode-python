#  Cinema Seat Allocation

# A cinema has n rows of seats, numbered from 1 to n and there are ten seats in each row, labelled from 1 to 10 as
# shown in the figure above.
#
# Given the array reservedSeats containing the numbers of seats already reserved, for example, reservedSeats[i] = [3,
# 8] means the seat located in row 3 and labelled with 8 is already reserved.
#
# Return the maximum number of four-person groups you can assign on the cinema seats. A four-person group occupies
# four adjacent seats in one single row. Seats across an aisle (such as [3,3] and [3,4]) are not considered to be
# adjacent, but there is an exceptional case on which an aisle split a four-person group, in that case,
# the aisle split a four-person group in the middle, which means to have two people on each side.
from typing import List


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        unable_seats = set()
        uns = set()
        for v in reservedSeats:
            row = v[0]
            column = v[1]
            if column in (2, 3):
                uns.add(row)
                unable = (row, 1)
                unable_seats.add(unable)
            elif column in (4, 5):
                uns.add(row)
                unable1 = (row, 1)
                unable2 = (row, 2)
                unable_seats.add(unable1)
                unable_seats.add(unable2)
            elif column in (6, 7):
                uns.add(row)
                unable1 = (row, 2)
                unable2 = (row, 3)
                unable_seats.add(unable1)
                unable_seats.add(unable2)
            elif column in (8, 9):
                uns.add(row)
                unable = (row, 3)
                unable_seats.add(unable)
        total = n * 2
        un = 0

        for v in uns:
            first = (v, 1)
            second = (v, 2)
            third = (v, 3)
            temp = 0
            if first not in unable_seats:
                temp += 1
            if second not in unable_seats:
                temp += 1
            if third not in unable_seats:
                temp += 1
            if temp == 3:
                temp = 2
            elif temp == 2:
                temp = 1

            un += (2 - temp)

        return total - un


if __name__ == '__main__':
    s = Solution()
    print(s.maxNumberOfFamilies(4, [[4, 3], [1, 4], [4, 6], [1, 7]]))
