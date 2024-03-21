class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        q = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))

        if len(q) == 0:
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        return -1
            return 0
        
        
        ans = 0
        while q:
            ans += 1
            q_ = []
            for i, j in q:
                if i-1>=0 and grid[i-1][j]==1:
                    grid[i-1][j] = 2
                    q_.append((i-1, j))
                if i+1<m and grid[i+1][j] == 1:
                    grid[i+1][j] = 2
                    q_.append((i+1, j))
                if j-1>=0 and grid[i][j-1]==1:
                    grid[i][j-1] = 2
                    q_.append((i, j-1))
                if j+1<n and grid[i][j+1] == 1:
                    grid[i][j+1] = 2
                    q_.append((i, j+1))
            q = q_

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        
        return ans-1