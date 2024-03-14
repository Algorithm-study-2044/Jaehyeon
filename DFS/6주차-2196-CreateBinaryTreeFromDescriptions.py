# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def createBinaryTree(self, descriptions):
        """
        :type descriptions: List[List[int]]
        :rtype: Optional[TreeNode]
        """
        nodedict = dict()
        pset = set()
        cset = set()
        for des in descriptions:
            p, c, isleft = des
            if p not in nodedict:
                nodedict[p] = TreeNode(p, None, None)
            if c not in nodedict:
                nodedict[c] = TreeNode(c, None, None)
            if isleft:
                nodedict[p].left = nodedict[c]
            else:
                nodedict[p].right = nodedict[c]
            pset.add(nodedict[p])
            cset.add(nodedict[c])
        
        return (pset-cset).pop()