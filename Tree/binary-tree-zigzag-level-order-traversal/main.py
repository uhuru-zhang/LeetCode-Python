# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        if root is None:
            return []

        nodes = [[root], []]
        i = 0
        result = []

        while len(nodes[i % 2]) != 0:
            current = i % 2
            next = (i + 1) % 2

            line = []
            for node in nodes[current]:
                if current == 0:
                    line.append(node.val)
                else:
                    line.insert(0, node.val)

                if node.left is not None:
                    nodes[next].insert(0, node.left)
                if node.right is not None:
                    nodes[next].insert(0, node.right)

            nodes[current] = []
            i += 1
            result.append(line)
        return result