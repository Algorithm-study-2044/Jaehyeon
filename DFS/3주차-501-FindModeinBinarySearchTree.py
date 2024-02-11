# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countDFS(self, root, nodeCount):
        if root.val in nodeCount.keys():
            nodeCount[root.val] += 1
        else:
            nodeCount[root.val] = 1
        if root.left:
            self.countDFS(root.left, nodeCount)
        if root.right:
            self.countDFS(root.right, nodeCount)
        
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        nodeCount = dict()
        self.countDFS(root, nodeCount)
        maxcount = max(nodeCount.values())
        ans = []
        for val, count in nodeCount.items():
            if count == maxcount:
                ans.append(val)
        
        return ans