class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        S = set(nums)
        S.discard(0)
        return len(S)