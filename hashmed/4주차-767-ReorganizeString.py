class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        alphadict = dict()
        n = len(s)
        for c in s:
            if c in alphadict.keys():
                alphadict[c] += 1
            else:
                alphadict[c] = 1
        for c in alphadict.keys():
            if alphadict[c] > (n+1)//2:
                return ""
        anslst = ['' for _ in range(n)]
        sorted_items = sorted(alphadict.items(), key=lambda item: item[1], reverse=True)
        idx = 0
        for c, count in sorted_items:
            for _ in range(count):
                anslst[idx] = c
                idx += 2
                if idx >= n:
                    idx = 1
        
        ans = ''.join(anslst)
        return ans