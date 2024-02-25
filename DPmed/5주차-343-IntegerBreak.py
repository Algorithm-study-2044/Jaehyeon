class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = [0, 1, 1]
        for m in range(3, n+1):
            maxprod = 0
            for k in range(1, m):
                tmp = k*max(ans[m-k], m-k)
                if maxprod < tmp:
                    maxprod = tmp
            ans.append(maxprod)
        return ans[-1]