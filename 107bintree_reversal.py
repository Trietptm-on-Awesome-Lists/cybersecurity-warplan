# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        bottom_up = []
        def depth_first(root, level):

            if root is None:
                return

            try:
                bottom_up[level].append(root.val)
            except:
                bottom_up.append([root.val])

            depth_first(root.left, level + 1)
            depth_first(root.right, level + 1)

        depth_first(root,0)
        return (bottom_up[::-1])
