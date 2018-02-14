# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        values = []
        def depthfirst(root, level):

            if root is None:
                return

            try:
                values[level].append(root.val)
            except IndexError:
                values.append([root.val])

            # End case
            if root.left is None and root.right is None:
                return

            left_val = depthfirst(root.left, level + 1)

            right_val = depthfirst(root.right, level + 1)

        depthfirst(root, 0)
        new_res = []
        for e_level in values:
            new_res.append(sum(e_level)/len(e_level))
        return new_res
