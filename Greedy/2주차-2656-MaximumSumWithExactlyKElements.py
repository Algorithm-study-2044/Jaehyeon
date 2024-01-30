class Solution(object):
    def maximizeSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        m = max(nums)
        return (2*m+k-1)*k//2

if __name__ == '__main__':
    sol = Solution()
    nums = [5,5,5]
    k = 2
    print(sol.maximizeSum(nums, k))