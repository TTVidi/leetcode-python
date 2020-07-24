# Binary Subarrays With Sum

# In an array A of 0s and 1s, how many non-empty subarrays have sum S?
#
#
#
# Example 1:
#
# Input: A = [1,0,1,0,1], S = 2
# Output: 4
# Explanation:
# The 4 subarrays are bolded below:
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
#
#
# Note:
#
# A.length <= 30000
# 0 <= S <= A.length
# A[i] is either 0 or 1.
from typing import List


class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        count = res = left = 0
        for right in range(len(A)):
            S -= A[right]
            if A[right] == 1:
                count = 0
            while left <= right and S <= 0:
                if S == 0:
                    count += 1
                S += A[left]
                left += 1
            res += count
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.numSubarraysWithSum([0, 0, 0, 0, 1]
                                , 2))
