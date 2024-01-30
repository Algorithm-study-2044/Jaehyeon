import math
class Solution(object):
    def countBitswithlog2n(self, m):
        if m == 0:
            return [0]
        elif m == 1:
            return [0,1]
        else:
            arr = self.countBitswithlog2n(m-1)
            arr2 = [x+1 for x in arr]
            return arr+arr2
        
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        m = 0
        x = 1
        while x<=n:
            m += 1
            x *= 2

        arr = self.countBitswithlog2n(m)
        return arr[:n+1]
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.countBits(15))