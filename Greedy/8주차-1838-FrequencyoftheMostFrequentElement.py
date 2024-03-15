from collections import deque
class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        min_val = min(nums)
        max_val = max(nums)
        count_arr = [0]*(max_val-min_val+1)
        for num in nums:
            count_arr[num-min_val] += 1
        sorted_arr = []
        for i, count in enumerate(count_arr):
            sorted_arr.extend([i+min_val]*count)
        nums = sorted_arr

        q = deque()
        sumq = 0
        ans = 0
        for idx in range(len(nums)):
            while nums[idx]*len(q)-sumq > k:
                sumq -= q.popleft()
            ans = max(ans, len(q)+1)
            sumq += nums[idx]
            q.append(nums[idx])
        return ans