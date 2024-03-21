import random
class Solution(object):
    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.bndlst = [0]
        for wei in w:
            self.bndlst.append(self.bndlst[-1]+wei)

    def pickIndex(self):
        """
        :rtype: int
        """
        target = random.randint(0, self.bndlst[-1]-1)
        lidx = 0
        ridx = len(self.bndlst)-1
        while ridx-lidx > 1:
            midx = (lidx+ridx)//2
            if target < self.bndlst[midx]:
                ridx = midx
            else:
                lidx = midx
        
        return lidx


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()