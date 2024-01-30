class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            arr = [0 for _ in range(n+1)]
            arr[1] = 1
            for idx in range(2, n+1):
                arr[idx] = arr[idx-1]+arr[idx-2]
            return arr[n]