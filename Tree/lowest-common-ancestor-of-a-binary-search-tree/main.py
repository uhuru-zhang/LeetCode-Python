class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root == p or root == q or root is None:
            return root

        p_in_left = self.inPreRoot(root, p)
        q_in_left = self.inPreRoot(root, q)

        # p、q 两个节点只有三种情况
        # 第一种：在不同侧 那么 返回当前节点 证明为最低公共节点
        if p_in_left ^ q_in_left:
            return root
        else:
            # 第二种：同在左侧，那么去左侧寻找
            if p_in_left:
                return self.lowestCommonAncestor(root.left, p, q)
            # 第三种：同在右侧，那么去右侧寻找
            else:
                return self.lowestCommonAncestor(root.right, p, q)

    def inPreRoot(self, root, p):
        if root is None:
            return False

        return root.val >= p.val