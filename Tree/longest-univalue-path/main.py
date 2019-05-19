# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.result = 0

    def longestUnivaluePath(self, root: TreeNode) -> int:
        if root is not None:
            left = self.isSame(root.left, root.val, 0)
            right = self.isSame(root.right, root.val, 0)
            return max(left + right,
                       self.longestUnivaluePath(root.left),
                       self.longestUnivaluePath(root.right))

    def isSame(self, root, val, result):
        if root is not None:
            if val == root.val:
                result += 1

                left = self.isSame(root.left, val, result)
                right = self.isSame(root.right, val, result)

                return max(left, right)
        else:
            return result