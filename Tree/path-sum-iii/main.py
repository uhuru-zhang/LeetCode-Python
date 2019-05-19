class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def __init__(self):
        self.result = 0

    def pathSum(self, root: TreeNode, sum: int):
        if root is not None:
            self.hasPathSum(root, sum)
            self.pathSum(root.left, sum)
            self.pathSum(root.right, sum)
        return self.result

    def hasPathSum(self, root: TreeNode, sum: int):
        if root is None:
            return

        if root.val == sum:
            self.result += 1  # 此处不能返回，因为可能会有 后续和为0的序列加入

        self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
