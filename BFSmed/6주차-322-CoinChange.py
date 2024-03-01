class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        arr = [-1 for _ in range(amount+1)]
        arr[0] = 0
        for n in range(1, amount+1):
            mincount = 99999999999
            for coin in coins:
                if n-coin >=0 and arr[n-coin] != -1 and arr[n-coin]+1 <mincount:
                    mincount = arr[n-coin] + 1
            if mincount == 99999999999:
                arr[n] = -1
            else:
                arr[n] = mincount
        return arr[-1]