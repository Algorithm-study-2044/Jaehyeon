# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def validminmax(node):
            m = node.val
            M = node.val
            if node.left:
                v1, m1, M1 = validminmax(node.left)
                if not v1 or M1 >= node.val:
                    return False, 0, 0
                else:
                    m = m1
            if node.right:
                v2, m2, M2 = validminmax(node.right)
                if not v2 or m2 <= node.val:
                    return False, 0, 0
                else:
                    M = M2
            return True, m, M
        
        ans = True
        if root:
            ans = validminmax(root)[0]
        return ans