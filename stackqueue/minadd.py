class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        unValidOpenCount = 0
        unValidClosedCount = 0
        for c in s:
            if c == '(':
                unValidOpenCount += 1
            else:
                if unValidOpenCount >0:
                    unValidOpenCount -= 1
                else:
                    unValidClosedCount += 1
        return unValidOpenCount + unValidClosedCount