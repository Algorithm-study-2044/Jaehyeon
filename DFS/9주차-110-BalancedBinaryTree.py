# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def DFS(node):
            if node:
                lok, lh = DFS(node.left)
                rok, rh = DFS(node.right)
                return (abs(lh-rh)<=1 and lok and rok), max(lh, rh)+1
            else:
                return True, -1
        
        ok, h = DFS(root)
        return ok