class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.bottom = None

def merge(nodeA, nodeB):
    temp = Node(0)
    res = temp

    while a != None and b != None:
        if a.data < b.data:
            temp.bottom = a 
            temp = temp.bottom
            a = a.bottom
        
        else:
            temp.bottom = b
            temp = temp.bottom
            b = b.bottom 

    if a:
        temp.bottom = a
    else:
        temp.bottom = b

    return res.bottom

def flatten(root):
    if root == None or root.next == None:
        return root

    root.next = flatten(root.next)
    root = merge(root, root.next)

    return root