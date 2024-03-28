class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        S = set(nums)

        ans = 0
        for num in nums:
            if num-1 not in S:
                n = num+1
                while n in S:
                    n += 1
                if ans < n - num:
                    ans = n - num

        return ans