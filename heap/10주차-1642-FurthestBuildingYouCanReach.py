import heapq
class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        """
        :type heights: List[int]
        :type bricks: int
        :type ladders: int
        :rtype: int
        """
        n = len(heights)
        usedbricks = 0
        usedladders = []
        for i in range(n-1):
            if heights[i+1] > heights[i]:
                diff = heights[i+1]-heights[i]
                if len(usedladders) < ladders:
                    heapq.heappush(usedladders, diff)
                else:
                    usedbricks += heapq.heappushpop(usedladders, diff)
            if usedbricks > bricks:
                return i
        return n-1