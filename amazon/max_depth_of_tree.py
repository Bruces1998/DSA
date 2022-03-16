def max_depth(root):
    if root == None:
        return 0
    
    lh = max_depth(root.left)
    lr = max_depth(root.right)

    return 1 + max(lh+lr)

#Has a time complexity of O(n) and space complexity of 
# O(H) where H is the height of the tree.