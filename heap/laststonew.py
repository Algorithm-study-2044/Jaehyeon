import heapq
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        max_heap = [-x for x in stones]
        heapq.heapify(max_heap)

        while True:
            if len(max_heap) == 1:
                return -max_heap[0]
            elif len(max_heap) == 0:
                return 0
            else:
                x = heapq.heappop(max_heap)
                y = heapq.heappop(max_heap)
                if x<y:
                    heapq.heappush(max_heap, x-y)
