import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = []
        for i in nums:
            if len(heap) != k:
                heapq.heappush(heap,i)
            elif i > heap[0]:
                heapq.heapreplace(heap, i)
        return heapq.heappop(heap)