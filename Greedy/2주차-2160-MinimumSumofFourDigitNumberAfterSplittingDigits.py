class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        nums = [int(x) for x in str(num)]
        nums.sort()

        return 10*nums[0]+10*nums[1]+nums[2]+nums[3]
    
if __name__ == '__main__':
    sol = Solution()
    num = 4009
    print(sol.minimumSum(num))