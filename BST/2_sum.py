'''
Given a binary search tree A, where each node
contains a positive integer, and an integer B, 
you have to find whether or not there exist two 
different nodes X and Y such that X.value + Y.value = B.
Return 1 to denote that two such nodes exist. 
Return 0, otherwise.
'''
def inOrder(self, node, arr, B):
    if (node!=None):
        
        
        if node.left!=None:
            self.inOrder(node.left, arr, B)
        
        if node.val <= B:
            arr.append(node.val)
        
        if node.right!=None:
            self.inOrder(node.right, arr, B)
                
def t2Sum(self, A, B):
    arr = []
    self.inOrder(A, arr, B)
    
    pt1 = 0
    pt2 = len(arr) - 1
    while (pt1!=pt2):
        if arr[pt1] + arr[pt2] > B:
            pt2-=1
        elif arr[pt1] + arr[pt2] < B:
            pt1+=1
        else:
            return 1
    return 0