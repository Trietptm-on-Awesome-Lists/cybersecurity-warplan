def maxDepth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    h1,h2 = 0,0
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return 1

    if root.left is not None:
        h1 = maxDepth(root.left) + 1

    if root.right is not None:
        h2 = maxDepth(root.right) + 1

    return max(h1,h2)
