def isBST(node):
    if node == None:
        return True

    if node.right  and node.right.val < node.val:
        return False

    if node.left and node.left.val > node.val:
        return False

    if not isBST(node.left) or not isBST(node.right):
        return False

    return True