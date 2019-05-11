# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# class Solution:
#     def hasPathSum(self, root: TreeNode, sum: int) -> bool:
#         if root is None:
#             return False
#         sums = self.get_sums(root)
#
#         for n in sums:
#             if n == sum:
#                 return True
#         return False
#
#     def get_sums(self, root):
#         if root is None:
#             return [0]
#
#         left = self.get_sums(root.left)
#         right = self.get_sums(root.right)
#
#         return [n + root.val for n in left] + [n + root.val for n in right]

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False

        if root.left is None and root.right is None and root.val == sum:
            return True

        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
