class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    result = []

    def pathSum(self, root: TreeNode, sum: int):
        self.result = []
        self.hasPathSum(root, sum, [])
        return self.result

    def hasPathSum(self, root: TreeNode, sum: int, nodes: list):
        if root is None:
            return

        if root.left is None and root.right is None and root.val == sum:
            self.result.append([n for n in nodes] + [root.val])
            return

        self.hasPathSum(root.left, sum - root.val, [n for n in nodes] + [root.val]) or \
        self.hasPathSum(root.right, sum - root.val, [n for n in nodes] + [root.val])