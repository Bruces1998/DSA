class BSTIterator:
    
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.index = -1
        self.arr = []
        inorder(self.root, self.arr)

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        if self.index==len(self.arr) - 1:
            self.index=-1
            return False
        return True
    # @return an integer, the next smallest number
    def next(self):
        self.index+=1
        return self.arr[self.index]
        

def inorder(root,arr):
    if root!=None:
        if root.left!=None:
            inorder(root.left, arr)
            
        arr.append(root.val)
        
        if root.right!=None:
            inorder(root.right, arr)