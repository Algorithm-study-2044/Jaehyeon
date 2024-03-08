class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        m = arr[0]
        M = arr[-1]
        n = len(arr)
        if x<=m:
            return arr[:k]
        if x>=M:
            return arr[n-k:]
        diffarr = [0 for _ in range(m, M+1)]
        for num in arr:
            diffarr[num-m] += 1
        diff = 0
        count = diffarr[x-m]
        while count < k:
            diff += 1
            if x-m-diff >= 0:
                count += diffarr[x-m-diff]
                if count >=k:
                    diffarr[x-m-diff] -= (count-k)
            else:
                return arr[:k]
            if x-m+diff < len(diffarr):
                count += diffarr[x-m+diff]
            else:
                return arr[n-k:]
        
        idx = x-m-diff
        ans = []
        while True:
            if len(ans) == k:
                break
            for _ in range(diffarr[idx]):
                if len(ans) == k:
                    break
                ans.append(idx+m)
            idx += 1
        return ans
