class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        countdict = dict()
        for num in arr:
            countdict[num] = countdict.get(num, 0)+1
        freqlst = list(countdict.values())
        freqlst.sort(reverse = True)
        count = 0
        while freqlst:
            count += freqlst[-1]
            if count > k:
                break
            freqlst.pop()
        return len(freqlst)
