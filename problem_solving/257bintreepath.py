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
        def set_string(str_path, val):
            if str_path == "":
                str_path = str(val)
            else:
                str_path += "->" + str(val)
            return str_path

        def find_leaves(root, path):

            if root is None:
                return

            path = set_string(path, root.val)

            if root.left is None and root.right is None:
                tree_paths.append(path)
                return

            find_leaves(root.left, path)
            find_leaves(root.right, path)
        find_leaves(root, "")
        return (tree_paths)
