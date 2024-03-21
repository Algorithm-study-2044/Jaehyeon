from collections import deque
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        #graphlst
        graphlst = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graphlst[a].append(b)

        # topological sort
        courselst = []
        visited = set()
        def DFS(node):
            visited.add(node)
            for nextnode in graphlst[node]:
                if nextnode not in visited:
                    DFS(nextnode)
            courselst.append(node)
        for v in range(numCourses):
            if v not in visited:
                DFS(v)
        
        orderlst = [0 for _ in range(numCourses)]
        for idx, v in enumerate(courselst):
            orderlst[v] = idx
        # check if cycle exist
        for u, v in prerequisites:
            if orderlst[u] < orderlst[v]:
                return []
        return courselst