# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def reverseOddLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        def DFSswap(node1, node2):
            node1.val, node2.val = node2.val, node1.val
            if node1.left == None or node1.left.left == None:
                return
            DFSswap(node1.left.left, node2.right.right)
            DFSswap(node1.left.right, node2.right.left)
            DFSswap(node1.right.left, node2.left.right)
            DFSswap(node1.right.right, node2.left.left)
        
        if root.left:
            DFSswap(root.left, root.right)

        return root