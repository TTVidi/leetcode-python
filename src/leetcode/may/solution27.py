# Possible Bipartition
# Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.
#
# Each person may dislike some other people, and they should not go into the same group.
#
# Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.
#
# Return true if and only if it is possible to split everyone into two groups in this way.
#
#
import collections
from typing import List


class Solution:
    def possibleBipartition1(self, N: int, dislikes: List[List[int]]) -> bool:
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        graph = collections.defaultdict(list)
        for dislike in dislikes:
            graph[dislike[0] - 1].append(dislike[1] - 1)
            graph[dislike[1] - 1].append(dislike[0] - 1)
        color = [0] * N
        for i in range(N):
            if color[i] != 0: continue
            bfs = collections.deque()
            bfs.append(i)
            color[i] = 1
            while bfs:
                cur = bfs.popleft()
                for e in graph[cur]:
                    if color[e] != 0:
                        if color[cur] == color[e]:
                            return False
                    else:
                        color[e] = -color[cur]
                        bfs.append(e)
        return True

    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        di = {}
        for i, v in enumerate(dislikes):
            cur = v[0]
            dis = v[1]
            if cur in di:
                di[cur].append(dis)
            else:
                di[cur] = [dis]

            if dis in di:
                di[dis].append(cur)
            else:
                di[dis] = [cur]

        noCircleSet = set()

        def circled(li: List[int], k: int) -> bool:
            if k in noCircleSet:
                return False
            length = len(li)
            temp = li
            if length >= 3:
                temp = li[-3:]
            if k in temp:
                return True
            else:
                if k in di:
                    li.append(k)
                    if length >= 3:
                        temp = li[-3:]
                    for l in di[k]:
                        if l == temp[0]:
                            return True
                        if l not in li:
                            if circled(li, l):
                                print(li, l, True)
                                return True
                            else:
                                print(li, l, False)
                    li.pop(-1)
                noCircleSet.add(k)
                return False

        for i, v in di.items():
            if circled([], i):
                return False

        return True


if __name__ == '__main__':
    s = Solution()
    # print(s.possibleBipartition(6,
    #                             [[1, 2], [1, 3], [2, 4], [3, 4], [1, 5], [2, 6], [5, 6]]))
    print(s.possibleBipartition(3,
                                [[1, 2], [1, 3], [2, 3]]))
    print(s.possibleBipartition(4,
                                [[1, 2], [1, 3], [2, 4]]))
