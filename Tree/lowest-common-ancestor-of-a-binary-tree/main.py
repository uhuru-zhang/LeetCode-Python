# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 超时-----------------------------------------------------------------------------------------------------------------------------------------------------------
# class Solution(object):
#     def lowestCommonAncestor(self, root, p, q):
#         """
#         :type root: TreeNode
#         :type p: TreeNode
#         :type q: TreeNode
#         :rtype: TreeNode
#         """
#         if root == p or root == q or root is None:
#             return root
#
#         p_in_left = self.inPreRoot(root.left, p)
#         q_in_left = self.inPreRoot(root.left, q)
#
#         if p_in_left ^ q_in_left:
#             return root
#         else:
#             if p_in_left:
#                 self.lowestCommonAncestor(root.left, p, q)
#             else:
#                 self.lowestCommonAncestor(root.right, p, q)
#
#     def inPreRoot(self, root, p):
#         if root is None:
#             return False
#         if root == p:
#             return True
#
#         return self.inPreRoot(root.left, p) or self.inPreRoot(root.right, p)
# 超时-----------------------------------------------------------------------------------------------------------------------------------------------------------
## 普通二叉树
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root == p or root == q or root is None:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left is not None and right is not None:
            return root
        elif left is None and right is not None:
            return right
        elif left is not None and right is None:
            return left

        return None
