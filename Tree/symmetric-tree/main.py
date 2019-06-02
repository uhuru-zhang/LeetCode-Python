# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.is_mirror(root, root)

    def is_mirror(self, l, r):
        if l is None and r is None:
            return True
        if l is None or r is None:
            return False

        if l.val != r.val:
            return False

        return self.is_mirror(l.left, r.right) and self.is_mirror(l.right, r.left)
