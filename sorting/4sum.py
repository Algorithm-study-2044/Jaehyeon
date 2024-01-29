class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n = len(nums)
        sumdict = dict([])
        result = set([])

        for a in range(n):
            for b in range(a+1, n):
                sum = nums[a]+nums[b]
                if sum in sumdict.keys():
                    sumdict[sum].add((a,b))
                else:
                    sumdict[sum] = {(a,b)}
        
        for sum1 in sumdict.keys():
            sum2 = target - sum1
            if sum2 in sumdict.keys():
                for a, b in sumdict[sum1]:
                    for c, d in sumdict[sum2]:
                        if b<c:
                            result.add((nums[a], nums[b], nums[c], nums[d]))
        
        result_ = []
        for n1, n2, n3, n4 in result:
            result_.append([n1, n2, n3, n4])
        
        return result_
