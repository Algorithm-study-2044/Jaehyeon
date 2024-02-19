class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        countdict = dict()
        for num in nums:
            countdict[num] = 1 + countdict.get(num, 0)
        freq = [[] for _ in range(len(nums))]
        for n, c in countdict.items():
            freq[len(nums)-c].append(n)
        
        ans = []
        idx = 0
        while len(ans) < k:
            ans += freq[idx]
            idx += 1
        
        return ans