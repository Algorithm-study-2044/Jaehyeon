# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def removeLeafNodes(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode
        """
        def DFSshoulddelete(node):
            if node.left:
                leftdel = DFSshoulddelete(node.left)
                if leftdel:
                    node.left = None
            if node.right:
                rightdel = DFSshoulddelete(node.right)
                if rightdel:
                    node.right = None
            
            if node.left == None and node.right == None and node.val == target:
                return True
            else:
                return False
        
        rootdel = DFSshoulddelete(root)
        if rootdel:
            return None
        else:
            return root