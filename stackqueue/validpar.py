class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        bracstack = []
        for c in s:
            if c == '(' or c == '{' or c=='[':
                bracstack.append(c)
            elif not bracstack:
                return False
            elif c==')':
                if bracstack.pop() != '(':
                    return False
            elif c=='}':
                if bracstack.pop() != '{':
                    return False
            elif c==']':
                if bracstack.pop() != '[':
                    return False
        if bracstack:
            return False
        return True
