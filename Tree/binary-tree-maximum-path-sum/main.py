# Definition for a binary tree node.
import sys


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    max_value = -sys.maxsize

    def maxPathSum(self, root: TreeNode) -> int:
        self.get_max(root)
        return self.max_value

    def get_max(self, root):
        if root == None:
            return 0

        left = max(0, self.get_max(root.left))
        right = max(0, self.get_max(root.right))

        self.max_value = max(self.max_value, left + right + root.val)

        return max(left, right) + root.val
