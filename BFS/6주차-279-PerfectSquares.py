class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr = [0 for _ in range(n+1)]
        def minsquaresnum(m):
            if m == 0:
                return 0
            k = 1
            minnum = 999999999999999
            while k**2 <= m:
                if m-k**2>0 and arr[m-k**2] == 0:
                    arr[m-k**2] = minsquaresnum(m-k**2)
                if arr[m-k**2]+1 < minnum:
                    minnum = arr[m-k**2]+1
                k += 1
            return minnum
        
        return minsquaresnum(n)
