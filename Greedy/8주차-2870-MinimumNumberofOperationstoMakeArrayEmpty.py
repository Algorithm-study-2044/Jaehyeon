from collections import Counter
class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = Counter(nums)
        ans = 0

        for freq in cnt.values():
            if freq == 1:
                return -1
            elif freq%3 == 0:
                ans += freq//3
            else:
                ans += (freq//3 + 1)
        
        return ans