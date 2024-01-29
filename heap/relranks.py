class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        score_argsort = sorted(range(len(score)), key=lambda k: score[k])
        result = [0 for _ in score_argsort]
        n = len(score_argsort)

        for idx in range(1, n+1):
            if idx == 1:
                result[score_argsort[n-idx]] = "Gold Medal"
            elif idx == 2:
                result[score_argsort[n-idx]] = "Silver Medal"
            elif idx == 3:
                result[score_argsort[n-idx]] = "Bronze Medal"
            else:
                result[score_argsort[n-idx]] = str(idx)

        return result