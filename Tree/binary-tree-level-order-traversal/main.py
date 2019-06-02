# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.result = []
    def levelOrder(self, root: TreeNode) -> list:
        if root is None:
            return []

        self.__level_order__([root])

        return self.result

    def __level_order__(self, nodes: list):
        self.result.append([node.val for node in nodes])

        next_nodes = []
        for node in nodes:
            if node.left is not None:
                next_nodes.append(node.left)
            if node.right is not None:
                next_nodes.append(node.right)
        if len(next_nodes) > 0:
            self.__level_order__(next_nodes)

