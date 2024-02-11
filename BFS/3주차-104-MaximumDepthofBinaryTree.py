# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        root.depth = 1
        nodeq = deque()
        nodeq.append(root)
        maxdepth = 1
        while nodeq:
            node = nodeq.popleft()
            if node.left:
                node.left.depth = node.depth + 1
                if maxdepth < node.left.depth:
                    maxdepth = node.left.depth
                nodeq.append(node.left)
            if node.right:
                node.right.depth = node.depth + 1
                if maxdepth < node.right.depth:
                    maxdepth = node.right.depth
                nodeq.append(node.right)
        return maxdepth