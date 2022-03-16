def kthSmallest(root, k):
    #  Write the code here.

    def inorder(node, arr):
        if node:
            if node.left:
                inorder(node.left, arr)
            arr.append(node.data)
            if node.right:
                inorder(node.right, arr)
                
    arr = []
    inorder(root, arr)
    return arr[k-1]