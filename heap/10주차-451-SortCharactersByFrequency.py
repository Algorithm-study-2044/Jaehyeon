from collections import defaultdict
import heapq
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = []
        freqdict = defaultdict(int)
        for c in s:
            freqdict[c]+=1
        
        letterfreq = []

        for c, freq in freqdict.items():
            heapq.heappush(letterfreq, (-freq, c))
        
        while letterfreq:
            num, c = heapq.heappop(letterfreq)
            freq = -num
            ans.append(c*freq)
        
        return ''.join(ans)