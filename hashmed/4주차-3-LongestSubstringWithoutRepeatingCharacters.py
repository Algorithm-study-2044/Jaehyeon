class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            maxlen = 1
            right = 0
            letterset = set()
            for left in range(n):
                if left>right:
                    right = left
                while right < n-1:
                    letterset.add(s[right])
                    if s[right+1] in letterset:
                        break
                    right += 1
                if maxlen < right+1-left:
                    maxlen = right+1-left
                letterset.discard(s[left])
            return maxlen