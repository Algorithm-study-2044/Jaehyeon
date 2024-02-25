class Solution(object):
    def winnerOfGame(self, colors):
        """
        :type colors: str
        :rtype: bool
        """
        a_cnt = 0
        b_cnt = 0
        for idx in range(1, len(colors)-1):
            s = colors[idx-1: idx+2]
            if s == 'AAA':
                a_cnt += 1
            elif s == 'BBB':
                b_cnt += 1
        if a_cnt > b_cnt:
            return True
        else:
            return False