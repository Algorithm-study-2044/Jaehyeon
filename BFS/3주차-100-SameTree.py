# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        Q1 = deque()
        Q2 = deque()
        Q1.append(p)
        Q2.append(q)

        while Q1 and Q2:
            node1 = Q1.popleft()
            node2 = Q2.popleft()
            
            if node1 == None:
                if node2 == None:
                    pass
                else:
                    return False
            else:
                if node2 == None:
                    return False
                else:
                    if node1.val != node2.val:
                        return False
                    Q1.append(node1.left)
                    Q1.append(node1.right)
                    Q2.append(node2.left)
                    Q2.append(node2.right)
        if Q1 or Q2:
            return False

        return True