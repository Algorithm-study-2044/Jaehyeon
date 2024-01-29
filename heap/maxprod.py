import heapq
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_heap = []
        for num in nums:
            heapq.heappush(max_heap, -num)
        max1 = -max_heap[0]
        if len(max_heap)>2:
            max2 = max(-max_heap[1], -max_heap[2])
        else:
            max2 = -max_heap[1]
        return (max1-1)*(max2-1)