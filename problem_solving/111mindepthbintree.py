# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Do a depth search, see
        # which side has min len

        def find_min(root, depth):
            if root is None:
                return depth

            depth += 1

            if root.left is None and root.right is None:
                return depth

            dep1 = dep2 = float('inf')
            if root.left is not None:
                dep1 = find_min(root.left, depth)

            if root.right is not None:
                dep2 = find_min(root.right, depth)

            print(dep1,dep2)
            return(min(dep1,dep2))

        res = find_min(root, 0)
        return res
        
