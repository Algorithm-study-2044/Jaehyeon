class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        
        s = str(num)
        for idx, c in enumerate(s):
            if c=='6':
                return int(s[:idx]+'9'+s[idx+1:])
        return int(s)
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.maximum69Number(9999))