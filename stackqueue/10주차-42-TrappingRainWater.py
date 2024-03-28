class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        dsc = [0]
        n = len(height)
        ans = 0

        for idx in range(1, n):
            while dsc:
                if height[dsc[-1]] < height[idx]:
                    idx_ = dsc.pop()
                    if dsc:
                        ans += (min(height[dsc[-1]], height[idx])-height[idx_])*(idx-dsc[-1]-1)
                else:
                    break
            dsc.append(idx)
        
        return ans