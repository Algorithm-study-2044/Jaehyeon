class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        ssort = sorted(s)
        tsort = sorted(t)
        for idx in range(len(s)):
            if ssort[idx] != tsort[idx]:
                return False
        return True