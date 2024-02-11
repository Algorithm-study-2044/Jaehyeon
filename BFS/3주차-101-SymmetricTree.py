# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        qleft = deque()
        qright = deque()
        qleft.append(root.left)
        qright.append(root.right)

        while qleft and qright:
            leftnode = qleft.popleft()
            rightnode = qright.popleft()
            if leftnode != None and rightnode == None:
                return False
            if leftnode == None and rightnode != None:
                return False
            if leftnode != None and rightnode != None:
                if leftnode.val != rightnode.val:
                    return False
            if leftnode:
                qleft.append(leftnode.left)
                qleft.append(leftnode.right)
            if rightnode:
                qright.append(rightnode.right)
                qright.append(rightnode.left)
        
        if qleft or qright:
            return False
        else:
            return True