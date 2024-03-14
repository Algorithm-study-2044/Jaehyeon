class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        ans = 0
        arr.append(0)
        stack = []
        lbound = -1
        for rbound, r in enumerate(arr):
            while stack and arr[stack[-1]] > r:
                midx = stack.pop()
                if stack:
                    lbound = stack[-1]
                else:
                    lbound = -1
                ans = (ans + arr[midx]*(midx-lbound)*(rbound-midx))%(10**9+7)
            stack.append(rbound)
        
        return ans