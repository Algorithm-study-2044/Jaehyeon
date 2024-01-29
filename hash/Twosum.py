class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numsdict = dict([])
        for idx, num in enumerate(nums):
            if num in numsdict.keys():
                numsdict[num].append(idx)
            else:
                numsdict[num] = [idx]

        for idxa, a in enumerate(nums):
            b = target - a
            if b in numsdict.keys():
                listb = numsdict[b]
                if listb[0] == idxa:
                    if len(listb)>1:
                        idxb = listb[1]
                        return [idxa, idxb]
                else:
                    idxb = listb[0]
                    return [idxa, idxb]