# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        lidx = 0
        ridx = n
        while ridx-lidx > 1:
            midx = (lidx+ridx)//2
            if isBadVersion(midx):
                ridx = midx
            else:
                lidx = midx
        return ridx