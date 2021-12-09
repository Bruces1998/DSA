class Node:
    def __init__(self,x):
        self.right = None
        self.left = None
        self.val = x


class BinaryTree:
    def __init__(self, x):
        root = x


n1 = Node(7)
n2 = Node(96)
n2.right = n1
n3 = Node(125)

n3.right = n2
n3.left = Node(8)

root = Node(100)
root.left = n3

n4 = Node(15)
n4.left = Node(-2)
n4.right = Node(-21)

root.right = n4
def inOrder(node):
    if (node==None):
        return

    if node.left!=None:
        inOrder(node.left)

    print(node.val, end=' ')

    if node.right!=None:
        inOrder(node.right)

inOrder(root)
