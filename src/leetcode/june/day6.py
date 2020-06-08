# Queue Reconstruction by Height

# Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h,
# k), where h is the height of the person and k is the number of people in front of this person who have a height
# greater than or equal to h. Write an algorithm to reconstruct the queue.
# Input:
# [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
#
# Output:
# [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
# Note:
# The number of people is less than 1,100.
#
from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (x[0], -x[1]), reverse=True)
        li = []
        for k in people:
            if li:
                li.insert(k[1], k)
            else:
                li.append(k)
        return li


if __name__ == '__main__':
    s = Solution()
    print(s.reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))
