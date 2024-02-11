class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        m = len(image)
        n = len(image[0])
        beforecolor = image[sr][sc]
        aftercolor = color
        if beforecolor == aftercolor:
            return image
            
        def DFS(r, c):
            image[r][c] = aftercolor
            if r>0 and image[r-1][c] == beforecolor:
                DFS(r-1, c)
            if r<m-1 and image[r+1][c] == beforecolor:
                DFS(r+1, c)
            if c>0 and image[r][c-1] == beforecolor:
                DFS(r, c-1)
            if c<n-1 and image[r][c+1] == beforecolor:
                DFS(r, c+1)
            
        DFS(sr, sc)
        return image