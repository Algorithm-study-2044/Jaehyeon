class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        count = 0
        for c in s:
            if c == 'R':
                count += 1
            else:
                count -= 1
            if count == 0:
                ans += 1
        
        return ans

if __name__=='__main__':
    sol = Solution()
    print(sol.balancedStringSplit("RLRRRLLRLL"))