import re
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace(' ', '')
        pattern = r'(\d+|\D)'
        tokens = re.findall(pattern, s)

        numstack = []
        opstack = []
        for c in tokens:
            if c == '+' or c =='-':
                while opstack:
                    op = opstack.pop()
                    if op == '+':
                        b = numstack.pop()
                        a = numstack.pop()
                        numstack.append(a+b)
                    elif op == '-':
                        b = numstack.pop()
                        a = numstack.pop()
                        numstack.append(a-b)
                    elif op == '*':
                        b = numstack.pop()
                        a = numstack.pop()
                        numstack.append(a*b)
                    elif op == '/':
                        b = numstack.pop()
                        a = numstack.pop()
                        numstack.append(a//b)
                opstack.append(c)
            elif c == '*' or c == '/':
                while opstack:
                    op = opstack.pop()
                    if op == '+' or op == '-':
                        opstack.append(op)
                        break
                    elif op == '*':
                        b = numstack.pop()
                        a = numstack.pop()
                        numstack.append(a*b)
                    elif op == '/':
                        b = numstack.pop()
                        a = numstack.pop()
                        numstack.append(a//b)
                opstack.append(c)
            else:
                numstack.append(int(c))
        while opstack:
            op = opstack.pop()
            if op == '+':
                b = numstack.pop()
                a = numstack.pop()
                numstack.append(a+b)
            elif op == '-':
                b = numstack.pop()
                a = numstack.pop()
                numstack.append(a-b)
            elif op == '*':
                b = numstack.pop()
                a = numstack.pop()
                numstack.append(a*b)
            elif op == '/':
                b = numstack.pop()
                a = numstack.pop()
                numstack.append(a//b)

        return numstack[-1]