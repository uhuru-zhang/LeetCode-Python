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

        if p_in_left ^ q_in_left:
            return root
        else:
            if p_in_left:
                return self.lowestCommonAncestor(root.left, p, q)
            else:
                return self.lowestCommonAncestor(root.right, p, q)

    def inPreRoot(self, root, p):
        if root is None:
            return False

        return root.val >= p.val