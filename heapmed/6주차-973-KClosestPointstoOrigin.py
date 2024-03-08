import heapq
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        distpoints = []
        for pt in points:
            distpt = [pt[0]**2+pt[1]**2, pt]
            distpoints.append(distpt)
        heapq.heapify(distpoints)
        ans = []
        for _ in range(k):
            d, pt = heapq.heappop(distpoints)
            ans.append(pt)
        return ans