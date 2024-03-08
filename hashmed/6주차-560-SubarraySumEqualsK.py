class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        freqdict = dict()
        freqdict[0] = 1
        partialsum = 0
        ans = 0
        for num in nums:
            partialsum += num
            ans += freqdict.get(partialsum-k, 0)
            freqdict[partialsum] = freqdict.get(partialsum, 0) + 1
        return ans