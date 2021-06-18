import heapq
        
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone) #max heap
        while len(heap)>1:
            result = heapq.heappop(heap)-heapq.heappop(heap)
            if result !=0:
                heapq.heappush(heap,result)
        return 0 if len(heap)==0 else -heap[0]
