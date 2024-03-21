# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        global ans
        ans = False
        def DFS(node, Sum):
            global ans
            Sum += node.val
            if node.left:
                DFS(node.left, Sum)
            if node.right:
                DFS(node.right, Sum)
            if node.left == None and node.right == None:
                if Sum == targetSum:
                    ans = True
        if root:
            DFS(root, 0)
        return ans