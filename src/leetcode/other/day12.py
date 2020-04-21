import json
from typing import List


class Solution:

    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            self.heap_add(heap, stone)
        length = len(heap)
        while length > 1:
            max1 = self.heap_remove(heap)
            max2 = self.heap_remove(heap)
            self.heap_add(heap, max1 - max2)
            if len(heap) == 1:
                break
        return heap[0]

    # 构建大顶堆
    def heap_add(self, heap: List[int], num: int) -> None:
        heap.append(num)
        idx = len(heap) - 1
        while idx > 0:
            parent_index = (idx - 1) // 2
            if heap[parent_index] < num:
                heap[parent_index], heap[idx] = heap[idx], heap[parent_index]
                idx = parent_index
            else:
                break

    # 移除堆顶元素
    def heap_remove(self, heap: List[int]) -> int:
        idx = len(heap) - 1
        # 堆顶元素与堆尾元素互换
        heap[idx], heap[0] = heap[0], heap[idx]
        result = heap.pop(idx)
        # 对堆进行整理
        self.heap_resort(heap, 0)
        return result

    # 对堆进行重新整理，使堆符合基本规则
    def heap_resort(self, heap: List[int], initial: int) -> None:
        length = len(heap)
        max_idx = initial * 2 + 1
        right = max_idx + 1
        if right < length:
            if heap[right] > heap[max_idx]:
                max_idx = right
            if heap[max_idx] > heap[initial]:
                heap[max_idx], heap[initial] = heap[initial], heap[max_idx]
                self.heap_resort(heap, max_idx)
        elif max_idx < length:
            if heap[max_idx] > heap[initial]:
                heap[max_idx], heap[initial] = heap[initial], heap[max_idx]
                self.heap_resort(heap, max_idx)


def stringToIntegerList(input):
    return json.loads(input)


def main():
    stones = stringToIntegerList('[1,2,3,4,19]')

    ret = Solution().lastStoneWeight(stones)

    out = str(ret);
    print(out)


if __name__ == '__main__':
    main()
