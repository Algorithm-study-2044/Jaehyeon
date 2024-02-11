# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        depthdict = dict()
        depthdict[root.val] = 0
        parentdict = dict()

        def depthDFS(node):
            if node.left:
                depthdict[node.left.val] = depthdict[node.val] + 1
                parentdict[node.left.val] = node.val
                depthDFS(node.left)
            if node.right:
                depthdict[node.right.val] = depthdict[node.val] + 1
                parentdict[node.right.val] = node.val
                depthDFS(node.right)
        
        depthDFS(root)
        if depthdict[x] == depthdict[y] and parentdict[x] != parentdict[y]:
            return True
        else:
            return False