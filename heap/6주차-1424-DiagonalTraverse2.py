class Solution(object):
    def findDiagonalOrder(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        m = len(nums)
        n = max([len(arr) for arr in nums])
        ans = []
        diagarr = [[] for _ in range(m+n-1)]
        for i, arr in enumerate(nums):
            for j, num in enumerate(arr):
                diagarr[i+j].append(num)
        
        for arr in diagarr:
            while arr:
                ans.append(arr.pop())
        
        return ans