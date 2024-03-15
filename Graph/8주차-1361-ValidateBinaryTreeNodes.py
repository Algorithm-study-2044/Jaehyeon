class Solution(object):
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        """
        :type n: int
        :type leftChild: List[int]
        :type rightChild: List[int]
        :rtype: bool
        """
        parlst = [-1 for _ in range(n)]
        for par, child in enumerate(leftChild):
            if child!=-1:
                if parlst[child] == -1:
                    parlst[child] = par
                else:
                    return False
        for par, child in enumerate(rightChild):
            if child!=-1:
                if parlst[child] == -1:
                    parlst[child] = par
                else:
                    return False
        
        count = 0
        root = -1
        for node, par in enumerate(parlst):
            if par == -1:
                count += 1
                root = node
        if count != 1:
            return False
        
        global visitcnt
        visitcnt = 0
        
        def DFS(node):
            global visitcnt
            visitcnt += 1
            lchild = leftChild[node]
            rchild = rightChild[node]
            if lchild != -1:
                DFS(lchild)
            if rchild != -1:
                DFS(rchild)
        
        DFS(root)
        if visitcnt == n:
            return True
        else:
            return False