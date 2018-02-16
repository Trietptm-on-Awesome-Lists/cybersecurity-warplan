class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        val = ""
        if t is not None:
            val = str(t.val)
            if t.left is not None or t.right is not None:
                val += "("+self.tree2str(t.left)+")"
            if t.right is not None:
                val += "("+self.tree2str(t.right)+")"
        return val
