# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ""

        pre_order = []
        self.__pre_order__(root, pre_order)
        in_order = []
        self.__in_order__(root, in_order)
        return " ".join(map(str, pre_order)) + "-" + " ".join(map(str, in_order))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        ""
        if len(data) == 0:
            return None

        pre_order = data.split("-")[0]
        in_order = data.split("-")[1]

        pre_order = list(map(int, pre_order.split(" ")))
        in_order = list(map(int, in_order.split(" ")))

        return self.__buildTree(pre_order, in_order)

    def __in_order__(self, root, result):
        if root is None:
            return

        self.__in_order__(root.left, result)
        result.append(root.val)
        self.__in_order__(root.right, result)

    def __pre_order__(self, root, result):
        if root is None:
            return

        result.append(root.val)
        self.__in_order__(root.left, result)
        self.__in_order__(root.right, result)

    def __buildTree(self, preorder: list, inorder: list) -> TreeNode:
        if len(preorder) == 1:
            return TreeNode(preorder[0])

        if len(preorder) == 0:
            return None
        index = inorder.index(preorder[0])

        root = TreeNode(preorder[0])
        root.left = self.__buildTree(preorder[1:index + 1], inorder[:index])
        root.right = self.__buildTree(preorder[index + 1:], inorder[index + 1:])

        return root

if __name__ == '__main__':
    c = Codec()


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
