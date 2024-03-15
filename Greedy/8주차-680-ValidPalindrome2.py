class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        leftpt = 0
        rightpt = len(s)-1

        while leftpt < rightpt:
            if s[leftpt] == s[rightpt]:
                leftpt += 1
                rightpt -= 1
            else:
                leftpt1 = leftpt + 1
                rightpt1 = rightpt
                while leftpt1<rightpt1:
                    if s[leftpt1] == s[rightpt1]:
                        leftpt1 += 1
                        rightpt1 -= 1
                    else:
                        break
                leftpt2 = leftpt 
                rightpt2 = rightpt - 1
                while leftpt2<rightpt2:
                    if s[leftpt2] == s[rightpt2]:
                        leftpt2 += 1
                        rightpt2 -= 1
                    else:
                        break
                break
        
        if leftpt >= rightpt or leftpt1 >= rightpt1 or leftpt2 >= rightpt2:
            return True
        else:
            return False