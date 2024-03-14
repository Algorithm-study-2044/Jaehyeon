# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def closestNodes(self, root, queries):
        """
        :type root: Optional[TreeNode]
        :type queries: List[int]
        :rtype: List[List[int]]
        """
        # tree to lst
        arr = []
        def Inordertraversal(node):
            if node.left:
                Inordertraversal(node.left)
            arr.append(node)
            if node.right:
                Inordertraversal(node.right)
        Inordertraversal(root)
        # lst to tree
        def GenerateTree(lst):
            if not lst:
                return None
            mididx = len(lst)//2
            parentnode = lst[mididx]
            parentnode.left = GenerateTree(lst[:mididx])
            parentnode.right = GenerateTree(lst[mididx+1:])
            return parentnode
        root = GenerateTree(arr)

        # search
        ans = []
        for target in queries:
            m = 0
            M = 1000001
            node = root
            while node:
                if node.val == target:
                    m = target
                    M = target
                    break
                elif node.val < target:
                    if m < node.val:
                        m = node.val
                    node = node.right
                else:
                    if M > node.val:
                        M = node.val
                    node = node.left
                    
            if m == 0:
                m = -1
            if M == 1000001:
                M = -1
            ans.append([m, M])
        return ans