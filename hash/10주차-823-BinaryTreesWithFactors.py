from collections import defaultdict
class Solution(object):
    def numFactoredBinaryTrees(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr.sort()
        S = set(arr)
        n = len(arr)
        childdict = defaultdict(list)
        # childlst[c] 에는 c의 child가 될 수 있는 것들의 순서쌍 저장할 예정

        for k in range(1, n):
            c = arr[k]
            for i in range(k):
                a = arr[i]
                if c%a == 0:
                    b = c//a
                    if b in S:
                        childdict[c].append((a,b))

        dpdict = defaultdict(int)
        # dpdict[c]에는 c를 root로 하는 tree 개수 저장할 예정

        N = 10**9 + 7
        for k in range(n):
            c = arr[k]
            dpdict[c] += 1
            for a, b in childdict[c]:
                dpdict[c] = (dpdict[c]+dpdict[a]*dpdict[b])% N
        
        ans = 0
        for v in dpdict.values():
            ans = (ans + v)% N
        return ans