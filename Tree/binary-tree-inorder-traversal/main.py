# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> list:
        result = []

        stack = []
        current = root
        while current is not None or len(stack) > 0:
            if current is not None:
                stack.append(root)
                current = current.left
            else:
                current = stack.pop()
                result.append(current.val)
                current = current.right

        return result

