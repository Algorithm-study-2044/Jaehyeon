# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def DFS(node, arr):
            if node == None:
                return
            DFS(node.left, arr)
            arr.append(node.val)
            DFS(node.right, arr)
        
        arr = []
        DFS(root, arr)
        return arr