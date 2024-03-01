class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        prevnodelst = [set() for _ in range(n+1)]
        nextnodelst = [set() for _ in range(n+1)]
        for s, e in trust:
            prevnodelst[e].add(s)
            nextnodelst[s].add(e)
        
        for e in range(1, n+1):
            if len(prevnodelst[e]) == n-1 and len(nextnodelst[e]) == 0:
                return e
        return -1