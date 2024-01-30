class Solution(object):
    def divisorGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        arr = [False, True, False]
        for m in range(4, n+1):
            flag = False
            for x in range(1, 2+int(m**0.5)):
                if m%x == 0:
                    if arr[m-x-1] == False:
                        flag = True
                        break
            arr.append(flag)
        
        return arr[n-1]
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.divisorGame(6))