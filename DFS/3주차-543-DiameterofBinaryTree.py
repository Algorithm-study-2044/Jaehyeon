# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def DFSheight(node):
            hleft = -1
            hright = -1
            if node.left:
                DFSheight(node.left)
                hleft = node.left.height
            if node.right:
                DFSheight(node.right)
                hright = node.right.height
            node.height = 1+max(hleft, hright)
        
        DFSheight(root)

        def DFSdiameter(node):
            if node.left == None:
                if node.right == None:
                    return 0
                else:
                    return max(node.height, DFSdiameter(node.right))
            else:
                if node.right == None:
                    return max(node.height, DFSdiameter(node.left))
                else:
                    return max(2+node.left.height+node.right.height, DFSdiameter(node.left), DFSdiameter(node.right))
        
        return DFSdiameter(root)