class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums3 = []
        idx1 = 0
        idx2 = 0
        while idx1<m and idx2<n:
            if nums1[idx1] <= nums2[idx2]:
                nums3.append(nums1[idx1])
                idx1 += 1
            else:
                nums3.append(nums2[idx2])
                idx2 += 1
        while idx1<m:
            nums3.append(nums1[idx1])
            idx1 += 1
        while idx2<n:
            nums3.append(nums2[idx2])
            idx2 += 1
        for idx in range(len(nums1)):
            nums1[idx] = nums3[idx]
