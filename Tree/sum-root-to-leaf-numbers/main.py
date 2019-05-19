# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.nums = []

    def sumNumbers(self, root: TreeNode) -> int:
        self.get_values(root, 0)
        return sum(self.nums)

    def get_values(self, root: TreeNode, num: int):
        if root is None:
            return

        num = num * 10 + root.val
        if root.left is None and root.right is None:
            self.nums.append(num)
        else:
            self.get_values(root.left, num)
            self.get_values(root.right, num)
