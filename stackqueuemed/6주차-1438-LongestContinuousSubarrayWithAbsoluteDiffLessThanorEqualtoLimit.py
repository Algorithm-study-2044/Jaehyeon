from collections import deque
class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        ans = 1
        ascq = deque([0])
        dscq = deque([0])
        leftidx = 0
        for idx in range(1, len(nums)):
            num = nums[idx]
            while ascq and nums[ascq[-1]] > num:
                ascq.pop()
            ascq.append(idx)
            while dscq and nums[dscq[-1]] < num:
                dscq.pop()
            dscq.append(idx)
            while nums[dscq[0]]-nums[ascq[0]] > limit:
                leftidx += 1
                if leftidx > dscq[0]:
                    dscq.popleft()
                if leftidx > ascq[0]:
                    ascq.popleft()
            ans = max(ans, idx - leftidx + 1)

        return ans