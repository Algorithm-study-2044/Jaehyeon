class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = s[0]
        dp = [[False for _ in range(len(s))] for __ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                ans = s[i: i+2]
        for d in range(2, len(s)):
            for i in range(len(s)-d):
                if (s[i] == s[i+d]) and dp[i+1][i+d-1]:
                    dp[i][i+d] = True
                    if d+1 > len(ans):
                        ans = s[i: i+d+1]
        return ans