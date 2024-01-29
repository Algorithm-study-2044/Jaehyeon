class Solution(object):
    def majorityElementCount(self, nums, startidx, lastidx):
        if startidx == lastidx:
            return [nums[startidx], 1]

        pair1 = self.majorityElementCount(nums, startidx, (startidx+lastidx)//2)
        pair2 = self.majorityElementCount(nums, (startidx+lastidx)//2+1, lastidx)

        if pair1 != None:
            for idx in range((startidx+lastidx)//2+1, lastidx+1):
                if nums[idx]== pair1[0]:
                    pair1[1] += 1
            if pair1[1]> (lastidx-startidx+1)//2:
                return pair1

        if pair2 != None:
            for idx in range(startidx, (startidx+lastidx)//2+1):
                if nums[idx]== pair2[0]:
                    pair2[1] += 1
            if pair2[1]> (lastidx-startidx+1)//2:
                return pair2

        return None

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return self.majorityElementCount(nums, 0, n-1)[0]
