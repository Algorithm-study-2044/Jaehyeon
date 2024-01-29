class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        alphadict = dict([])
        for c in s:
            if c in alphadict.keys():
                alphadict[c] = False
            else:
                alphadict[c] = True
        for idx, c in enumerate(s):
            if c in alphadict.keys() and alphadict[c]:
                return idx
        return -1