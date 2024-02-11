class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        start = 0
        end = len(nums)-1
        if nums[end] == end:
            return end+1
        elif nums[0] == 1:
            return 0
        while end-start>1:
            med = (end+start)//2
            if nums[med] == med:
                start = med
            else:
                end = med
        return end