class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        answers = [[''], ['()']]
        for i in range(2, n+1):
            ans = []
            for j in range(i):
                k = i-1-j
                for a in answers[j]:
                    for b in answers[k]:
                        s = '('+a+')'+b
                        ans.append(s)
            answers.append(ans)
        return answers[-1]