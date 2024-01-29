class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        occurdict = dict([])
        for val in arr:
            if val in occurdict.keys():
                occurdict[val] += 1
            else:
                occurdict[val] = 1

        occurset = set([])
        for occur in occurdict.values():
            if occur in occurset:
                return False
            occurset.add(occur)
        return True
