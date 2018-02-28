# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        tree_paths = []
        # path = []
        def find_leaves(root, path):

            if root is None:
                return

            if root.left is None and root.right is None:
                if path == "":
                    path = str(root.val)
                else:
                    path += "->" + str(root.val)

                tree_paths.append(path)
                return

            if path == "":
                path = str(root.val)
            else:
                path += "->" + str(root.val)

            find_leaves(root.left, path)
            find_leaves(root.right, path)
        find_leaves(root, "")
        return (tree_paths)
