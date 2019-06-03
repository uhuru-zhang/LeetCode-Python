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
        # 如果当前节点 为 要寻找的节点 那么该节点就被返回 在递归的过程中证明结点在此存在
        # 如果 返回为 None 证明不存在该子树中
        if root == p or root == q or root is None:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # 如果二者存在同一侧证明二者 还可以吧公共节点降到更低
        # 如果不在同一侧 证明已经达到二者的 最低公共节点
        if left is not None and right is not None:
            return root
        elif left is None and right is not None:
            return right
        elif left is not None and right is None:
            return left

        return None
