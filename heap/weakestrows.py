class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        m = len(mat)
        n = len(mat[0])
        delidxset = set([])
        result = []
        for j in range(n):
            for i in range(m):
                if not i in delidxset and not mat[i][j]:
                    delidxset.add(i)
                    result.append(i)
                    if len(result) == k:
                        return result