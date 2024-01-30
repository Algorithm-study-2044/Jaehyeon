class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        mincost = [cost[0], cost[1]]
        n = len(cost)
        for idx in range(2, n):
            mincost.append(cost[idx]+min(mincost[-1], mincost[-2]))
        return min(mincost[-1], mincost[-2])
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))