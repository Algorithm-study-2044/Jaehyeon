import heapq
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        #neighbor
        graphlst = [[] for _ in range(n)]
        for fromnode, tonode, price in flights:
            graphlst[fromnode].append((tonode, price))
        distlst = [[10**6 for _ in range(k+2)] for __ in range(n)]
        distlst[src][0] = 0

        #Dijkstra
        q = [(0, 0, src)]
        while q:
            u_cost, u_move, u = heapq.heappop(q)
            if u_move <= k:
                for v, w_uv in graphlst[u]:
                    cost = u_cost+w_uv
                    v_cost = distlst[v][u_move+1]
                    if cost < v_cost:
                        distlst[v][u_move+1] = cost
                        heapq.heappush(q, (cost, u_move+1, v))
        
        ans = min(distlst[dst])
        if ans == 10**6:
            return -1
        else:
            return ans