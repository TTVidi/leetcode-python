# Flood Fill

# An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0
# to 65535).
#
# Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value
# newColor, "flood fill" the image.
#
# To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting
# pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with
# the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the
# newColor.
#
# At the end, return the modified image.
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        r = len(image)
        c = len(image[0])

        color = image[sr][sc]
        _set = set()

        def fill(i: int, j: int):
            k = str(i) + "," + str(j)
            if not _set.__contains__(k):
                image[i][j] = newColor
                _set.add(k)
                if i - 1 >= 0 and image[i - 1][j] == color:
                    image[i - 1][j] = newColor
                    fill(i - 1, j)
                if i + 1 < r and image[i + 1][j] == color:
                    image[i + 1][j] = newColor
                    fill(i + 1, j)
                if j - 1 >= 0 and image[i][j - 1] == color:
                    image[i][j - 1] = newColor
                    fill(i, j - 1)
                if j + 1 < c and image[i][j + 1] == color:
                    image[i][j + 1] = newColor
                    fill(i, j + 1)

        fill(sr, sc)
        return image


if __name__ == '__main__':
    s = Solution()
    print(s.floodFill([[0, 1, 1], [0, 1, 1]],
                      1,
                      1,
                      2))
