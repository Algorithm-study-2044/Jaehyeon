# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # exception
        if root == None:
            return []

        # write level
        def DFS(node, lev):
            if node:
                node.level = lev+1
                DFS(node.left, node.level)
                DFS(node.right, node.level)
        DFS(root, -1)

        # BFS
        ans = [root.val]
        q = deque([root])
        level = 0
        while q:
            node = q.pop()
            if node.right:
                q.appendleft(node.right)
            if node.left:
                q.appendleft(node.left)
            if len(q)>1 and q[1].level > level:
                level = q[1].level
                ans.append(q[1].val)
            elif q and q[0].level > level:
                level = q[0].level
                ans.append(q[0].val)
    
        return ans