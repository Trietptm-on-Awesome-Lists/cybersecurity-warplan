# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is None and t2 is None:
            return None

        if t1 is None:
            t1 = TreeNode(0)
        if t2 is None:
            t2 = TreeNode(0)

        sum_of_nodes = t1.val + t2.val
        print(sum_of_nodes)
        tree = TreeNode(sum_of_nodes)

        if t1.left is not None or t2.left is not None:
            tree.left = self.mergeTrees(t1.left,t2.left)

        if t1.right is not None or t2.right is not None:
            tree.right = self.mergeTrees(t1.right,t2.right)

        return tree


sol = Solution()

t1 = TreeNode(None)
t2 = TreeNode(None)
sol.mergeTrees(None,None)
