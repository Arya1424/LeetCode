import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        heap=[]
        for i in nums:
            heapq.heappush(heap, i)
            if len(heap)>k:
                heapq.heappop(heap)
        return heap[0]
        