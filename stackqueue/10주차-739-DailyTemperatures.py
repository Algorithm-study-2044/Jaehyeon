from collections import deque
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        dscs = [0]
        n = len(temperatures)
        ans = [0 for _ in range(n)]

        for idx in range(1, n):
            temp = temperatures[idx]
            while dscs:
                lasttemp = temperatures[dscs[-1]]
                if lasttemp < temp:
                    idx_ = dscs.pop()
                    ans[idx_] = idx-idx_
                else:
                    break
            dscs.append(idx)
        
        return ans
