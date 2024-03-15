class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()

        spt = 0
        ans = 0

        for gpt in range(len(g)):
            while spt<len(s) and s[spt]<g[gpt]:
                spt += 1
            if spt < len(s):
                ans += 1
                spt += 1
        
        return ans