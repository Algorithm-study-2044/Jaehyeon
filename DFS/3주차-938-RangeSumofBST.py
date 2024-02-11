# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        sum = 0
        if root == None:
            return 0
        else:
            if low <= root.val <= high:
                sum += root.val
            sum += self.rangeSumBST(self, root.left, low, high)
            sum += self.rangeSumBST(self, root.right, low, high)
            return sum