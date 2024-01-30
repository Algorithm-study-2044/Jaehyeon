class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1,1]]
        else:
            ans = self.generate(numRows-1)
            arr = ans[-1]
            lastarr = [1]
            for idx in range(len(arr)-1):
                lastarr.append(arr[idx]+arr[idx+1])
            lastarr.append(1)
            ans.append(lastarr)
            return ans
        
if __name__ == '__main__':
    sol = Solution()
    print(sol.generate(5))