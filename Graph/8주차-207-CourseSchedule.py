from collections import deque
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graphlst = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graphlst[a].append(b)
        q = deque()
        visited = [False for _ in range(numCourses)]

        def DFS(node):
            visited[node] = True
            for nextNode in graphlst[node]:
                if visited[nextNode] == False:
                    DFS(nextNode)
            q.appendleft(node)

        for v in range(numCourses):
            if visited[v] == False:
                DFS(v)
        
        orderlst = [0 for _ in range(numCourses)]
        for order in range(numCourses):
            orderlst[q[order]] = order
        
        for a, b in prerequisites:
            if orderlst[a] >= orderlst[b]:
                return False
        return True