class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0:
            return 0
        elif x==1:
            return 1
        else:
            left = 1
            right = x
            while right-left>1:
                med = (left+right)//2
                if med*med > x:
                    right = med
                else:
                    left = med
            return left
            