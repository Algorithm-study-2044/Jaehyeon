class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        countdict = dict()
        rnums = []
        for num in nums:
            if num in countdict.keys():
                if countdict[num]!=4:
                    countdict[num] += 1
                    rnums.append(num)
            else:
                countdict[num] = 1
                rnums.append(num)

        sumdict = dict([])
        result = set([])
        n = len(rnums)

        for a in range(n):
            for b in range(a+1, n):
                sum = rnums[a]+rnums[b]
                if sum in sumdict.keys():
                    sumdict[sum].add((a,b))
                else:
                    sumdict[sum] = {(a,b)}
        
        for sum1 in sumdict.keys():
            sum2 = target - sum1
            if sum2 in sumdict.keys():
                for a, b in sumdict[sum1]:
                    for c, d in sumdict[sum2]:
                        ans = [rnums[a], rnums[b], rnums[c], rnums[d]]
                        ans.sort()
                        if b<c:
                            result.add(tuple(ans))
        
        result_ = []
        for n1, n2, n3, n4 in result:
            result_.append([n1, n2, n3, n4])
        
        return result_
