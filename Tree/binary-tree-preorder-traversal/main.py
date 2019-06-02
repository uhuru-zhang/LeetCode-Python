# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> list:
        result = []

        stack = []
        stack.append(root)
        while len(stack) > 0:
            current = stack.pop()
            result.append(current)
            if current.right is not None:
                stack.append(current.right)
            if current.left is not None:
                stack.append(current.left)

        return result