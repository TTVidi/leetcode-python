#  Find K Pairs with Smallest Sums

# You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.
#
# Define a pair (u,v) which consists of one element from the first array and one element from the second array.
#
# Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        l1 = len(nums1)
        l2 = len(nums2)
        if l1 >= k:
            nums1 = nums1[:k]
        if l2 >= k:
            nums2 = nums2[:k]
        from queue import PriorityQueue
        pq = PriorityQueue()
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if pq.qsize() == k:
                    current = pq.get()
                    current_max = current[0] * -1
                    if nums1[i] + nums2[j] >= current_max:
                        pq.put(current)
                        break
                pq.put(((nums1[i] + nums2[j]) * -1, (nums1[i], nums2[j])))

        li = []
        while not pq.empty():
            c = pq.get()
            li.insert(0, [c[1][0], c[1][1]])
        return li


if __name__ == '__main__':
    s = Solution()
    print(s.kSmallestPairs([1, 7, 11], [2, 4, 6], 3))
