class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        singleRomantoInt = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D':500, 'M': 1000}
        # result가 int 답
        result = 0
        for idx, c in enumerate(s):
            flagplus = True # c에 해당하는 정수를 +해야 하면 true - 해야 하면 false
            if idx< len(s)-1:
                nextc = s[idx+1]
                if c == 'I':
                    if nextc == 'V' or nextc == 'X':
                        flagplus = False
                if c == 'X':
                    if nextc == 'L' or nextc == 'C':
                        flagplus = False
                if c == 'C':
                    if nextc == 'D' or nextc == 'M':
                        flagplus = False
            if flagplus:
                result += singleRomantoInt[c]
            else:
                result -= singleRomantoInt[c]
        return result
