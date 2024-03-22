from collections import deque
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        
        arrwithidx = [(matrix[i][j], i, j) for j in range(n) for i in range(m)]
        arrwithidx.sort()

        dp = [[1 for _ in range(n)] for __ in range(m)]
        for val, curri, currj in arrwithidx:
            newcnt = dp[curri][currj]
            if curri-1>=0 and matrix[curri-1][currj] < val:
                newcnt = max(newcnt, dp[curri-1][currj]+1)
            if curri+1<m and matrix[curri+1][currj] < val:
                newcnt = max(newcnt, dp[curri+1][currj]+1)
            if currj-1>=0 and matrix[curri][currj-1] < val:
                newcnt = max(newcnt, dp[curri][currj-1]+1)
            if currj+1<n and matrix[curri][currj+1] < val:
                newcnt = max(newcnt, dp[curri][currj+1]+1)
            dp[curri][currj] = newcnt

        ans = 1
        for i in range(m):
            for j in range(n):
                ans = max(ans, dp[i][j])
        return ans