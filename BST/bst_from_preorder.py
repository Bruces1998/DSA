def bst_from_preorder(preorder):
    def cons(A, start, end):
        if start >= end:
            return None
        
        root = TreeNode(A[start])
        i = start+1
        
        while(i < end):
            if A[i] > root.val:
                break
            i += 1
        
        j = i
        while(j < end):
            if A[j] <= root.val:
                break

            j +=1

        root.left = cons(A, start+1, i)
        root.right = cons(A, i, j)

        return root

    return cons(preorder, 0, len(preorder))