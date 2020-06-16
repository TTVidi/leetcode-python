# Excel Sheet Column Title

# Given a positive integer, return its corresponding column title as appear in an Excel sheet.

class Solution:
    def convertToTitle(self, n: int) -> str:
        heap = []
        while n >= 26:
            heap.append(n % 26)
            n = (n // 26)
        heap.append(n)
        b = 0
        for i in range(len(heap)):
            if heap[i] - b <= 0:
                heap[i] = (heap[i] - b + 26)
                b = 1
            else:
                heap[i] = heap[i] - b
        if len(heap) > 1:
            v = heap.pop(-1)
            if v != 26:
                heap.append(v)

        rs = ""
        while heap:
            rs += chr(heap.pop(-1) + 64)
        return rs


if __name__ == '__main__':
    s = Solution()
    print(s.convertToTitle(28))
