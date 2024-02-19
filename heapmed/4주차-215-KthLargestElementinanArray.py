import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        maxheap = []
        for num in nums:
            heapq.heappush(maxheap, -num)
        for idx in range(k-1):
            heapq.heappop(maxheap)
        
        return -heapq.heappop(maxheap)