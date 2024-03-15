class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        sums = [0]
        for num in nums:
            sums.append(sums[-1]+num)
        
        sidx = len(sums)-2
        eidx = len(sums)-1
        ans = sums[eidx] - sums[sidx]

        while sidx > 0:
            if sums[eidx] < sums[sidx]:
                eidx = sidx
            sidx -= 1
            ans = max(ans, sums[eidx]-sums[sidx])
        
        return ans