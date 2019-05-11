# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    n = None
    count = 0

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.Inorder(root, k)
        return self.n

    def Inorder(self, root, k):
        if root is None:
            return
        self.kthSmallest(root.left, k)
        self.count += 1
        if self.count == k:
            self.n = root.val
            return
        self.kthSmallest(root.right, k)