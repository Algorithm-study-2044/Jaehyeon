class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        bit_num = [[] for _ in range(14)]
        for x in arr:
            bit_num[bin(x).count('1')].append(x)
        result = []
        for a in bit_num:
            a.sort()
            result += a
        return result