# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        ans = []
        def DFS(node):
            if node:
                ispleft, isqleft = DFS(node.left)
                ispright, isqright = DFS(node.right)
                isp = ispleft or ispright or node.val == p.val
                isq = isqleft or isqright or node.val == q.val
                if isp and isq:
                    ans.append(node)
                return isp, isq
            else:
                return False, False
        DFS(root)
        return ans[0]