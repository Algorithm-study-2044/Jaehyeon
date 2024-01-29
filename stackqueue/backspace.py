class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        idxs = len(s)
        idxt = len(t)
        while True:
            counts = 0
            while True:
                idxs -= 1
                if idxs < 0:
                    break
                else:
                    if s[idxs] == '#':
                        counts += 1
                    else:
                        if counts == 0:
                            break
                        else:
                            counts -= 1
            countt = 0
            while True:
                idxt -= 1
                if idxt < 0:
                    break
                else:
                    if t[idxt] == '#':
                        countt += 1
                    else:
                        if countt == 0:
                            break
                        else:
                            countt -= 1

            if idxs < 0 and idxt < 0:
                return True
            elif idxs<0 and idxt>=0:
                return False
            elif idxs>=0 and idxt <0:
                return False
            else:
                if s[idxs] != t[idxt]:
                    return False
