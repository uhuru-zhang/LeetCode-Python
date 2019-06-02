# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal(self, root: TreeNode) -> list:
        result = []
        stack = []  # 数组模拟栈
        last_visit = root
        while root is not None or len(stack) > 0:
            while root is not None:
                stack.append(root)
                root = root.left
            root = stack[-1]
            if root.right is None or root.right == last_visit:
                result.append(root.val)
                stack.pop()
                last_visit = root
                root = None
            else:
                root = root.right
        return result
