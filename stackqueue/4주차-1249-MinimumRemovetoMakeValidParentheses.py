class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        inputlst = list(s)
        # remove )
        ans1 = []
        leftcount = 0
        for c in inputlst:
            if c == '(':
                leftcount += 1
                ans1.append(c)
            elif c == ')':
                if leftcount:
                    leftcount -= 1
                    ans1.append(c)
            else:
                ans1.append(c)
        # remove (
        ans2 = []
        rightcount = 0
        for c in reversed(ans1):
            if c == ')':
                rightcount += 1
                ans2.append(c)
            elif c == '(':
                if rightcount:
                    rightcount -= 1
                    ans2.append(c)
            else:
                ans2.append(c)
        
        return ''.join(ans2[::-1])