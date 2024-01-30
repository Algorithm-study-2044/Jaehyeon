class Solution(object):
    def makeSmallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        s_lst = list(s)
        for idx in range(n//2):
            if s_lst[idx]<s_lst[n-1-idx]:
                s_lst[n-1-idx] = s_lst[idx]
            elif s_lst[idx]>s_lst[n-1-idx]:
                s_lst[idx] = s_lst[n-1-idx]
        
        return "".join(s_lst)
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.makeSmallestPalindrome('abcd'))