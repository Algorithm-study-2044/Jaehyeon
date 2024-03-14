from collections import deque
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        lastchardict = dict()
        for i, c in enumerate(s):
            lastchardict[c] = i
        
        stack = []
        usedchar = set()
        for idx, c in enumerate(s):
            if c not in usedchar:
                while stack and stack[-1] > c and lastchardict[stack[-1]] > idx:
                    delel = stack.pop()
                    usedchar.discard(delel)
                stack.append(c)
                usedchar.add(c)

        return ''.join(stack)