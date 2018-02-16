class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        # Instead of using the hashset later,
        # I can use it during recursion
        # Check again
        all_elements = {}
        def all_el(root):
            if root is None:
                return

            if root.val not in all_elements:
                all_elements[root.val] = 1
            else:
                all_elements[root.val] += 1

            if root.left is not None:
                all_el(root.left)

            if root.right is not None:
                all_el(root.right)

        all_el(root)

        res = False
        for each_el in all_elements:
            if (k - each_el) in all_elements and ( 2*each_el != k or (2*each_el == k and all_elements[each_el] > 1)):
                    res = True
                    break
        return res
