class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buyidx = len(prices)-2
        sellidx = len(prices)-1
        ans = prices[sellidx] - prices[buyidx]

        while buyidx > 0:
            if prices[buyidx] > prices[sellidx]:
                sellidx = buyidx
            buyidx -= 1
            ans = max(ans, prices[sellidx] - prices[buyidx])
        
        return max(0, ans)