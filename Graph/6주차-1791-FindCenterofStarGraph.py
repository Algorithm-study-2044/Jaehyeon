class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        
        graphlist = [set() for _ in range(n)]
        for u, v in edges:
            graphlist[u].add(v)
            graphlist[v].add(u)
        visitednodes = set()
        def DFS(s):
            visitednodes.add(s)
            if s == destination:
                return
            for c in graphlist[s]:
                if c not in visitednodes:
                    DFS(c)
        
        DFS(source)
        return destination in visitednodes