class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        pallst = []
        ans = s[0]
        for diff in range(2, len(s)+1):
            if diff - len(ans) > 2:
                break
            newlst = []
            for idx in range(1+len(s)-diff):
                if diff == 2 or diff==3:
                    if s[idx] == s[idx+diff-1]:
                        newlst.append(True)
                        ans = s[idx: idx+diff]
                    else:
                        newlst.append(False)
                else:
                    if s[idx] == s[idx+diff-1] and pallst[-2][idx+1]:
                        newlst.append(True)
                        ans = s[idx: idx+diff]
                    else:
                        newlst.append(False)
            pallst.append(newlst)
        
        ans = s[0]
        for diff in range(2, len(s)+1):
            try:
                ansidx = pallst[diff-2].index(True)
                ans = s[ansidx: ansidx+diff]
            except:
                pass
        
        return ans