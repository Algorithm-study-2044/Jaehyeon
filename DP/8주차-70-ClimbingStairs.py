class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        dp = [1, 2]
        for _ in range(n-2):
            dp.append(dp[-1]+dp[-2])
        return dp[-1]