class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        freqdict = dict()
        for c in s:
            freqdict[c] = freqdict.get(c, 0)+1
        freqset = set()
        ans = 0
        for c, freq in freqdict.items():
            for idx in range(26):
                if freq-idx not in freqset:
                    ans += idx
                    if freq-idx>0:
                        freqset.add(freq-idx)
                    break
        return ans