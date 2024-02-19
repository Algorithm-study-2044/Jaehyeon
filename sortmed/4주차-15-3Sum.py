class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if i>0 and nums[i-1] == nums[i]:
                continue
            target = -nums[i]
            j = i+1
            k = len(nums)-1
            while j<k:
                if nums[j] + nums[k] > target:
                    k -= 1
                elif nums[j] + nums[k] < target:
                    j += 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j-1] == nums[j]:
                        j += 1
                    
        return ans