class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        """
        :type aliceSizes: List[int]
        :type bobSizes: List[int]
        :rtype: List[int]
        """
        bobSet = set(bobSizes)

        d = (sum(bobSizes)-sum(aliceSizes))//2
        for a in aliceSizes:
            b = a+d
            if b in bobSet:
                return [a,b]
        
            
