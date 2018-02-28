# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        max_vals = []

        def tree_levels(root, level):
            if root is None:
                return
            level += 1
            if len(max_vals) < level:
                max_vals.append(root.val)
            else:
                if max_vals[level - 1] < root.val:
                    max_vals[level - 1] = root.val

            tree_levels(root.left, level)
            tree_levels(root.right, level)

        tree_levels(root, 0)
        return (max_vals)
