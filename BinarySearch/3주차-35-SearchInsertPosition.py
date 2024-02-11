class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums)-1
        if target<=nums[start]:
            return start
        elif target> nums[end]:
            return end+1
        else:
            while end-start>1:
                med = (start+end)//2
                if target <= nums[med]:
                    end = med
                else:
                    start = med
            return end