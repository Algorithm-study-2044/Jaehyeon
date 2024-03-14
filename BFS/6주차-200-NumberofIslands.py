from collections import deque
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        def available(i, j):
            return 0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j] == "1" and (i,j) not in visited
        def BFS(starti, startj):
            q = deque([(starti, startj)])
            visited.add((starti, startj))
            while q:
                i, j = q.popleft()
                if available(i-1, j):
                    visited.add((i-1, j))
                    q.append((i-1, j))
                if available(i+1, j):
                    visited.add((i+1, j))
                    q.append((i+1, j))
                if available(i, j-1):
                    visited.add((i, j-1))
                    q.append((i, j-1))
                if available(i, j+1):
                    visited.add((i, j+1))
                    q.append((i, j+1))
        
        islandcount = 0
        visited = set()
        for si in range(len(grid)):
            for sj in range(len(grid[0])):
                if available(si, sj):
                    islandcount += 1
                    BFS(si, sj)
        return islandcount