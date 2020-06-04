# Partition Labels

# A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that
# each letter appears in at most one part, and return a list of integers representing the size of these parts.
#
from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        chr_list = [[-1, -1] for i in range(26)]
        i = 0
        j = len(S)
        while i < j:
            idx = ord(S[i]) - 97
            arr = chr_list[idx]
            if arr[0] == -1:
                arr[0] = i
            arr[1] = i
            i += 1

        def find_end_idx(c: chr) -> List[int]:
            return chr_list[ord(c) - 97]

        rs = []
        i = 0
        while i < j:
            arr = find_end_idx(S[i])
            begin = arr[0]
            end = arr[1]
            k = begin + 1
            while k <= end:
                current_arr = find_end_idx(S[k])
                if current_arr[1] > end:
                    end = current_arr[1]
                k += 1
            rs.append(end - begin + 1)
            i = end + 1
        return rs


if __name__ == '__main__':
    s = Solution()
    print(s.partitionLabels("ababcbacadefegdehijhklij"))
