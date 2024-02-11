class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums)-1
        if nums[end] == target:
            return end
        while end-start>1:
            med = (end+start)//2
            if target>=nums[med]:
                start = med
            else:
                end = med
        if nums[start] == target:
            return start
        else:
            return -1