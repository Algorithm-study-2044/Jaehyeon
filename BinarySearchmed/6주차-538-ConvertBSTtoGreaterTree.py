# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        global keysum
        keysum = 0
        def DFS(node):
            global keysum
            if node.right:
                DFS(node.right)
            keysum += node.val
            node.val = keysum
            if node.left:
                DFS(node.left)
            
        if root:
            DFS(root)

        return root