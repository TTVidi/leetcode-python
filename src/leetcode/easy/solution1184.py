# Distance Between Bus Stops

# A bus has n stops numbered from 0 to n - 1 that form a circle. We know the distance between all pairs of
# neighboring stops where distance[i] is the distance between the stops number i and (i + 1) % n.
#
# The bus goes along both directions i.e. clockwise and counterclockwise.
#
# Return the shortest distance between the given start and destination stops.
#
from typing import List


class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start > destination:
            start, destination = destination, start
        _sum = 0
        dis = 0
        for i in range(len(distance)):
            _sum += distance[i]
            if start <= i < destination:
                dis += distance[i]
        return min(dis, _sum - dis)


if __name__ == '__main__':
    s = Solution()
    print(s.distanceBetweenBusStops([1, 2, 3, 4], 3, 0))
