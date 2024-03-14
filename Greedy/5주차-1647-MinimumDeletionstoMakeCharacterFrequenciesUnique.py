class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        d = dict()
        for c in s:
            d[c] = 1+ d.get(c, 0)
        freqarr = sorted(d.values(), reverse = True)
        ans = 0
        for idx in range(1, len(freqarr)):
            if freqarr[idx-1] <= freqarr[idx]:
                if freqarr[idx-1] > 0:
                    temp = freqarr[idx-1] - 1
                    ans += (freqarr[idx] - temp)
                    freqarr[idx] = temp
                else:
                    ans += freqarr[idx]
                    freqarr[idx] = 0
        return ans